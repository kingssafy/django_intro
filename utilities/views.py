from django.shortcuts import render 
from datetime import datetime
from django.http import HttpResponse
import requests
import os

# Create your views here.

def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    now = datetime.now()
    target_date = datetime(2019, 2, 28, 0, 0)
    result = target_date - now
    context = {"result" : result}
    return render(request, 'utilities/bye.html', context)

def graduation(request):
    now = datetime.now()
    target_date = datetime(2019, 5, 18)
    result = target_date - now
    result = result.days
    context = {"result" : result}
    return render(request, 'utilities/graduation.html', context)

def imagepick(request):
    return render(request, 'utilities/imagepick.html')

def today(request):
    key = os.getenv("WEATHERKEY")
    url = "https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID="
    url += key
    info = requests.get(url).json()
    temp = info["main"]["temp"]
    temp -= 273
    temp = round(temp, 2)
    return render(request, 'utilities/today.html', {"temp": temp})

def ascii_new(request):
    fonts = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    context = {"fonts": fonts}
    return render(request, 'utilities/ascii_new.html', context)

def ascii_make(request):
    text = request.GET.get("text")
    font = request.GET.get("font")
    url = "http://artii.herokuapp.com/make"
    url += "?text=" + text + "&"
    url += "?font=" + font
    result = requests.get(url) 
    context = {"result": result.text}
    return render(request, 'utilities/ascii_make.html', context)



def original(request):
    return render(request, 'utilities/original.html')

def translated(request):
    naver_client_id = os.getenv("NAVER_CLIENT_ID")
    naver_client_secret = os.getenv("NAVER_CLIENT_SECRET")
    text = request.GET.get("text")
    papago_url = "https://openapi.naver.com/v1/language/translate"
    # 네이버에 Post 요청을 위해서 필요한 내용들
    headers = {
        "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    data = {
        "source": "ko",
        "target": "en",
        "text": text
    }
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    print(papago_response)
    reply_text = papago_response['message']["result"]["translatedText"]
    context = {
            "text": reply_text,
            }
    return render(request, 'utilities/translated.html', context)
