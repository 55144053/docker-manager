""" 
@Time    : 2018/7/17 19:36
@Author  : 郭家兴
@Email   : 302802003@qq.com
@File    : client_forms.py
@Desc    :
"""
from wtforms import StringField, IntegerField, Form, FormField, BooleanField
from wtforms.validators import DataRequired, length, Email, Regexp, ValidationError

from app.validators.base import BaseForm


class ClientForm(BaseForm):
    host = StringField(validators=[DataRequired(message='不许为空'),length(min=5,max=32)])

class ListForm(BaseForm):
    host = StringField(validators=[DataRequired(message='不许为空'),length(min=5,max=32)])
    page = IntegerField(default=1)
    search = StringField()

class ImageForm(BaseForm):
    host = StringField(validators=[DataRequired(message='不许为空'),length(min=5,max=32)])
    image = StringField(validators=[DataRequired(message='不许为空')])
    command = StringField()
    name = StringField()
    links = StringField()
    ports = StringField()
    restart = BooleanField(default=True)
    volumes = StringField()
