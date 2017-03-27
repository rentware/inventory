# encoding: utf-8
#from django.contrib.auth.models import User
from django.db import models
#from django.utils.timezone import now
#from django.db import models
from django.utils import timezone
from stdimage import StdImageField

from django.db.models import permalink

import datetime




class Salutation(models.Model):
    salutation = models.CharField(max_length=30)

    def __str__(self):
        return self.salutation


class UserGroup(models.Model):
    author = models.ForeignKey('auth.User')
    group = models.CharField(max_length=200)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.group

    class Meta:
        ordering = ('group',)


class UserPerm(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    #user_groups = models.ForeignKey(UserGroup, default="")
    user_groups = models.ManyToManyField(UserGroup, default="")
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class VisaType(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Nationality(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class inventoryType(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class ContractorType(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class EmployeeType(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class EntityType(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class inventory(models.Model):
    inventorytype = models.ForeignKey(inventoryType, default="")
    author = models.ForeignKey('auth.User')
    entity_type = models.ForeignKey(EntityType, default="")
    trading_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    street_address = models.CharField(max_length=200, default="")
    suburb = models.CharField(max_length=200, default="")
    province = models.CharField(max_length=200, default="")
    show_name = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=200, default="")
    EntityRegistrationNumber = models.CharField(max_length=200, default="")
    OfficePhone = models.CharField(max_length=200, default="")
    office_cell = models.CharField(max_length=200)
    office_email = models.CharField(max_length=200)
    comments = models.TextField()

    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.show_name

    def __unicode__(self):
        return '%s' % self.show_name


class UserAccessinventory(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default="notset")
    inventory = models.ForeignKey(inventory)
    users_inventory = models.ForeignKey('auth.User') #settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Employee(models.Model):
    employeetype = models.ForeignKey(EmployeeType, default="")
    inventory = models.ForeignKey(inventory, default="")
  #  author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    show_name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()

    flagstatus = models.BooleanField(default=0)

    firstname = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")

    car_registration = models.CharField(max_length=200, default="")

    created_date = models.DateTimeField(
            default=timezone.now)
    visit_date = models.DateTimeField(
            blank=True, null=True)

    def visit_date(self):
        self.visit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.show_name


class Contractor(models.Model):
    contractortype = models.ForeignKey(ContractorType, default="")
    inventory = models.ForeignKey(inventory, default="")
  #  author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    show_name = models.CharField(max_length=200)
    cell = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    comments = models.TextField()

    firstname = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")

    car_registration = models.CharField(max_length=20, default="")

    flagstatus = models.BooleanField(default=0)

    created_date = models.DateTimeField(
            default=timezone.now)
    visit_date = models.DateTimeField(
            blank=True, null=True)

    def visit_date(self):
        self.visit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.show_name


class Guest(models.Model):
    inventory = models.ForeignKey(inventory, null=True)
    visatype = models.ForeignKey(VisaType, null=True, default="")
    isSouthAfrican = models.BooleanField(default=0)
    SAidentityNo = models.CharField(max_length=13, blank=True, null=True)
    PassportNo = models.CharField(max_length=200)
    nationality = models.ForeignKey(Nationality, null=True, default="")
    user = models.ForeignKey('auth.User', null=True)
    salutation = models.ForeignKey(Salutation, null=True, default="")
    show_name = models.CharField(max_length=50, default="")
    firstname = models.CharField(max_length=50, default="")
    surname = models.CharField(max_length=200, default="")
    cellPhoneNumber = models.CharField(max_length=20, default="")
    emailAddress = models.EmailField(null=True, default="")
    car_registration = models.CharField(max_length=20, default="")

#    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    flagstatus = models.BooleanField(default=0)

    comments = models.TextField(null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    visit_date = models.DateTimeField(
            blank=True, null=True)

    def visit_date(self):
        self.visit_date = timezone.now()
        self.save()

    def __str__(self):
        return self.show_name


class DocummentType(models.Model):
    author = models.ForeignKey('auth.User')
    type = models.CharField(max_length=20)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.type


class Document(models.Model):
    docfile = StdImageField(upload_to='documents/%Y/%m/%d', blank=True, variations={'large': (640, 480), 'thumbnail': (120, 120, True)})
    guest = models.ForeignKey(Guest, null=True, default="")
    document_type = models.ForeignKey(DocummentType, null=True, default="")
    title = models.CharField(max_length=20, default="")
    description  = models.TextField()
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class GuestVisit(models.Model):
    release_date = models.DateField(default=datetime.date.today)
#    release_time = models.IntegerField(blank=True,  null=True, default=12)
    inventory = models.ForeignKey(inventory, null=True)
    guestname = models.ForeignKey(Guest, default="")
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    arrival_date = models.DateTimeField(
            default=timezone.now)
    departure_date = models.DateTimeField(
            blank=True, null=True)

    def departure(self):
        self.departure_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Offense(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    offense = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.offense


class EmployeeFlag(models.Model):
    inventory = models.ForeignKey(inventory, null=True)
    author = models.ForeignKey('auth.User', null=True)
    offense = models.ForeignKey(Offense, null=True)
    employee = models.ForeignKey(Employee, null=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class ContractorFlag(models.Model):
    inventory = models.ForeignKey(inventory, null=True)
    author = models.ForeignKey('auth.User', null=True)
    offense = models.ForeignKey(Offense, null=True)
    contractor = models.ForeignKey(Contractor, null=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class SAIDFlags(models.Model):
    guest = models.ForeignKey(Guest, null=True)
    said = models.CharField(max_length=13, blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)
    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.said

class GuestFlag(models.Model):
    inventory = models.ForeignKey(inventory, null=True)
    offense = models.ForeignKey(Offense, null=True)
    author = models.ForeignKey('auth.User', null=True)
    guest = models.ForeignKey(Guest, null=True)

    name = models.CharField(max_length=200, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __int__(self):
        return self.guest
