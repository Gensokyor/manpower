from manpowermanage.models import *
from django.db.models import Avg, Max, Min, Count, Sum


# 合法性检查(include 重复性检查)
def lencontent_check(checktype: str, target: str, value):
    checkresult = False
    if checktype == 'str':
        if not isinstance(value, str):
            value = str(value)
        if target == 'account':
            # print('account')
            print(len(value))
            if not len(value) < 8 or len(value) > 16:
                for i in value:
                    # print(i)
                    checkresult = (i == '_' or i.isdigit() or i.isalpha())
                    if not checkresult:
                        break
                    # print(checkresult)

            checkresult = checkresult and Repeatability_check('str', 'account', value)
        if target == 'pwd':
            # print('pwd')
            if not len(value) < 8 or len(value) > 16:
                for i in value:
                    checkresult = (i == '_' or i.isdigit() or i.isalpha())
        if target=='name':
            # print('name')
            if not len(value) < 8 or len(value) > 16:
                checkresult=True
    elif checktype == 'int':
        pass
    # print(checkresult)
    return checkresult


# 重复性检查
def Repeatability_check(checktype: str, target: str, value):
    checkresult = False
    if checktype == 'int':
        if not isinstance(value, int):
            value = int(value)
        if target == 'uid':
            if len(UserAccount.objects.filter(uid=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'pid':
            if len(Projects.objects.filter(pid=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'did':
            if len(Documents.objects.filter(did=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'dsid':
            if len(DocSets.objects.filter(dsid=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'pic_id':
            if len(Pictures.objects.filter(pic_id=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'tid':
            if len(Tasks.objects.filter(tid=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'cid':
            if len(Comments.objects.filter(cid=value)) == 0:
                checkresult = True
            else:
                checkresult = False
    elif checktype == 'str':
        if not isinstance(value, str):
            value = str(value)
        if target == 'account':
            if len(UserAccount.objects.filter(account=value)) == 0:
                checkresult = True
            else:
                checkresult = False
        elif target == 'dpath':
            if len(Documents.objects.filter(dpath=value)) == 0:
                checkresult = True
            else:
                checkresult = False
    return checkresult


def generate_uid():
    if len(UserAccount.objects.all()) == 0:
        return 100000000
    uid = UserAccount.objects.aggregate(Max('uid')) + 1
    return uid


def generate_pid():
    if len(Projects.objects.all()) == 0:
        return 1
    pid = Projects.objects.aggregate(Max('uid')) + 1
    return pid


def generate_tid():
    if len(Tasks.objects.all()) == 0:
        return 1
    tid = Tasks.objects.aggregate(Max('uid')) + 1
    return tid


def generate_picid():
    if len(Pictures.objects.all()) == 0:
        return 1
    pic_id = Pictures.objects.aggregate(Max('uid')) + 1
    return pic_id


def generate_cid():
    if len(Comments.objects.all()) == 0:
        return 1
    cid = Comments.objects.aggregate(Max('uid')) + 1
    return cid


def generate_did():
    if len(Documents.objects.all()) == 0:
        return 1
    did = Documents.objects.aggregate(Max('uid')) + 1
    return did


def generate_dsid():
    if len(DocSets.objects.all()) == 0:
        return 1
    dsid = DocSets.objects.aggregate(Max('uid')) + 1
    return dsid


def Idgenerator(idtype: str):
    new_id = None
    if idtype == 'uid':
        new_id = generate_uid()
    elif idtype == 'pic_id':
        new_id = generate_picid()
    elif idtype == 'cid':
        new_id = generate_cid()
    elif idtype == 'did':
        new_id = generate_did()
    elif idtype == 'dsid':
        new_id = generate_dsid()
    elif idtype == 'tid':
        new_id = generate_tid()
    elif idtype == 'pid':
        new_id = generate_pid()
    return new_id
