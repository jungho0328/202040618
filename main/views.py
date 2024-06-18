from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

grade_db = [
  {
    "_id": "1bcc7d45-6e43-41ed-B3ea-b2e6170cc6b7",
    "index": "1",
    "teacher": "노승현",
    "phone": "010-7373-8512",
    "grade": "2",
    "num": "5",
    "contents": "전직대통령의 국회가 30인 15일 생산 관하여 법률로서 국민. 둔다 15일"
  },
  {
    "_id": "6aa7c3dd-b2a0-4c00-B5ac-1a21f8d6258f",
    "index": "2",
    "teacher": "섭보경",
    "phone": "010-6825-0950",
    "grade": "2",
    "num": "12",
    "contents": "보배를 없을 헌법재판소에 부패를 같지 못할 제외하고는 경우를. 주며 중립성은"
  },
  {
    "_id": "de1fc3d7-5ce2-41ea-Bb98-875878c6539f",
    "index": "3",
    "teacher": "변린",
    "phone": "010-9132-0421",
    "grade": "3",
    "num": "4",
    "contents": "현역을 발할 헤는 끓는 선거관리위원회를 의결된 끝까지 국회의원의. 추가경정예산안을 있습니다"
  },
  {
    "_id": "c718967e-fef4-4039-A1ac-272ce1f40c46",
    "index": "4",
    "teacher": "엄진혁",
    "phone": "010-7327-8341",
    "grade": "3",
    "num": "9",
    "contents": "법률안은 뜨거운지라 같은 관여할 변호인의 대통령·국무총리와 않는 이것이야말로. 행하고 까닭이요"
  },
  {
    "_id": "e4966f28-e70a-46b5-A257-a2066ba85a23",
    "index": "5",
    "teacher": "당동진",
    "phone": "010-9513-6427",
    "grade": "2",
    "num": "10",
    "contents": "전과 목숨이 영역안에서의 날로부터 동의권을 재판관의 문서로써 있음으로써. 군사법원의 우리의"
  }
]



def index(request):
    return render(request,'main/index.html')

def jejuohyun(request):
    return render(request,'main/jejuohyun.html')

def high_1st(request):
    return render(request,'main/high_1st.html')

def high_2nd(request):
    return render(request,'main/high_2nd.html')

def high_3rd(request):
    return render(request,'main/high_3rd.html')

def my_page(request):
    return render(request,'main/my_page.html')

def grade(request):
    return render(request,'main/grade.html')
