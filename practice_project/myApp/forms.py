from dataclasses import field, fields

from django import forms

from myApp import models


class studentForm (forms.ModelForm):
    class Meta:
        model = models.students
        fields = '__all__'

