from manpowermanage.models import *
from manpowermanage.idgenerator import *
from django.http import HttpResponse


def regist_account(newaccount: str, newpwd: str, name: str):
    if lencontent_check('str', 'account', newaccount) and lencontent_check('str', 'pwd', newpwd) and lencontent_check(
            'str', 'name', name):
        uid = Idgenerator('uid')
        result = UserAccount.objects.create(uid=uid, account=newaccount, pwd=newpwd, account_type=3, name=name)
        print(result, type(result))
        return result
    else:
        return False


def longin(username: str, pwd: str):
    result = {}
    queryresult = UserAccount.objects.filter(account=username, pwd=pwd)
    if queryresult.first():
        queryresult = queryresult.first()
        print(queryresult)
        result['uid'] = str(queryresult.uid)
        result['account'] = queryresult.account
        result['name'] = queryresult.name
        result['account_type'] = str(queryresult.account_type)
    return result


def edit_UserInfo(uid, photo=None, tel=None, QQ=None, mail=None):
    result = {}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if isinstance(uid, int):
        if UserAccount.objects.filter(uid=uid).exists():
            if not UserInfo.objects.filter(uid=uid):
                UserInfo.objects.create(uid=uid)
            target = UserInfo.objects.filter(uid=uid).first()
            if photo:
                target.photo = photo
                target.save()
            if tel:
                target.tel = tel
                target.save()
            if QQ:
                target.QQ = QQ
                target.save()
            if mail:
                target.mail = mail
                target.save()
            result['uid'] = target.uid
            result['photo'] = target.photo
            result['tel'] = target.tel
            result['QQ'] = target.QQ
            result['mail'] = target.mail
    return result


def edit_PersonInfo(uid, college=None, major=None, degree=None, grade=None, intro=None):
    result = {}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if isinstance(uid, int):
        if UserAccount.objects.filter(uid=uid).exists():
            if not PersonInfo.objects.filter(uid=uid):
                PersonInfo.objects.create(uid=uid)
            target = PersonInfo.objects.filter(uid=uid).first()
            if college:
                target.college = college
                target.save()
            if major:
                target.major = major
                target.save()
            if degree:
                target.degree = degree
                target.save()
            if grade:
                target.grade = grade
                target.save()
            if intro:
                target.intro = intro
                target.save()
            result['uid'] = target.uid
            result['college'] = target.college
            result['major'] = target.major
            result['degree'] = target.degree
            result['grade'] = target.grade
            result['intro'] = target.intro
    return result


def edit_CorpInfo(uid, license_dsid=None, intro=None):
    result = {}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if isinstance(uid, int):
        if UserAccount.objects.filter(uid=uid).exists():
            if not CorpInfo.objects.filter(uid=uid):
                CorpInfo.objects.create(uid=uid)
            target = CorpInfo.objects.filter(uid=uid).first()
            if license_dsid:
                target.license_dsid = license_dsid
                target.save()
            if intro:
                target.intro = intro
                target.save()
            result['uid'] = target.uid
            result['license_dsid'] = target.license_dsid
            result['intro'] = target.intro
    return result


def edit_Comments(uid, op: str, cid=None, content=None):
    result = {'op': op}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if isinstance(uid, int):
        if UserAccount.objects.filter(uid=uid).exists():
            if op == 'query':
                target = Comments.objects.filter(uid=uid)
                result['query'] = []
                if target:
                    for i in target:
                        result['query'].append(i.cid, i.uid, i.content)
            elif op == 'add':
                result['add'] = {}
                if content:
                    cid = generate_cid()
                    Comments.objects.create(cid=cid, uid=uid, content=content)
                    result['add'] = {'cid': cid, 'uid': uid, 'content': content}
            elif op == 'delete':
                if cid:
                    result['delete'] = Comments.objects.filter(cid=cid).delete()
    return result


def test(request):
    #     # 注册测试
    #     if regist_account('adfadf222', 'dfadfsa55555', 'kjal4fdj'):
    #         return HttpResponse('ok')
    #     return HttpResponse('error')
    #     #if  dict测试
    #     a = {'n': 1}
    #     if a:
    #         return HttpResponse('true')
    #     else:
    #         return HttpResponse('error')
    #
    #     # 登陆测试
    #     a = longin('for_logintest', 'for_logintest')
    #     if a:
    #         result = '' + a['uid'] + '\n' + a['account'] + '\n' + a['name'] + '\n' + a['account_type']
    #         return HttpResponse(result)
    #     else:
    #         return HttpResponse('error')
    #     UserInfoedit测试
    #     result = edit_UserInfo('100000001', QQ=333)
    #     return HttpResponse(result.items())
    return HttpResponse('result.items()')
