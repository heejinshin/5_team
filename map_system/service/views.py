from django.shortcuts import render, redirect
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("<h1>Person</h1>")

def index(request):
    return render(request, 'service/choosebar.html')

def show_map(request):
    return render(request, 'service/map.html')

import csv
from service.models import MyModel



from service.forms import MyForm

# html에서 받아온 사용자 값을 모델에 저장하기 (우리의 데이터)
def save(request):
    form = MyForm(request.POST)  # form 객체 다 들고옴 ; 클라이언트로 부터 전달된 데이터인 form 객체를 생성 
    if form.is_valid():
        result = form.save(commit=True)  # 디비에 알아서 저장된다. Insert쿼리 자동생성ㅇ
    return redirect("service:list")

# csv파일을 불러와서 모델에 저장하기 (보여줄 데이터)
csv_file = 'service/data.csv'
def save_data_to_model(csv_file):
    with open(csv_file, 'r', newline='') as file:  # file 변수에 할당하여 읽기위함
        reader = csv.DictReader(file)  # csv파일을 읽음 
        for row in reader:
            my_form = MyForm()
            my_form.상호명 = row['상호명']
            my_form.업종코드 = row['상권업종중분류코드']
            my_form.업종분류명 = row['상권업종중분류명']
            my_form.법정동명 = row['법정동명']
            my_form.도로명 = row['도로명']
            my_form.경도 = float(row['경도'])
            my_form.위도 = float(row['위도'])
        # form_object = my_form.save(commit=True)   # 저장된 데이터의 모든 필드값을 갖는다. 

def write(request): 
    context = {"form": my_form.상호명}
    return render(request, "service/", context)


