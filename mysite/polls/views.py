from django.http import HttpResponse
#from django.template import loader  #django의 템플릿 시스템 (python 로직 코드와 페이지의 디자인 뷰 분리)
from django.shortcuts import get_object_or_404, render  #template loader 대신 render사용
from django.http import Http404

from .models import Question  #Django 자체 데이터베이스 API를 사용하기 위해

# 색인 페이지
# 최근의 질문들을 표시한다.
def index(request):
    '''
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # 시스템에 저장된 최신 발행일 투표 질문 최소 5개 
    template = loader.get_template('polls/index.html')
    context = {  # 템플릿에서 쓰이는 변수명과 python 객체를 연결하는 사전형 값
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    '''
    # 위의 코드 개선 => render() 사용
    # 템플릿에 context를 채워넣어 표현한 결과를 HttpResponse 객체와 함께 돌려주는 구문은 자주 쓰는 용법이다
    # 따라서 Django에서는 shortcurts 기능을 제공한다.
    # 아래가 shortcuts 기능으로 다시 작성한 것이다.
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# 세부 페이지
# 질문 내용과 투표할 수 있는 서식을 표시한다
def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)  # 요청된 질문의 ID가 없을 경우 Http404 예외를 발생시킨다.
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question':question})
    '''
    # 위의 코드 개선 => get_object_or_404()
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

# 결과 페이지
# 특정 질문에 대한 결과를 표시한다
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# 투표 기능
# 특정 질문에 대한 특정 선택을 할 수 있는 투표 기능을 제공한다
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)