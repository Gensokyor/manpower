from django.db import models


# Create your models here.
class UserAccount(models.Model):
    uid = models.BigIntegerField(max_length=12, unique=True, null=False)
    account = models.CharField(max_length=16, unique=True, null=False)
    pwd = models.CharField(max_length=16, null=False)
    account_type = models.SmallIntegerField(max_length=1, default=3, null=False)
    name = models.CharField(max_length=16, null=False)


class UserInfo(models.Model):
    uid = models.BigIntegerField(max_length=12, unique=True, null=False)
    photo = models.BigIntegerField(max_length=12, null=True)
    tel = models.BigIntegerField(max_length=11, null=True)
    QQ = models.BigIntegerField(max_length=18, null=True)
    mail = models.CharField(max_length=64, null=True)


class Pictures(models.Model):
    pic_id = models.BigIntegerField(max_length=12, unique=True, null=False)
    path = models.CharField(max_length=64, null=False, unique=True)


class Documents(models.Model):
    did = models.BigIntegerField(max_length=16, unique=True, null=False)
    dname = models.CharField(null=False, max_length=16)
    dpath = models.CharField(max_length=64, null=False, unique=True)


class DocSets(models.Model):
    dsid = models.BigIntegerField(max_length=16, unique=True, null=False)
    sequence = models.CharField(max_length=256, null=True)
    type = models.SmallIntegerField(max_length=1, null=False)


class PersonInfo(models.Model):
    uid = models.BigIntegerField(max_length=12, unique=True, null=False)
    college = models.CharField(max_length=16, null=True, )
    major = models.CharField(max_length=16, null=True, )
    degree = models.CharField(max_length=4, null=True, )
    grade = models.SmallIntegerField(max_length=4, null=True)
    intro = models.CharField(max_length=3000, null=True)


class CorpInfo(models.Model):
    uid = models.BigIntegerField(max_length=12, unique=True, null=False)
    license_dsid = models.BigIntegerField(max_length=16, unique=True, null=False)
    intro = models.CharField(max_length=3000, null=True)


class Comments(models.Model):
    cid = models.BigIntegerField(max_length=16, unique=True, null=False)
    uid = models.BigIntegerField(max_length=16, null=False)
    content = models.CharField(max_length=1000, null=False)


class Tasks(models.Model):
    tid = models.BigIntegerField(max_length=16, unique=True, null=False)
    uid = models.BigIntegerField(max_length=16, unique=False, null=False)
    pid = models.BigIntegerField(max_length=16, unique=False, null=False)
    status = models.SmallIntegerField(max_length=1, null=False)
    intro = models.CharField(max_length=3000, null=True)
    solution_dsid = models.BigIntegerField(max_length=16, null=True)


class Projects(models.Model):
    pid = models.BigIntegerField(max_length=16, unique=True, null=False)
    uid = models.BigIntegerField(max_length=16, unique=False, null=False)
    cr_time = models.DateTimeField(null=False, )
    st_time = models.DateTimeField(null=False, )
    end_time = models.DateTimeField(null=False, )
    status = models.SmallIntegerField(max_length=1, null=1)
    title = models.CharField(max_length=18, null=False)
    intro = models.CharField(max_length=3000, null=True)
    pro_dsid = models.BigIntegerField(max_length=16, null=True)
