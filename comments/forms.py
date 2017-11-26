from django import forms
from .models import Comment

#如果表单对应有一个数据库的模型，那么使用ModelForm类会简单很多
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment#表明这个表单对应的数据库模型是Comment类
        fields = ['name','email','url','text']#制定表单需要要显示的字段
