from django import forms
from .models import Guest
from .models import Contractor
from .models import Employee
from .models import GuestVisit
from .models import inventory
from .models import GuestFlag
from .models import EmployeeFlag
from .models import ContractorFlag
from .models import Nationality
from .models import VisaType
from .models import Document
from .models import UserAccessinventory
#from .models import GuestVisit
from .models import Salutation

import datetime

#from django.contrib.auth.models import User, Group

#from django.contrib.auth.models import User

#from django.forms import ModelChoiceField, CheckboxInput, HiddenInput

from django.contrib.auth import get_user_model


"""
from datetime import date
from django.forms import widgets

class DateSelectorWidget(widgets.MultiWidget):
    def __init__(self, attrs=None):
        # create choices for days, months, years
        # example below, the rest snipped for brevity.
        years = [(year, year) for year in (2011, 2012, 2013)]
        _widgets = (
            widgets.Select(attrs=attrs, choices=days),
            widgets.Select(attrs=attrs, choices=months),
            widgets.Select(attrs=attrs, choices=years),
        )
        super(DateSelectorWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.day, value.month, value.year]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        datelist = [
            widget.value_from_datadict(data, files, name + '_%s' % i)
            for i, widget in enumerate(self.widgets)]
        try:
            D = date(
                day=int(datelist[0]),
                month=int(datelist[1]),
                year=int(datelist[2]),
            )
        except ValueError:
            return ''
        else:
            return str(D)

"""


#from functools import partial
#DateInput = partial(forms.DateInput, {'class': 'datepicker'})

#from bootstrap3_datetime.widgets import DateTimePicker
#from django import forms


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
#    age = forms.IntegerField(max_value=100)
    accept_terms = forms.BooleanField()

    class Meta:
        model = get_user_model() # use this function for swapping user model

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.accept_terms = self.cleaned_data['accept_terms']
        user.save()



"""

class MyForm(Form):

    # the default format is %Y-%m-%d
    date_available = forms.DateField(
        widget=forms.widgets.DateInput(format="%m/%d/%Y"))

"""


class GuestVisitForm(forms.ModelForm):
    arrival_date = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(format="%Y-%m-%d %H:%M:%S"))
    class Meta:
        model = GuestVisit
        fields = ['arrival_date']

#    def __init__(self, *arg, **kwargs):
#        super(GuestVisit, self).__init__(*arg, **kwargs)
#        self.fields['arrival_date'] = DateTimeWithUsecsField()

    def __init__(self, *args, **kwargs):
        super(GuestVisitForm, self).__init__(*args, **kwargs)
        self.fields['arrival_date'] = DateTimeWithUsecsField()


class DateTimeWithUsecsField(forms.DateTimeField):
    def clean(self, value):
        if value and '.' in value:
            value, usecs = value.rsplit('.', 1)
            usecs += '0'*(6-len(usecs)) # right pad with zeros if necessary
            try:
                usecs = int(usecs)
            except ValueError:
                raise ValidationError('Microseconds must be an integer')
        else:
            usecs = 0
        cleaned_value = super(DateTimeWithUsecsField, self).clean(value)
        if cleaned_value:
            cleaned_value = cleaned_value.replace(microsecond=usecs)
        return cleaned_value

#    arrival_date = forms.DateField(widget=DateInput())
#    departure_date = forms.DateField(widget=DateInput())

#    dateTimeOptions = {
#        'format': 'dd-mm-yyyy HH:ii P',
#        'format': 'dd-M-yyyy hh:ii',
#        'autoclose': True,
#        'showMeridian' : True
#     }

    #arrival_date = forms.DateField(label='buy date', input_formats=['%Y-%m-%d'], initial=datetime.date.today())

#    dateTimeOptions = forms.DateTimeField(
#            required=False,
#            widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
#                                       "pickSeconds": False}))


#    arrival_date = forms.DateTimeField(
#        required=False,
#        widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
#                                       "pickSeconds": False}))

#        fields = "__all__"

#        self.fields['departure_date'].required = False

#        widgets = {
#            'arrival_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
#            }


#        widgets = {
#            'arrival_date': DateWidget(attrs = {'id':'id_dateTimeField'}, bootstrap_version=3, usel10n=True)
#            }

#        widgets = {
#            'arrival_date': DateInput(),
#        }
#        widgets = {
#            'arrival_date': forms.DateInput(attrs={'class':'datepicker'}),
#        }

#        widgets = {
#            'arrival_date': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
#                                       "pickSeconds": False}) }

#        fields = '__all__'
#        exclude = ['author','arrival_date', 'inventory', 'guestname', 'departure_date']
        exclude = ['author', 'inventory', 'guestname']


class SubUserForm(forms.ModelForm):
    class Meta:
        model = UserAccessinventory
        fields = '__all__'
        exclude = ['created_date', 'inventory']


class UserAccessinventoryForm(forms.ModelForm):

    class Meta:
        model = UserAccessinventory
        fields = '__all__'
        exclude = ['author', 'inventory', 'created_date', 'visit_date']

    def __init__(self, *args, **kwargs):
    #    super(UserAccessinventoryForm, self).__init__(*args, **kwargs)
        pass
        # there's a `fields` property now


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('docfile', 'title', 'description' )
        exclude = ['author', 'updated_date']

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = False
#        self.fields['inventorytype'].required = False
        #self.fields['office_email'].required = False
        #self.fields['office_cell'].required = False


class inventoryForm(forms.ModelForm):
    class Meta:
        model = inventory
        exclude = ['author', 'created_date', 'published_date']

    def __init__(self, *args, **kwargs):
        super(inventoryForm, self).__init__(*args, **kwargs)
        self.fields['comments'].required = False
#        self.fields['inventorytype'].required = False
        self.fields['office_email'].required = False
        self.fields['office_cell'].required = False

class EmployeeFlagForm(forms.ModelForm):
    class Meta:
        model = EmployeeFlag
        exclude = ['author', 'created_date', 'flagstatus', ]
        fields = ['comments', 'offense']

    def __init__(self, *args, **kwargs):
        super(EmployeeFlagForm, self).__init__(*args, **kwargs)
        self.fields['comments'].required = False

class ContractorFlagForm(forms.ModelForm):
    class Meta:
        model = ContractorFlag
        exclude = ['author', 'created_date', 'flagstatus']
        fields = ['comments', 'offense']

    def __init__(self, *args, **kwargs):
        super(ContractorFlagForm, self).__init__(*args, **kwargs)
        self.fields['comments'].required = False

class GuestFlagForm(forms.ModelForm):
    class Meta:
        model = GuestFlag
        exclude = ['author', 'created_date', 'flagstatus',]
        fields = ['comments', 'offense']

    def __init__(self, *args, **kwargs):
        super(GuestFlagForm, self).__init__(*args, **kwargs)
        self.fields['comments'].required = False

class FormattedDateField(forms.DateField):
    widget = forms.DateInput(format='%m/%d/%Y')

    def __init__(self, *args, **kwargs):
        super(FormattedDateField, self).__init__(*args, **kwargs)
        self.input_formats = ('%m/%d/%Y',)


class GuestForm(forms.ModelForm):
#    SAidentityNo = forms.CharField(max_length=13, min_length=13, required=False)
#    salutation = forms.ModelChoiceField(queryset = Salutation.objects.all(),
#        required=False,
#        help_text="Select salutation" )

    nationality = forms.ModelChoiceField(queryset = Nationality.objects.all(),
        required=False,
        help_text="Select nationality if not South African",
        empty_label="Select nationality"
         )
    visatype = forms.ModelChoiceField(queryset = VisaType.objects.all(),
        required=False,
        help_text="Select visa type if available",
        empty_label="Select visa type "
         )

    class Meta:
        model = Guest
        widgets = {
            'show_name' : forms.TextInput(attrs = {'placeholder': 'Nickname'}),
            'firstname' : forms.TextInput(attrs = {'placeholder': 'Firstname'}),
            'surname' : forms.TextInput(attrs = {'placeholder': 'Surname'}),
            'cellPhoneNumber' : forms.TextInput(attrs = {'placeholder': 'cellPhoneNumber'}),
            'emailAddress' : forms.TextInput(attrs = {'placeholder': 'emailAddress'}),
            'SAidentityNo' : forms.TextInput(attrs = {'placeholder': 'SAidentityNo'}),
            'PassportNo' : forms.TextInput(attrs = {'placeholder': 'PassportNo'}),
                }
#        created_date = FormattedDateField()
        exclude = ['author', 'inventory', 'created_date', 'published_date', 'flagstatus']
        fields = ['show_name', 'firstname',
        'surname', 'cellPhoneNumber', 'emailAddress', 'SAidentityNo',
             'nationality', 'visatype', 'PassportNo']

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        self.fields['SAidentityNo'].required = False
        # there's a `fields` property now
        self.fields['nationality'].required = False
        self.fields['visatype'].required = False
        self.fields['show_name'].required = True
        self.fields['cellPhoneNumber'].required = False
        self.fields['emailAddress'].required = False
        self.fields['surname'].required = True
        self.fields['firstname'].required = False
#        self.fields['mugshot'].required = False
        self.fields['PassportNo'].required = False
        self.fields['show_name'].label = "Nickname"
        self.fields['SAidentityNo'].label = "Identity Number(SA)"



class ContractorForm(forms.ModelForm):

    class Meta:
        model = Contractor
        fields = '__all__'
        exclude = ['author', 'inventory', 'created_date', 'visit_date']

    def __init__(self, *args, **kwargs):
        super(ContractorForm, self).__init__(*args, **kwargs)
        pass
        # there's a `fields` property now
#        self.fields['SAidentityNo'].required = False
#        self.fields['nationality'].required = False
#        self.fields['visatype'].required = False


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['author', 'inventory', 'created_date', 'visit_date']

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        pass


#class VisitForm(forms.ModelForm):

#    class Meta:
#        model = GuestVisit
#        fields = '__all__'
#        exclude = ['author', 'inventory', 'created_date', 'visit_date']

#    def __init__(self, *args, **kwargs):
#        super(VisitForm, self).__init__(*args, **kwargs)
#        pass
