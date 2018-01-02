#coding=utf-8
from django.http.response import HttpResponse
from django.shortcuts import render

from .utils import gene_code

def virfy_code(request):
    content,text = gene_code()
    request.session['virify']=str(text) # 产生的验证码存储到session中
    return HttpResponse(content=content,content_type='image/png')

from django.views import View
class LoginView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        account = request.POST.get('account')
        password = request.POST.get('password')
        virify = request.POST.get('virfy')
        if virify==request.session.get('virify'):
            if account == 'admin' and password == 'xxye2205790462':
                return HttpResponse('登录成功')
            else:
                return HttpResponse('账号密码不对')
        else:
            return HttpResponse('验证码不对')
