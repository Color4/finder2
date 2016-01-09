import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.template import Context, Template
from django.core.urlresolvers import reverse
from .form import *
from .models import *
from django.conf import settings
import os
from .word_cloud import create_cloud
# captcha
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import JsonResponse


def add(request, a, b):  # /分割
    # a = request.GET['a']
    # b = request.GET['b']
    return HttpResponse('the result is %s' % (a + b))


def add2(request):  # ?访问
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse('the result is %s' % (a + b))


def context(request):
    now = datetime.datetime.now()
    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def home(request):
    return render(request, 'index.html')


def login(request):
    pass


def index(request):
    return HttpResponse('''<a href="{}">Register</a> | <a href="{}">Login in</a>
        '''.format(reverse('registration_register'), reverse('auth_login')))


def contact_author(request):
    if request.method == 'POST':  # 提交请求时才会访问这一段，首次访问页面时不会执行
        form = ContactForm(request.POST)
        if form.is_valid():  # 说明各个字段的输入值都符合要求
            cd = form.cleaned_data  # 只有各个字段都符合要求时才有对应的cleaned_data
            # return HttpResponseRedirect('/thanks/')
            # return render(request, 'form.html', {'form': form, 'subject': cd['subject'], 'email': cd['email']})
            return HttpResponse("OK")
        else:  # 有部分字段不符合要求，会有error相关信息给加到form中去，需要覆盖掉
            pass
    else:  # 首次访问该url时没有post任何表单
        form = ContactForm()  # 第一次生成的form里面内容的格式


        # “首次访问”和“提交的信息不符合要求”时被调用
        return render(request, 'form.html', {'form': form.as_p})


def db(request):
    person = Person.objects.filter(name='小白')
    str_html = ''
    print(person)
    for ii in person:
        str_html += ii.name + ';' + str(ii.age) + '<br/>'

    return HttpResponse(str_html)


def book_list(request):

        # challenge = models.CharField(blank=False, max_length=32)
        # response = models.CharField(blank=False, max_length=32)
        # hashkey = models.CharField(blank=False, max_length=40, unique=True)
        # expiration = models.DateTimeField(blank=False)


    if request.method == 'POST':  # 提交请求时才会访问这一段，首次访问页面时不会执行
        form = BooksForm(request.POST)
        if form.is_valid():  # 说明各个字段的输入值都符合要求
            human=True # 验证码
            cd = form.cleaned_data  # 只有各个字段都符合要求时才有对应的cleaned_data

            bk = Books()
            bk.title = cd['title']
            bk.price = cd['price']
            bk.save()
            # return HttpResponseRedirect('/thanks/')
            # return render(request, 'form.html', {'form': form, 'subject': cd['subject'], 'email': cd['email']})
            book_list = Books.objects.all()
            return render(request, 'books.html', {'form': form.as_p, 'book_list': book_list})
        else:  # 有部分字段不符合要求，会有error相关信息给加到form中去，需要覆盖掉
            return HttpResponse('error')
    else:  # 首次访问该url时没有post任何表单
        form = BooksForm()  # 第一次生成的form里面内容的格式

        book_list = Books.objects.all()

        # “首次访问”和“提交的信息不符合要求”时被调用
        return render(request, 'books.html', {'form': form.as_p, 'book_list': book_list})

def word_cloud(request):
    if request.method == 'POST':
         form = WordCloudForm(request.POST, request.FILES)
         if form.is_valid():
            # return HttpResponse(request.FILES['file'].read())
            # os.path.join(BASE_DIR, "static")
            out_path = os.path.join(settings.STATIC_ROOT, 'out.jpg')
            create_cloud(request.FILES['word'], request.FILES['img'], out_path)
            export = {
                'success':True,
                'out_file': 'out.jpg'
            }
            return render(request, 'word_cloud.html', export)
         else:
             return HttpResponse('fail')
    else:
        form = WordCloudForm()
        return render(request, 'word_cloud.html', {'form':form})

def user_profile(request):
    return render(request, 'user_profile.html')

def ajax_val(request):
    if  request.is_ajax():
        cs = CaptchaStore.objects.filter(response=request.GET['response'],
                                     hashkey=request.GET['hashkey'])
        if cs:
            json_data={'status':1}
        else:
            json_data = {'status':0}
        return JsonResponse(json_data)
    else:
        # raise Http404
        json_data = {'status':0}
        return JsonResponse(json_data)

def some_view(request):
    if request.POST:
        form = CaptchaTestForm(request.POST)

        # Validate the form: the captcha field will automatically
        # check the input
        if form.is_valid():
            human = True
            return HttpResponse(form.clean()) # 这里没有建立模型，如果成功则直接打印
        else:
            return HttpResponse('validate error')
    else:
        form = CaptchaTestForm()

    return render(request,'template.html',locals())


def person(request):
    if request.POST:
        form = PersonForm(request.POST)

        if form.is_valid():
            p = form.save()
            return HttpResponse(request, 'success')
        else:
            return HttpResponse(request, 'hahaha')
    else:
        form = PersonForm()
        person_list = Person.objects.all()
        # school_list = person_list.School_set.all()
        return render(request, 'person.html', locals())
