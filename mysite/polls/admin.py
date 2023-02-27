from django.contrib import admin
from .models import Question

admin.site.register(Question)  # 관리 인덱스 페이지에 Question 등록