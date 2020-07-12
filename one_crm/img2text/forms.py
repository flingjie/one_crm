# -*- encoding: utf-8 -*-
"""
@File    :   forms
@Time    :   2020/7/12 8:06 下午
@Author  :   Fan Lingjie
@Version :   1.0
@Contact :   fanlingjie@laiye.com
isort:skip_file
"""

import pytesseract
from PIL import Image
from django import forms
from django.apps import apps

from .helpers import extract_name, extract_phone, extract_email

Lead = apps.get_model("leads", "Lead")


class CardForm(forms.Form):
    img = forms.FileField(label="请选择名片")

    def parse_card(self):
        img = Image.open(self.cleaned_data["img"])
        s = pytesseract.image_to_string(img, lang="chi_sim")
        contact = extract_phone(s)
        email = extract_email(s)
        name = extract_name(s)
        lead = Lead(
            name=name,
            contact=contact,
            email=email,
            description=s,
            attachment=self.cleaned_data["img"],
        )
        lead.save()
        return lead.pk
