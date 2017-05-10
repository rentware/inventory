"This is the main model file for rentWareApp"
from django.db import models
from django.utils import timezone
from stdimage import StdImageField


class Item(models.Model):
    "This class defines the items in the inventory"
    author = models.ForeignKey('auth.User', null=True)
    item = models.CharField(max_length=10, db_index=True, default="")
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)


    def __str__(self):
        return self.item

class Customer(models.Model):
    "Model class"
    author = models.ForeignKey('auth.User', null=True)
    AccountCode = models.CharField(max_length=200, default="")
    CompanyName = models.CharField(max_length=200, default="")
    VATNumber = models.CharField(max_length=200, default="")

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    def save_date(self):
        "Called when data is updated"
        self.update_date = timezone.now()
        self.save()


    def __str__(self):
        return self.CompanyName


class Comment(models.Model):
    "Comment class for customers"
    author = models.ForeignKey('auth.User', null=True)
#    comment = models.TextField(
#    created_date = models.DateTimeField()



class Rental(models.Model):
    "Rental class"
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
    "Phone class"
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
    TypeofTelephone = models.CharField(max_length=1, \
            choices=PHONE_TYPE, default='O')
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
    "Image class"
    imagefile = StdImageField(upload_to='documents/%Y/%m/%d', \
            blank=True, variations={'large': (640, 480), \
            'thumbnail': (120, 120, True)})
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
    "Contact Type"
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    customer = models.ForeignKey(Customer, null=True)


class AddressType(models.Model):
    "address type"
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    "address main class"
    customer = models.ForeignKey(Customer, null=True)
    address_type = models.ForeignKey(AddressType, null=True)
    author = models.ForeignKey('auth.User', null=True)
    street = models.CharField(max_length=200)
    suburb = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)

    def save_date(self):
        "Save date when update record"
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.street

class TypeInventory(models.Model):
    "Inventory type not yet used"
    author = models.ForeignKey('auth.User', null=True)


class Inventory(models.Model):
    "Inventory main class"
#    u_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=200, default="")
    partID = models.CharField(max_length=10, default="")
    author = models.ForeignKey('auth.User', null=True)
    comments = models.TextField(default="")
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(
        blank=True, null=True)

#    def save(self):
#        self.updated_date = timezone.now()
#        self.save()


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
    "upload class"
    author = models.ForeignKey('auth.User', null=True)
    name = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Contact(models.Model):
    "contact class"
    author = models.ForeignKey('auth.User', null=True)
    firstname = models.CharField("Contacts first name", \
            max_length=200, default="")
    surname = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    cellPhoneNumber = models.CharField(max_length=200, default="")
    customer = models.ForeignKey(Customer, null=True, default="")
    comment = models.ForeignKey(Comment, null=True, default="")
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)

    def save_updated_date(self):
        "called when upfdating data"
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return '%s %s' % (self.firstname, self.surname)


"""

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
