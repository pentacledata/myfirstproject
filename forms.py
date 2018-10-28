from django import forms
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet
from django.forms.fields import DateField
from django.core.validators import RegexValidator
from pentacledata.models import *
import datetime
from django.utils import timezone


class Department(forms.Form):

    department_name = forms.CharField(label='Department Name',
                                      required=True,
                                      widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Departmet Name'}),
                                      max_length=60)

    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,
                                                               'cols': 30}))

    class Meta:
        model = Department

    status = forms.BooleanField()


class Doctor(forms.Form):

    first_name = forms.CharField(label='First Name', required=True,
                                 widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'First Name'}),
                                 max_length=60)
    last_name = forms.CharField(label='Last Name', required=True,
                                widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Last Name'}),
                                max_length=60)

    email = forms.CharField(label='Email Address', required=True,
                            widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Email Address'}),
                            max_length=60)

    password = forms.CharField(label='Password', required=True,
                               widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Password'}),
                               max_length=60)

    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    short_biography = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    education = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 30}))
    sex = forms.BooleanField()
    status = forms.BooleanField()


class PatientDetails(forms.Form):

    patient_name = forms.CharField(label='Patient Name',
                                      required=True,
                                      widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Patient Name'}),
                                      max_length=60)

    mobile = forms.CharField(label='Mobile Number',
                                      required=True,
                                      widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Mobile Number'}),
                                      max_length=60)
    
    class DocumentDetails(forms.Form):

    patient_name = forms.CharField(label='Patient Name',
                                      required=True,
                                      widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Patient Name'}),
                                      max_length=60)

    mobile = forms.CharField(label='Mobile Number',
                                      required=True,
                                      widget=forms.TextInput(
                                         attrs={
                                             'size': '30',
                                             'placeholder':
                                                 'Mobile Number'}),
                                      max_length=60)

