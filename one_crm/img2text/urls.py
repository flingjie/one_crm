# -*- encoding: utf-8 -*-
"""
@File    :   urls
@Time    :   2020/7/12 8:13 下午
@Author  :   Fan Lingjie
@Version :   1.0
@Contact :   fanlingjie@laiye.com
"""
from django.urls import path

from .views import card_form_view

app_name = "img2text"

urlpatterns = [
    path("", card_form_view, name="card"),
]
