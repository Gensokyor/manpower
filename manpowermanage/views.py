from django.shortcuts import render, redirect, reverse, HttpResponse
from manpowermanage import registlogin
import pprint
from datetime import datetime
from manpowermanage.models import *


def test(request):
    return render(request, 'page\login-1.html')


def test2(request):
    return render(request, 'page\\user-setting.html')


def loginpage(request):
    if request.session.get("login_status", None):
        login_status = request.session.get("login_status", None)
        if login_status == 1:
            return redirect(reverse('home'))
    return render(request, 'loginpage.html')


def home(request):
    recommends = registlogin.get_recommend()
    if request.session.get('account_type') == '3':
        return render(request, "user.html", {"recommends": recommends})
    if request.session.get('account_type') == '2':
        return render(request, "companys.html", {"recommends": recommends})
    if request.session.get('account_type') == '1':
        return render(request, "massage.html", {"recommends": recommends})
    return redirect(reverse('loginpage'))
    # return render(request, "home.html", {"recommends": recommends})


def PTasks(request):
    uid = request.session['uid']
    pids = registlogin.edit_Tasks(uid=uid, op='query', pid=None)['query']
    fin = []
    for i in pids:
        fin.append(registlogin.edit_Projects(pid=i['pid'], op='edit', uid=None)['edit'])

    return render(request, "personal-tasks2.html", {'dic': fin})


def projectData(request):  #########################################
    if request.method == 'GET':
        pid = request.GET.get('pid', None)
        if pid:
            target = registlogin.edit_Projects(pid=pid, op='edit', uid=None)
            target = target['edit']

            pprint.pprint(target)
            return render(request, "projectdata.html", target)
    return redirect(reverse('home'))


def projectlist(request):  ######################################
    uid = request.session['uid']
    result = registlogin.edit_Projects(uid=uid, op='query')
    dic = result['query']
    return render(request, "projectlist2.html", {'dic': dic})


def search(request):
    if request.method == 'GET':
        pid = request.GET.get('title', None)
    result = registlogin.edit_Projects(pid=pid, op='edit', uid=None)
    dic = result['edit']
    return render(request, "search2.html", {'dic': [dic]})


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        pwd = request.POST.get('pwd')
        result = registlogin.longin(username=account, pwd=pwd)
        if result:
            request.session['login_status'] = 1
            request.session['account'] = result['account']
            request.session['uid'] = result['uid']
            request.session['account_type'] = result['account_type']
            pprint.pprint(request.POST)
            return redirect(reverse('home'))  ##############################################跳转home
        else:
            return redirect(reverse('loginpage'))


def corp_settings(request):
    return render(request, 'company-setting2.html')
    # if request.session.get('login_status',None)=='1':


def flush(request):
    request.session.flush()
    return redirect(reverse('loginpage'))


def setting_corp(request):
    # pprint.pprint(request.POST)
    if request.method == 'POST':
        pprint.pprint(request.session['login_status'])
        if request.session['login_status'] == 1:
            new_corp_info = request.POST
            a = {}
            a['QQ'] = new_corp_info['QQ']
            a['intro'] = new_corp_info['intro']
            a['mail'] = new_corp_info['mail']
            a['phone'] = new_corp_info['phone']
            a['file'] = new_corp_info['file']  ##########################################图片上传
            a['uid'] = request.session['uid']
            userinfo_res = registlogin.edit_UserInfo(uid=a['uid'], tel=a['phone'], QQ=a['QQ'], mail=a['mail'])
            corpinfo_res = registlogin.edit_CorpInfo(uid=a['uid'], intro=a['intro'])
            pprint.pprint(userinfo_res)
            pprint.pprint(corpinfo_res)
    return HttpResponse(request.POST)


def edit_project(request):
    return render(request, 'edit2.html')


def edit_pro(request):
    # pprint.pprint(request.POST)
    if request.method == 'POST':
        # pprint.pprint(request.session['login_status'])
        if request.session['login_status'] == 1:
            new_pro = {}
            posts = request.POST
            new_pro['title'] = posts['title']
            new_pro['intro'] = posts['']
            new_pro['st_date'] = datetime.strptime(posts['st_date'], "%Y-%m-%d")
            new_pro['end_date'] = datetime.strptime(posts['end_date'], "%Y-%m-%d")
            new_pro['uid'] = request.session['uid']
            result = registlogin.edit_Projects(uid=new_pro['uid'], op='new', st_time=new_pro['st_date'],
                                               end_time=new_pro['end_date'], title=new_pro['title'],
                                               intro=new_pro['intro'])
            pprint.pprint(result)
            return HttpResponse(result)
    return HttpResponse('new fail')


def regist(request):
    if request.method == 'POST':
        post = request.POST
        account = post.get('account', None)
        pwd = post.get('pwd', None)
        name = post.get('name', None)
        if account and pwd and name:
            result = registlogin.regist_account(newaccount=account, newpwd=pwd, name=name, account_type=3)
            if result:
                request.session['login_status'] = 1
                request.session['uid'] = result.uid
                request.session['account_type'] = result.account_type
                return redirect(reverse('home'))
    return redirect(reverse('loginpage'))


def user_settings(request):
    return render(request, 'user-setting2.html')


def setting_user(request):
    result = {}
    if request.method == 'POST':
        a = request.POST
        uid = request.session['uid']
        result['PersonInfo'] = registlogin.edit_PersonInfo(uid=uid, college=a['college'], major=a['major'],
                                                           degree=a['degree'], grade=a['collgradeege'],
                                                           intro=a['intro'])
        result['UserInfo'] = registlogin.edit_UserInfo(uid=uid, tel=a['phone'], QQ=a['QQ'], mail=a['mail'])
        return redirect(reverse('home'))
    return redirect(reverse('home'))


def see_corp(request):
    if request.method == 'GET':
        gets = request.GET
        uid = gets.get('uid')
        intro = registlogin.edit_CorpInfo(uid=uid)['intro']
        name = UserAccount.objects.filter(uid=uid).first().name
        pros = Projects.objects.filter(uid=uid)
        Cos = Comments.objects.filter(uid=uid)
        return render(request, 'company2.html', {'uid': uid, 'intro': intro, 'name': name, 'pros': pros, 'Cos': Cos})
    return redirect(reverse('home'))


def new_Comment(request):
    post=request.POST
    fl=post['fl']
    content=post['intro']
    uid=post["uid"]

    result=registlogin.edit_Comments(uid, op='add', cid=None, content=content,favor_lever=fl)


    return  HttpResponse('ok')
