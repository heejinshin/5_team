from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse("<h1>Person</h1>")

# def index(request):
#     return render(request, 'service/choosebar.html')

def show_map(request):
    return render(request, 'service/map.html')

import csv
from service.models import MyModel
from service.forms import MyForm



# from service.forms import MyForm

# html에서 받아온 사용자 값을 모델에 저장하기 (우리의 데이터)
def save(request):
    data = request.POST.get('searchInput')
     # form 객체 다 들고옴 ; 클라이언트로 부터 전달된 데이터인 form 객체를 생성 
    # if data.is_valid():
        # result = form.sav/e(commit=True)  # 디비에 알아서 저장된다. Insert쿼리 자동생성ㅇ
    return HttpResponse(data)
    

# csv파일을 불러와서 모델에 저장하기 (보여줄 데이터)

def save_data_to_model(request):
    csv_file = settings.DATA_CSV_URL
    with open(csv_file, 'r', newline='') as file:  # file 변수에 할당하여 읽기위함
        reader = csv.DictReader(file)  # csv파일을 읽음 
        for row in reader:
            MyModel.objects.create(
                store_name = row['상호명'],
                store_code = row['상권업종중분류코드'],
                store_segment=row['상권업종중분류명'],
                address_dong=row['법정동명'],
                address_road=row['도로명'],
                longitude=float(row['경도']),
                latitude=float(row['위도'])
            )
        # form_object = my_form.save(commit=True)   # 저장된 데이터의 모든 필드값을 갖는다. 
    # return redirect(form_object)


from django.http import HttpResponse

def write(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            if request.POST.get("btnradio") == "외식업":
                board.category = "외식업"
            elif request.POST.get("btnradio") == "소매업":
                board.category = "소매업"
            board.save()

            return HttpResponse("글이 성공적으로 저장되었습니다.")
    else:
        form = UserInputForm()

    context = {"form": form}
    return render(request, "board/board_write.html", context)

def generate_report(request):
    # 특정 영역의 경도, 위도 범위를 설정합니다.
    min_longitude = 126.956
    max_longitude = 127.007
    min_latitude = 37.47
    max_latitude = 37.51                              

    # 특정 영역 내에 있는 상권 정보를 조회합니다.
    model_result = MyModel.objects.filter(
        longitude__gte = min_longitude,
        longitude__lte = max_longitude,
        latitude__gte = min_latitude,
        latitude__lte = max_latitude
    )

    # 조회된 상권 정보를 리포트로 보여줍니다.
    context = {'model_result': model_result}
    return render(request, "service/report.html", context)


from django.shortcuts import render, redirect
from .forms import UserInputForm


# 사용자 입력값 받기 
def user_input_view(request):   
    if request.method == 'POST':
        form = UserInputForm(request.POST)
        if form.is_valid():
            form.save()  # 입력 값을 데이터베이스에 저장
            return redirect('success')  # 저장 후 리다이렉션할 URL
    else:
        form = UserInputForm()
    return render(request, 'index.html', {'form': form})


from django.http import HttpResponse

def write(request):
    if request.method == "POST":
        form = UserInputForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            if request.POST.get("btnradio") == "외식업":
                board.category = "외식업"
            elif request.POST.get("btnradio") == "소매업":
                board.category = "소매업"
            board.save()

            return HttpResponse("글이 성공적으로 저장되었습니다.")
    else:
        form = UserInputForm()

    context = {"form": form}
    return render(request, "board/board_write.html", context)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserInputModel

@csrf_exempt
def save_checked_values(request):  
    # 요청 값을 받아서, 포스트로 받으면. 
    # checkedvalues 리스트에 점포 유형이 들어온거에 대한 변수를 만들어서 
    if request.method == "GET":
        checked_values = request.POST.getlist("checkedValues[]")
        print(checked_values)
        # 선택된 checkbox의 카운트를 저장하는 로직
        # 예를 들어, CheckedValues 모델에 저장한다고 가정하면:
        for value in checked_values:
            checked_value, created = UserInputModel.objects.get_or_create(value=value)
            checked_value.count += 1
            checked_value.save()

        return JsonResponse({"message": "선택된 카운트가 저장되었습니다."})

    return JsonResponse({"message": "잘못된 요청입니다."})
