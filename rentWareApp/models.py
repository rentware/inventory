# encoding: utf-8
#from django.contrib.auth.models import User
from django.db import models
#from django.utils.timezone import now
#from django.db import models
from django.utils import timezone
from stdimage import StdImageField

from django.db.models import permalink

import datetime


class Customer(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    AccountCode = models.CharField(max_length=200, default="")
    CompanyName = models.CharField(max_length=200, default="")
    VATNumber = models.CharField(max_length=200, default="")
#    user = models.ForeignKey('auth.User', null=True, default="")

    created_date = models.DateTimeField(
            default=timezone.now)
    update_date = models.DateTimeField(
            blank=True, null=True, default=timezone.now)

    def update_date(self):
        self.update_date = timezone.now()
        self.save()


    def __str__(self):
        return self.CompanyName


class Comment(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    comment = models.TextField()
    customer = models.ForeignKey(Customer, null=True)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)


    def __str__(self):
        return self.created_date.strftime('%d/%m/%Y')

class Rental(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def __str__(self):
        return self.name

class Telephone(models.Model):
    PHONE_TYPE = (
        ('P', 'Personal Cellphone'),
        ('C', 'Private Cellphone'),
        ('S', 'Standby Cellphone'),
        ('O', 'Office Landline'),
        ('K', 'Inquiries Landline'),
        ('H', 'Home Landline'),
        ('Q', 'Direct Office Extension'),
        ('V', 'Virtual Phone'),
    )
    TypeofTelephone = models.CharField(max_length=1, choices=PHONE_TYPE, default='O')
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    imagefile = StdImageField(upload_to='documents/%Y/%m/%d', blank=True, variations={'large': (640, 480), 'thumbnail': (120, 120, True)})
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def __str__(self):
        return self.name


class TypeContact(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True)
#    author = models.ForeignKey('auth.User')
#    name = models.CharField(max_length=200)
#    created_date = models.DateTimeField(
#    default=timezone.now)
#    updated_date = models.DateTimeField(
#    blank=True, null=True)

#    def updated_date(self):
#        self.updated_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.name
class AddressType(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    customer = models.ForeignKey(Customer, null=True)
    address_type = models.ForeignKey(AddressType, null=True)
    author = models.ForeignKey('auth.User', null=True)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code= models.CharField(max_length=200)
    created_date = models.DateTimeField(
    default=timezone.now)
    updated_date = models.DateTimeField(
    blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.street

class TypeInventory(models.Model):
    author = models.ForeignKey('auth.User', null=True)
#    author = models.ForeignKey('auth.User')
#    name = models.CharField(max_length=200)
#    created_date = models.DateTimeField(
#    default=timezone.now)
#    updated_date = models.DateTimeField(
#    blank=True, null=True)

#    def updated_date(self):
#        self.updated_date = timezone.now()
#        self.save()

#    def __str__(self):
#        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    partID = models.CharField(max_length=200, default="")
#    typeinventory = models.ForeignKey(TypeInventory, default="")
    author = models.ForeignKey('auth.User', null=True)
    comments = models.TextField(default="")
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()


"""
Account code
Description (Company Name)
vat number
Main Contact
Main Contact Telephone
Main Contact E-Mail
Main Contact Cell
Accounts Contact
Accounts Telephone
Contact person on site
Contact cell number on site
Postal Address (Business Address)
Delivery Address
"""



class Upload(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Contact(models.Model):
    author = models.ForeignKey('auth.User', null=True)
    firstname = models.CharField(max_length=200, default="")
    surname = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    cellPhoneNumber = models.CharField(max_length=200, default="")
    customer = models.ForeignKey(Customer, null=True, default="")
#    Telephone = models.ForeignKey(Telephone, null=True, default="")
#    address = models.ForeignKey(Address, null=True, default="")
    comment = models.ForeignKey(Comment, null=True, default="")
#    image  = models.ForeignKey(Image, null=True, default="")
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def updated_date(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.firstname, self.surname)


"""
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
"""

"""
class UserAccessinventory(models.Model):
    #author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200, default="notset")
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
"""
