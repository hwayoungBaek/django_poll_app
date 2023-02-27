from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

'''
브라우저에서 "/polls/34" 주소에 접속하면 detail() 함수를 호출하여 URL에 입력한 ID를 출력할 것이다.

1) 사용자가 "/polls/34"를 요청하면, Django는 mysite.urls 파이썬 모듈을 불러오게 된다. (ROOT_URLCONF 설정에 의해 여기 모듈을 바라보도록 지정되어 있음)
2) mysite.urls에서 urlpatterns라는 변수를 찾고, 순서대로 패턴을 따라간다.
'polls/'를 찾은 후엔, 일치하는 텍스트("polls/")를 버리고, 남은 텍스트인 "34/"를 'polls.url' URLconf로 전달하여 남은 처리를 진행한다.
3) 거기에 '<int:question_id>/'와 일치하여, 결과적으로 detail()뷰 함수가 호출된다.
detail(request=<HttpRequest object>, question_id=34)
question_id=34 부분은 <int:question_id>에서 왔다. 
꺾쇠 괄호(<>)를 사용하면 URL의 일부가 "캡쳐"되어 키워드 인수로 view함수에 전송된다.
문자열의 question_id 부분은 일치하는 패턴을 식별하는데 사용할 이름을 정의하고, int 부분은 URL 경로의 이 부분과 일치하는 패턴을 결정하는 변환기이다.
콜론(:)은 컨버터와 패턴 이름을 구분한다.
'''