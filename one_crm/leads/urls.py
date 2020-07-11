# -*- encoding: utf-8 -*-
"""
@File    :   urls.py
@Time    :   2020/7/11 7:50 下午
@Author  :   Fan Lingjie
@Version :   1.0
@Contact :   fanlingjie@laiye.com
"""
from django.urls import path

from .views import (  # isort:skip
    lead_create_view,
    lead_detail_view,
    lead_update_view,
    lead_delete_view,
    lead_list_view,
)

app_name = "leads"

urlpatterns = [
    path("add/", lead_create_view, name="lead-add"),
    path("<int:pk>/", lead_detail_view, name="lead-detail"),
    path("<int:pk>/update/", lead_update_view, name="lead-update"),
    path("<int:pk>/delete/", lead_delete_view, name="lead-delete"),
    path("", lead_list_view, name="lead-list"),
]
