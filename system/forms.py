# -*- coding: utf-8 -*-
from django import forms

from system.models import Feedback

class FeedBackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        exclude=[]
