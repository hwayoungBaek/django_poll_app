import datetime

from django.db import models
from django.utils import timezone

# 모델마다 여러 클래스 변수가 있으며,
# 각 클래스 변수는 모델에서 데이터베이스 필드를 나타냅니다.

# 데이터베이스의 각 필드는 Field 클래스의 인스턴스로 표현
# CharField: 문자필드, DateTimeField: 날짜시간 필드, IntegerField: 정수 필드
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # CharField는 max_length를 입력해줘야 한다
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    # ForeignKey로 관계 설정
    # Choice가 하나의 Question에 관계된다
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        # 모델에 __str__() 메소드 추가
        # 1) 대화식 프롬프트에서 객체의 표현을 편하게 보기 위해
        # 2) Django가 자동으로 생성하는 관리 사이트에서도 객체의 표현이 사용되기 때문
