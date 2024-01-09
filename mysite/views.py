from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
from .models import MainContent

# Create your views here.

def index(request):
    #return HttpResponse("Hello world")
    content_list=MainContent.objects.order_by('-pub_date') #-붙여 최신 콘텐츠를 상단에 노출
    context={'content_list':content_list}
    return render(request,'mysite/content_list.html',context) #render는 mysite/content_list.html파일에 적용 후 HTML을 리턴.


