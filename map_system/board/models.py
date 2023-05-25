from django.db import models

class Board(models.Model):
    title = models.CharField("제목", max_length=400)
    writer = models.CharField("작성자", max_length=40)
    contents = models.TextField("내용")
    wdate = models.DateField()  # 작성일
    hlt = models.IntegerField()  # 조회수
    filename = models.CharField(max_length=200)



# python manage.py makemigrations board 
# python manage.py migrate   

# select trable_name from tabs;

