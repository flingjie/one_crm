from django.db import models
from django.urls import reverse

from django.db.models import (  # isort:skip
    CharField,
    EmailField,
    TextField,
    FileField,
    DateTimeField,
)


class Lead(models.Model):
    name = CharField("名字", max_length=255)
    title = CharField("职称", max_length=255, blank=True)
    contact = CharField("联系方式", max_length=255, blank=True)
    email = EmailField("邮箱", blank=True)
    description = TextField("描述", blank=True)
    attachment = FileField("附件", upload_to="upload", blank=True)
    create_time = DateTimeField("创建时间", auto_now_add=True)
    update_time = DateTimeField("上次更新时间", auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("leads:lead-detail", kwargs={"pk": self.pk})
