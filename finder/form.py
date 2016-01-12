# coding:utf8
from django import forms
from captcha.fields import CaptchaField
from django.forms import ModelForm

from finder.models import Person


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=10, label='主题',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))  # 设置最大长度为10
    email = forms.EmailField(required=True, label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))  # 非必要字段
    message = forms.CharField(widget=forms.Textarea, label='信息')  # 指定form中组件的类型
    # message.label_tag(attrs={'hah':'hahah'})
    # 自定义校验规则，该方法在校验时被系统自动调用，次序在“字段约束”之后
    def clean_message(self):
        message = self.cleaned_data['message']  # 能到此处说明数据符合“字段约束”要求
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("单词个数低于4个!")
        return message


class CommentForm(forms.Form):
    name = forms.CharField(max_length=10, label='name')
    url = forms.URLField(max_length=100, label='url')
    comment = forms.CharField(max_length=100, label='comment')


class BooksForm(forms.Form):
    title = forms.CharField(max_length=100, label='title')
    price = forms.FloatField(max_value=100, label='price')
    # captcha = CaptchaField()

    def clean_message(self):
        message = self.cleaned_data['price']  # 能到此处说明数据符合“字段约束”要求
        num_words = int(message)
        if num_words < 4:
            raise forms.ValidationError("单词个数低于4个!")
        return message


class WordCloudForm(forms.Form):
    title = forms.CharField(max_length=50)
    # file = forms.FileField()
    word = forms.FileField()
    img = forms.FileField()


class CaptchaTestForm(forms.Form):
    title = forms.CharField(max_length=100, label='title')
    price = forms.FloatField(max_value=100, label='price')  # 这里是我们需要的字段，以title和price为例
    captcha = CaptchaField()  # 为生成的验证码图片，以及输入框


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # def __init__(self, *args, **kwargs):
        #     # user = kwargs.pop('user','')
        #     super(PersonForm, self).__init__(*args, **kwargs)
        #     self.fields['school']=forms.ModelChoiceField(queryset=School.objects.all())


class TestForm(forms.Form):
    title = forms.CharField(max_length=10,
                            label='标题',
                            help_text='100 characters max.',
                            widget=forms.TextInput(attrs={'placeholder': 'title', 'class': 'form-control'}))

    content = forms.CharField(max_length=110,
                              label='内容',
                              error_messages={'required': 'Please enter your name'},
                              widget=forms.TextInput(attrs={'placeholder': 'content', 'class': 'form-control'}))

    email = forms.EmailField(required=True,
                             error_messages={'required': u'邮箱不能为空', 'invalid': u'请输入正确的邮箱'},
                             widget=forms.EmailInput(attrs={'placeholder': 'email', 'class': 'form-control'}))
