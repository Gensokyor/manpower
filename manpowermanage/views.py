from django.shortcuts import render, redirect, reverse,HttpResponse
from manpowermanage import registlogin
import pprint


def test(request):
    return render(request, 'page\login-1.html')


def test2(request):
    return render(request, 'page\\user-setting.html')


def loginpage(request):
    if request.session.get("login_status"):
        login_status = request.session.get("login_status")
        if login_status == '1':
            return redirect(reverse('home'))
    return render(request, 'loginpage.html')


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        pwd = request.POST.get('pwd')
        result = registlogin.longin(username=account, pwd=pwd)
        pprint.pprint(request.POST)
        return HttpResponse('io')


def home(request):
    pass
