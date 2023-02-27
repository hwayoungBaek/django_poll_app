"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),  
    # include() 함수는 다른 URLconf들을 참조할 수 있도록 도와준다
    # Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고,
    # 남은 문자열 부분을 후속 처리를 위해 include된 URLconf로 전달한다
    path('admin/', admin.site.urls),
]


'''
Django는 URL 패턴을 사용한다
URL 의 일반적인 형식은 /newsarchive/<year>/<month>/
URL로부터 뷰를 얻기 위해, Django는 'URLconfs'라는 것을 사용한다
URLconf는 URL 패턴을 뷰에 연결한다.
'''