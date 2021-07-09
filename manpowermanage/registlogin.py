from manpowermanage.models import *
from manpowermanage.idgenerator import *
from django.http import HttpResponse
import datetime
import os
from manpower import settings


def regist_account(newaccount: str, newpwd: str, name: str, account_type=3):
    if lencontent_check('str', 'account', newaccount) and lencontent_check('str', 'pwd', newpwd) and lencontent_check(
            'str', 'name', name):
        uid = Idgenerator('uid')
        result = UserAccount.objects.create(uid=uid, account=newaccount, pwd=newpwd, account_type=account_type,
                                            name=name)
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
                license_dsid = generate_dsid()
                CorpInfo.objects.create(uid=uid, license_dsid=license_dsid)
            target = CorpInfo.objects.filter(uid=uid).first()
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


def edit_Projects(uid, op: str, pid=None, cr_time=None, st_time=None, end_time=None, status=None, title=None,
                  intro=None, pro_dsid=None):
    result = {'op': op}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if True:
    # if isinstance(uid, int):
        if op == 'new':
            pid = generate_pid()
            pro_dsid = generate_dsid()
            if not cr_time:
                cr_time = datetime.datetime.now()
            new_project = Projects.objects.create(uid=uid, pid=pid, cr_time=cr_time, st_time=st_time, end_time=end_time,
                                                  status=1, title=title, intro=intro, pro_dsid=pro_dsid)
            new_project_info = {}
            new_project_info['uid'] = new_project.uid
            new_project_info['pid'] = new_project.pid
            new_project_info['status'] = new_project.status
            new_project_info['title'] = new_project.title
            new_project_info['cr_time'] = new_project.cr_time
            new_project_info['st_time'] = new_project.st_time
            new_project_info['end_time'] = new_project.end_time
            new_project_info['intro'] = new_project.intro
            new_project_info['pro_dsid'] = new_project.pro_dsid
            result['new'] = new_project_info
        elif op == 'edit':
            edited_projects = {}
            if pid:
                target = Projects.objects.filter(pid=pid)
                if target:
                    target = target.first()
                    if True:
                    # if uid == target.uid:
                        if status:
                            target.status = status
                            target.save()
                        if title:
                            target.title = title
                            target.save()
                        if st_time:
                            target.st_time = st_time
                            target.save()
                        if end_time:
                            target.end_time = end_time
                            target.save()
                        if intro:
                            target.intro = intro
                            target.save()
                        if pro_dsid:
                            target.pro_dsid = pro_dsid
                            target.save()
                        edited_projects['pid'] = target.pid
                        edited_projects['uid'] = target.uid
                        edited_projects['cr_time'] = target.cr_time
                        edited_projects['st_time'] = target.st_time
                        edited_projects['end_time'] = target.end_time
                        edited_projects['status'] = target.status
                        edited_projects['title'] = target.title
                        edited_projects['intro'] = target.intro
                        edited_projects['pro_dsid'] = target.pro_dsid
            result['edit'] = edited_projects
        elif op == 'delete':
            deleted_p = None
            if pid:
                target = Projects.objects.filter(pid=pid)
                if target:
                    target = target.first()
                    if uid == target.uid:
                        deleted_p = target.delete()
                        print(type(deleted_p))
            result['delete'] = deleted_p
        elif op == 'query':
            query = []
            if uid:
                a = Projects.objects.filter(uid=uid)
                for i in a:
                    query.append(
                        {'pid': i.pid, 'uid': i.uid, 'cr_time': i.cr_time, 'st_time': i.st_time, 'end_time': i.end_time,
                         'status': i.status, 'title': i.title, 'intro': i.intro, 'pro_dsid': i.pro_dsid})
            result[op] = query

    return result


def edit_Tasks(uid, op: str, pid, tid=None, status=None, intro=None, solution_dsid=None):
    result = {'op': op}
    if not isinstance(uid, int):
        if isinstance(uid, str) and uid.isdigit():
            uid = int(uid)
    if isinstance(uid, int):
        if op == 'new':
            proj = Projects.objects.filter(pid=pid)
            a = {}
            if proj and (not Tasks.objects.filter(pid=pid, uid=uid)):
                tid = generate_tid()
                solution_dsid = generate_dsid()
                new_task = Tasks.objects.create(tid=tid, status=1, uid=uid, pid=pid, solution_dsid=solution_dsid)
                a = {'tid': new_task.tid, 'uid': new_task.uid, 'pid': new_task.pid,
                     'solution_dsid': new_task.solution_dsid, 'status': new_task.status, 'intro': new_task.intro}
            result[op] = a
        elif op == 'edit':
            if tid:
                target = Tasks.objects.filter(tid=tid)
            else:
                target = Tasks.objects.filter(uid=uid, pid=pid)
            a = {}
            if target:
                target = target.first()
                if status:
                    target.status = status
                    target.save()
                    a['status'] = target.status
                if intro:
                    target.intro = intro
                    target.save()
                    a['intro'] = target.intro
            result[op] = a
        elif op == 'delete':
            if tid:
                target = Tasks.objects.filter(tid=tid)
            else:
                target = Tasks.objects.filter(uid=uid, pid=pid)
            result[op] = None
            if target:
                target = target.first()
                a = target.delete()
                result[op] = a
        elif op == 'query':
            query = []
            if uid:
                a = Tasks.objects.filter(uid=uid)
                for i in a:
                    query.append(
                        {'pid': i.pid, 'uid': i.uid, 'tid': i.tid,
                         'status': i.status, 'intro': i.intro, 'solution_dsid': i.solution_dsid})
            result[op] = query

    return result


def edit_Documents(op: str, did=None, dpath=None, dname=None):
    result = {'op': op}
    if op == 'new':
        result[op] = None
        did = generate_did()
        if dname and dpath:
            new_doc = Documents.objects.create(did=did, dname=dname, dpath=dpath)
            a = {'did': new_doc.did, 'dname': new_doc.dname, 'dpath': new_doc.dpath}
            result[op] = a
    elif op == 'get':
        result[op] = None
        if did:
            target = Documents.objects.filter(did=did)
            if target:
                target = target.first()
                a = {'did': target.did, 'dname': target.dname, 'dpath': target.dpath}
                result[op] = a
    elif op == 'delete':
        result[op] = None
        if did:
            target = Documents.objects.filter(did=did)
            if target:
                a = target.delete()
                result[op] = a
    elif op == 'edit':  # 不建议使用
        result[op] = None
        if did:
            a = {}
            target = Documents.objects.filter(did=did)
            if target:
                if dname:
                    target.dname = dname
                    target.save()
                    a['dname'] = target.dname
                if dpath:
                    target.dpath = dpath
                    target.save()
                    a['dpath'] = target.dpath
            result[op] = a
    return result


def edit_DocSets(op, dsid, sequence=None, type=None, dids=None):
    result = {'op': op}
    if op == 'new':
        new_docsets = {}
        if not DocSets.objects.filter(dsid=dsid):
            target = DocSets.objects.create(dsid=dsid, type=type)
            new_docsets['dsid'] = target.dsid
            new_docsets['type'] = target.type
            if isinstance(sequence, str):
                docs = sequence.split('|')
                dids = ''
                for i in docs:
                    if i.isdigit():
                        dids += i
                target.sequence = dids
                target.save()
                new_docsets['sequence'] = target.sequence
            if isinstance(dids, list):
                dids = ''
                for i in dids:
                    if i.isdigit():
                        dids += i
                target.sequence = dids
                target.save()
                new_docsets['sequence'] = target.sequence
        result[op] = new_docsets
    elif op == 'edit':
        new_docsets = {}
        target = DocSets.objects.filter(dsid=dsid)
        if target:
            target = target.first()
            if isinstance(sequence, str):
                docs = sequence.split('|')
                ds = ''
                for i in docs:
                    if i.isdigit():
                        ds += i
                        ds += '|'
                target.sequence = ds
                target.save()
                new_docsets['sequence'] = target.sequence
            if isinstance(dids, list):
                ds = ''
                for i in dids:
                    if i.isdigit():
                        ds += i
                        ds += '|'
                target.sequence = ds
                target.save()
                new_docsets['sequence'] = target.sequence
            if type:  # 尽量避免使用
                target.type = type
                target.save()
                new_docsets['type'] = target.type
        result[op] = new_docsets
    elif op == 'delete':
        target = DocSets.objects.filter(dsid=dsid)
        a = None
        if target:
            target = target.first()
            a = target.delete()
        result[op] = a
    elif op == 'get':
        target = DocSets.objects.filter(dsid=dsid)
        ds_info = None
        if target:
            target = target.first()
            ds_info = {}
            ds_info['dsid'] = target.dsid
            ds_info['sequence'] = target.sequence
            ds_info['type'] = target.type
        result[op] = ds_info
    return result


def get_recommend():
    # 项目
    result = {}
    a = Projects.objects.all()
    result['pro'] = [a[1], a[2], a[3], a[4]]
    b = CorpInfo.objects.all()
    uids = [int(b[1].uid), int(b[2].uid), int(b[3].uid), int(b[4].uid), int(b[5].uid), int(b[6].uid), int(b[7].uid),
            int(b[8].uid), int(b[9].uid), int(b[10].uid)]
    results = []
    for i in uids:
        corpname = UserAccount.objects.filter(uid=i).first().name
        intro = CorpInfo.objects.filter(uid=i).first().intro
        results.append({'uid': i, 'name': corpname, 'intro': intro})


    return results


def change_pwd(uid, oldpwd, newpwd):
    result = False
    target = UserAccount.objects.filter(uid=uid, pwd=oldpwd)
    if target:
        target = target.first()
        target.pwd = newpwd
        target.save()
        result = True
    return result


# def save_pic(request):
#     if request.method == 'POST':
#         # picfile = request.FILES['picfile']
#         pics=None
#         pics= request.FILES['picfile']
#         for pic in pics
#         pic_file_no=None
#         pic_file_no=generate_picid()
#         pic_path = os.path.join(settings.IMG_ROOT, str(pic_file_no))
#         with open(pic_path, 'wb') as f:
#             for pic_Part in pic.chunks():
#                 f.write(pic_Part)
#         return {'pic_id':pic_file_no,'path':pic_path}
#     else:
#         return None


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
    # result = edit_Projects(uid=100000001, op='new', intro='22222')
    # result = edit_Projects(uid=100000001, pid=5, op='edit', intro='3333')
    # result = edit_Projects(uid=100000001, pid=7, op='delete', intro='3333')
    # 测试Tasks
    # result=edit_Tasks(uid=100000001,op='new',pid=1,)
    # result=edit_Tasks(uid=100000001,op='edit',pid=1,intro='3333')
    # result = edit_Tasks(uid=100000001, op='delete', pid=1, intro='3333')
    # result = edit_DocSets(op='new', type='1',dsid=1)
    # result = edit_DocSets(op='edit',dsid=1,sequence='123|51|21')
    # result = edit_DocSets(op='edit', dsid=1,dids=['555','321','555'])
    result = edit_DocSets(op='delete', dsid=1)
    return HttpResponse(result[result['op']])
