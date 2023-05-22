from django.db import models

# Create your models here.
# 입력된 값으로 주소를 추리도록 
# 2. 업종선택을 눌렀을 때 쿼리에서 중식 및 한식 이런식으로 선택하도록 

from django import forms
from service.models import Datas

class MyForm(forms.ModelForm):
    class Meta:  # 클래스 안에 Meta 라는 이름의 클래스 또 생성
        model = Datas
        fields = ["상호명", "업종코드", "업종분류명", "법종동명", "도로명", "경도", "위도"]

        labels = {
            "상호명": "상호명",
            "업종코드": "업종코드",
            "업종분류명": "업종분류명",
            "법정동명": "법정동명",
            "도로명": "도로명",
            "경도": "경도",
            "위도": "위도"
        }


# form.py

