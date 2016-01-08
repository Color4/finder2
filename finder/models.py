from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    def __str__ (self):#在Python2中用__unicode__替换__str__
        return self.title




class Books(models.Model):
    title = models.CharField('标题', max_length=200)
    price = models.FloatField('价格')

class Province(models.Model):
    name = models.CharField('省份', max_length = 10)
    post = models.CharField('邮编', max_length = 10)
    def __str__ (self):#在Python2中用__unicode__替换__str__
        return self.name

# class School_Type(models.Model):
#     school_type = models.CharField('学校类别')

class School(models.Model):
    id = models.IntegerField('学校编号', primary_key=True)
    name = models.CharField('学校名称', max_length=200)
    address = models.CharField('学校地址', max_length=200)

    def __str__ (self):#在Python2中用__unicode__替换__str__
        return self.name




class Person(models.Model):
    name = models.CharField('姓名', max_length=50)
    age = models.IntegerField('年龄')
    address = models.CharField('地址', max_length=100)
    email = models.EmailField('电子邮件')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete = models.CASCADE)
