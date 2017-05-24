# import the logging library
#import logging

# Get an instance of a logger
#logger = logging.getLogger(__name__)


#from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .models import Customer
from .models import Address
from .models import Image
from .models import Comment
from .models import Rental
from .models import Contact
from .models import Rate
from .models import Specification

from django.contrib.sites.shortcuts import get_current_site

#from django.views.generic import ListView

#import pdb
#pdb.set_trace()


#from .models import Contractor
#from .models import GuestVisit
#rom .models import EmployeeFlag
#from .models import ContractorFlag
#from .models import UserGroup
#from .models import UserPerm
#from .models import Document
#from .models import UserAccessinventory
#from .models import SAIDFlags

from django.contrib.auth.models import User


#login
#from django.contrib.auth import authenticate, login
from .forms import CustomerForm
from .forms import ContactForm
from .forms import AddressForm
from .forms import CommentForm
from .forms import RentalForm
from .forms import ImageForm
from .forms import InventoryForm

#from .forms import SubUserForm

#from django.utils.decorators import method_decorator
#from django.contrib.auth.decorators import login_required

from django.utils import timezone
#import datetime

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.contrib.auth.decorators import user_passes_test

from django.core.urlresolvers import reverse

from django.utils import six
from django.core.exceptions import PermissionDenied

from django.contrib.auth.models import Group

from django.http import HttpResponse
#from django.views import View
#class sample
from dateutil import parser

from django.contrib import messages

#from django_ajax.decorators import ajax

from django.views.generic import TemplateView
from django.views.generic import DetailView, CreateView, UpdateView, ListView, DeleteView


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoggedInMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class RateListView(LoggedInMixin, ListView):
    "rate list"
    template_name = "rates/rate_list.html"
    context_object_name = 'all_rates'
    def get_queryset(self):
        result = Rate.objects.filter(inventory__slug=self.kwargs ['slug']).order_by('slug')
        return result

class SpecificationListView(LoggedInMixin, ListView):
    "rate list"
    template_name = "specification/specification_list.html"
    context_object_name = 'all_specifications'
    def get_queryset(self):
        result = Specification.objects.filter(inventory__slug=self.kwargs ['slug']).order_by('slug')
        return result


#Customer block
class CustomerListView(LoggedInMixin, ListView):
    "Customer list"
    template_name = "customers/customer_list.html"
#    model = Customer
    context_object_name = 'all_customers'
    paginate_by = 4
#    @method_decorator(login_required)
    def get_queryset(self):
        search_term = ''
        if ('search_term' in self.request.GET) and self.request.GET['search_term'].strip():
            search_term = self.request.GET['search_term'].strip()
            result = Customer.objects.filter(Q(AccountCode=search_term))
        else:
            result = Customer.objects.all().order_by('-created_date')

        return result


class CustomerCreateView(LoggedInMixin, CreateView):
    "Customer list"
    form_class = CustomerForm
    template_name = 'customers/customer_edit.html'
    success_url = '/customer_list'


class CustomerUpdateView(LoggedInMixin, UpdateView):
    "Customer update"
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_edit.html'
    success_url = '/customer_list'


class CustomerDeleteView(LoggedInMixin, DeleteView):
    "Customer delete"
    form_class = CustomerForm
    template_name = 'customers/customer_edit.html'
    success_url = '/customer_list'


class CustomerDetailView(LoggedInMixin, DetailView):
    "Customer detail"
    form_class = CustomerForm
    template_name = "customer_detail/customer_detail.html"
    context_object_name = 'customer_detail'
    model = Customer

    def get_context_data(self, **kwargs):
            context = super(CustomerDetailView, self).get_context_data(**kwargs)
            context['update_date'] = timezone.now()
            return context



#inventorys block
class InventoryListView(LoggedInMixin, ListView):
    "Customer list"
    template_name = "inventories/inventory_list.html"
    context_object_name = 'all_inventories'
    paginate_by = 4
    def get_queryset(self):
        search_term = ''
        if ('search_term' in self.request.GET) and self.request.GET['search_term'].strip():
            search_term = self.request.GET['search_term'].strip()
            result = Inventory.objects.filter(Q(partID=search_term))
        else:
            result = Inventory.objects.all().order_by('-created_date')

        return result


class InventoryCreateView(LoggedInMixin, CreateView):
    "Customer list"
    form_class = InventoryForm
    template_name = 'inventories/inventory_edit.html'
    success_url = '/inventory_list'


class InventoryUpdateView(LoggedInMixin, UpdateView):
    "Customer update"
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventories/inventory_edit.html'
    success_url = '/inventory_list'


class InventoryDeleteView(LoggedInMixin, DeleteView):
    "Customer delete"
    form_class = InventoryForm
    template_name = 'inventories/inventory_edit.html'
    success_url = '/inventory_list'




class InventoryDetailView(LoggedInMixin, DetailView):
    "Inventory detail"
    template_name = "inventories/inventory_detail.html"
    context_object_name = 'inventory_detail'
    model = Inventory

    def get_context_data(self, **kwargs):
            context = super(InventoryDetailView, self).get_context_data(**kwargs)
            context['update_date'] = timezone.now()
            return context


#end block inventorys




def group_required(group, login_url=None, raise_exception=False):
    def check_perms(user):
        if isinstance(group, six.string_types):
            groups = (group, )
        else:
            groups = group
        # First check if the user has the permission (even anon users)
        if user.groups.filter(name__in=groups).exists():
            return True
        # In case the 403 handler should be called raise the exception
        if raise_exception:
            # As the last resort, show the login form
            raise PermissionDenied
        return False
    return user_passes_test(check_perms, login_url='denied')

#not used


def customer_main_view(request, customer_pk):
    customer = Customer.objects.filter(pk=customer_pk).get()
    contacts = Contact.objects.filter(customer_id=customer_pk).all()
    addresses = Address.objects.filter(customer_id=customer_pk).all()
    comments = Comment.objects.filter(customer_id=customer_pk).all()
    images = Image.objects.filter(customer_id=customer_pk).all()

    return render(request, 'customer_main_view/customer_main_view.html',
        {'customer': customer, 'contacts': contacts,'addresses': addresses,'comments': comments,'images': images,})


def rental_list(request, customer_pk):
    rental = Rental.objects.filter(customer=customer_pk).order_by('pk')
    customer = Customer.objects.filter(pk=customer_pk).get()

    return render(request, 'rentals/rental_list.html',
        {'rental': rental, 'customer': customer, })


def rental_new(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.author = request.user
            rental.customer_id = customer_pk
            rental.created_date = timezone.now()
            rental.save()
            messages.success(request, 'Rental details saved.')
            return redirect('rental_list', customer_pk=customer_pk)
    else:
        isnew=0
        form = RentalForm()
    return render(request, 'rentals/rental_edit.html', {'form': form,  'isnew': isnew,})


def comment_list(request, customer_pk):
    comment = Comment.objects.filter(customer=customer_pk).order_by('pk')
    customer = Customer.objects.filter(pk=customer_pk).get()

    return render(request, 'comments/comment_list.html',
        {'comment': comment, 'customer': customer, })

def comment_new(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.customer_id = customer_pk
            comment.created_date = timezone.now()
            comment.save()
            messages.success(request, 'Comment details saved.')
            return redirect('comment_list', customer_pk=customer_pk)
    else:
        form = CommentForm()
    return render(request, 'comments/comment_edit.html', {'form': form, })


def image_list(request, customer_pk):
    image = Image.objects.filter(customer=customer_pk).order_by('pk')
    customer = Customer.objects.filter(pk=customer_pk).get()

    return render(request, 'images/image_list.html',
        {'image': image, 'customer': customer, })

def address_new(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.author = request.user
            address.customer_id = customer_pk
            address.created_date = timezone.now()
            address.save()
            messages.success(request, 'Address details saved.')
            return redirect('address_list', customer_pk=customer_pk)
    else:
        form = AddressForm()
    return render(request, 'addresses/address_edit.html', {'form': form, })

def image_new(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            image.customer_id = customer_pk
            image.created_date = timezone.now()
            image.save()
            messages.success(request, 'Image details saved.')
            return redirect('image_list', customer_pk=customer_pk)
    else:
        form = ImageForm()
    return render(request, 'images/image_edit.html', {'form': form, })


def contact_list(request, customer_pk):
    contact = Contact.objects.filter(customer=customer_pk).order_by('pk')
    customer = Customer.objects.filter(pk=customer_pk).get()

    return render(request, 'contacts/contact_list.html',
        {'contact': contact, 'customer': customer, })

def contact_new(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.customer_id = customer_pk
            contact.created_date = timezone.now()
            contact.save()
            messages.success(request, 'Contact details saved.')
            return redirect('contact_list', customer_pk=customer_pk)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_edit.html', {'form': form, })




def address_list(request, customer_pk):
    addresses = Address.objects.filter(customer=customer_pk).order_by('pk')
    customer = Customer.objects.filter(pk=customer_pk).get()

    return render(request, 'addresses/address_list.html',
        {'addresses': addresses, 'customer': customer, })


def customer_list(request):
    current_site = get_current_site(request)
    #messages.info(request, "Welcome "+request.user.username)
    customers = Customer.objects.order_by('pk')
    return render(request, 'customers/customer_list.html', {"customers": customers,})

def customer_new(request):
    if request.method == "POST":
        user = None
        if request.user.is_authenticated():
            user = request.user.pk

        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            #customer._id = est_pk
            customer.published_date = timezone.now()
            customer.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_edit.html', {'form': form})


def customer_edit(request):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            customer.published_date = timezone.now()
            customer.save()
            return redirect('customer_list')
    else:
        form = CustomForm(instance=customer)
    return render(request, 'customers/customer_edit.html', {'form': form})

def document_edit(request, pk, est_pk):
    document = get_object_or_404(Document, pk=pk)
    if request.method == "POST":
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            document = form.save(commit=False)
            document.author = request.user
            document.published_date = timezone.now()
            document.save()
            return redirect('inventory_detail_guests', pk=est_pk)
    else:
        form = DocumentForm(instance=guest)
    return render(request, 'downloaded/upload_edit.html', {'form': form})


def about(request):
    return render(request, 'documents/about.html', {})


def tandc(request):
    return render(request, 'documents/tandc.html', {})




"""
#@group_required("employee_flag")
def employee_flag(request, est_pk, pk):
    if request.method == "POST":
#        user = None
        if request.user.is_authenticated():
            pass
#            user = request.user.pk
        form = EmployeeFlagForm(request.POST)
        if form.is_valid():
            flag = form.save(commit=False)
            flag.employee_id = pk
            flag.author = request.user
            flag.inventory_id = est_pk
            flag.updated_date = timezone.now()
            flag.save()
            addflag = get_object_or_404(Employee, pk=flag.employee_id)
            addflag.flagstatus=1
            addflag.save()
            return redirect('inventory_detail_employees', pk=est_pk)
    else:
        form = EmployeeFlagForm()
    return render(request, 'flag/flag_edit.html', {'form': form})


#@group_required("contractor_flag")
def contractor_flag(request, est_pk, pk):
    if request.method == "POST":
        if request.user.is_authenticated():
            pass
#            user = request.user.pk

        form = ContractorFlagForm(request.POST)
        if form.is_valid():
            flag = form.save(commit=False)
            flag.contractor_id = pk
            flag.author = request.user
            flag.inventory_id = est_pk
            flag.updated_date = timezone.now()
            flag.save()
            addflag = get_object_or_404(Contractor, pk=flag.contractor_id)
            addflag.flagstatus=1
            addflag.save()
            return redirect('inventory_detail_contractors', pk=est_pk)
    else:
        form = ContractorFlagForm()
    return render(request, 'flag/flag_edit.html', {'form': form})


    guests = Guest.objects.order_by('created_date')
    return render(request, 'guests/guest_list.html', {"guests": guests})


#TODO flag list
def guest_visit_list(request, est_pk, guest_pk):
    guest_visits = GuestVisit.objects.filter(guestname=guest_pk).order_by('-arrival_date')
    guest = Guest.objects.filter(pk=guest_pk).get()

    return render(request, 'visits/visit_list.html', {'guest': guest,
    'guest_visits': guest_visits })


#TODO flag list
def list_guest_flag(request, est_pk, guest_pk):
    guest_flags = GuestFlag.objects.filter(guest=guest_pk).order_by('-created_date')
    guest = Guest.objects.filter(pk=guest_pk).get()

    return render(request, 'flag/flag_list.html', {'guest': guest,
    'guest_flags': guest_flags })


#@group_required("guest_flag")
def guest_flag(request, est_pk, pk):
    if request.method == "POST":
#        user = None
        if request.user.is_authenticated():
            pass

        form = GuestFlagForm(request.POST)
        if form.is_valid():
            flag = form.save(commit=False)
            flag.guest_id = pk
            flag.author = request.user
            flag.inventory_id = est_pk
            flag.updated_date = timezone.now()
            flag.save()
            addflag = get_object_or_404(Guest, pk=flag.guest_id)
            addflag.flagstatus=1
            addflag.save()
            said = SAIDFlags(guest_id=pk, said=addflag.SAidentityNo)
            said.save()

            return redirect('list_guest_flag', guest_pk=pk, est_pk=est_pk )
    else:
        form = GuestFlagForm()
    return render(request, 'flag/flag_edit.html', {'form': form})

#@group_required("guest_new")
def guest_new(request, est_pk):  # need pk of inventory
    if request.method == "POST":
        user = None
        if request.user.is_authenticated():
            user = request.user.pk

        form = GuestForm(request.POST)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.author = request.user
            guest.inventory_id = est_pk
            guest.published_date = timezone.now()
            guest.save()
            return redirect('inventory_detail_guests', pk=est_pk)
    else:
        form = GuestForm()
    return render(request, 'guests/guest_edit.html', {'form': form})


#@group_required("guest_edit")
def guest_edit(request, pk, est_pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "POST":
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            guest = form.save(commit=False)
            guest.author = request.user
            guest.published_date = timezone.now()
            guest.save()
            return redirect('inventory_detail_guests', pk=est_pk)
    else:
        isnew=0
        form = GuestForm(instance=guest)
    return render(request, 'guests/guest_edit.html', {'form': form, 'guest': guest, 'isnew': isnew, 'est_pk': est_pk,})

#employee
#@group_required("employee_new")
def employee_new(request, est_pk):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.inventory_id = est_pk
            employee.published_date = timezone.now()
            employee.save()


            return redirect('inventory_detail_employees', pk=est_pk)
    else:
        form = EmployeeForm()
    return render(request, 'employees/employee_edit.html', {'form': form})

#@group_required("employee_edit")
def employee_edit(request, pk, est_pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.author = request.user
            employee.published_date = timezone.now()
            employee.save()
            return redirect('inventory_detail_employees', pk=est_pk)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/employee_edit.html', {'form': form})

#contractor

#@group_required("contractor_new")
def contractor_new(request, est_pk):
    if request.method == "POST":
#        user = None
#        if request.user.is_authenticated():
#            user = request.user.pk

        form = ContractorForm(request.POST)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.author = request.user
            contractor.inventory_id = est_pk
            contractor.published_date = timezone.now()
            contractor.save()
            return redirect('inventory_detail_contractors', pk=est_pk)
    else:
        form = ContractorForm()
    return render(request, 'contractors/contractor_edit.html', {'form': form})

#@group_required("contractor_edit")
def contractor_edit(request, pk, est_pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == "POST":
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            contractor = form.save(commit=False)
            contractor.author = request.user
            contractor.published_date = timezone.now()
            contractor.save()
            return redirect('inventory_detail_contractors', pk=est_pk)
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'contractors/contractor_edit.html', {'form': form})


def isnewvisit(guest_pk):
    entry=""
    visit=""
    try:
        visit = GuestVisit.objects.filter(guestname_id=guest_pk)
    except:
        pass

    if (visit.count() == 0):
        entry="new"
    else:
        try:
            entry = GuestVisit.objects.filter(guestname_id=guest_pk).latest('arrival_date').departure_date
            entry = entry.strftime('%d/%m/%Y')
        except:
            entry="not a date"

    return entry

#visit
#@group_required("visit_new")
def new_guest_visit(request, guest_pk, est_pk):
    isnew = isnewvisit(guest_pk)
    print(isnew)
    if request.method == "POST":

        if isnew == "new":
            pass
        else:
            try:
                parsed_date = parser.parse(isnew)
            # formatting
            except ValueError:
            # something if format incorrect
                messages.warning(request, 'Visit not saved. guest still booked in')
                return redirect('guest_visit_list', est_pk=est_pk, guest_pk=guest_pk)

        form = GuestVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.author = request.user
            visit.inventory_id = est_pk
            visit.guestname_id = guest_pk
            visit.arrival_date = timezone.now()
            visit.save()
            messages.success(request, 'Visit details saved.')
            return redirect('guest_visit_list', est_pk=est_pk, guest_pk=guest_pk)
    else:
        isnew=0
        form = GuestVisitForm()
    return render(request, 'visits/visit_edit.html', {'form': form, 'isnew': isnew})


#FINDME
#@group_required("visit_edit")
def edit_guest_visit(request, guest_pk, visit_pk, est_pk):
    visit = get_object_or_404(GuestVisit, pk=visit_pk)
    if request.method == "POST":
        form = GuestVisitForm(request.POST, instance=visit)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.author = request.user
            if not visit.departure_date:
                visit.departure_date = timezone.now()
            visit.save()
            return redirect('guest_visit_list', est_pk=est_pk, guest_pk=guest_pk)
    else:
        form = GuestVisitForm(instance=visit)
    return render(request, 'visits/visit_edit.html', {'form': form})

#documnsts
#return HttpResponse(json.dumps(infoDict))

def testmethod(request):
    return HttpResponse('Hello World!')

#@ajax
def hello(request):
    a = request.GET["id"]
    findflag = SAIDFlags.objects.filter(said=a)
    if findflag:
        flagged="flagged"
    else:
        flagged = "clear"

    return HttpResponse(flagged)


#RETURNHERE
def denied(request):
    return render(request, 'denied/denied.html', {})

def test(request):
    return render(request, 'users/test.html', {})

def test2(request):
    form = GuestVisitForm(request.POST)
    if form.is_valid():
        visit = form.save(commit=False)
        visit.save()
        messages.success(request, 'Visit details saved.')
        return redirect('guest_visit_list', est_pk="1", guest_pk="1")
    else:
        form = GuestVisitForm()

    return render(request, 'guests/test.html', {'form': form})
#    return render(request, 'users/test.html', {})
"""
"""

def offenses(request):
    return render(request, 'documents/offenses.html', {})

#TODO finish
def guest_upload_list(request, guest_pk, est_pk):
    guest = get_object_or_404(Guest, pk=guest_pk)
    guest_upload = Document.objects.filter(guest=guest)
    return render(request, 'uploaded/upload_list.html', {"guest_upload": guest_upload,
        "guest_pk": guest_pk, "est_pk": est_pk})

#TODO IMAGE UPLOAD
def guest_upload_file(request, guest_pk, est_pk):
    if request.method == 'POST':
        guest = get_object_or_404(Guest, pk=guest_pk)
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            pic = form.save(commit=False)
            pic.guest = guest
            pic.updated_date = timezone.now()
            pic.save()
            return redirect('guest_upload_list', guest_pk=guest_pk, est_pk=est_pk)
    else:
        form = UploadFileForm()
    return render(request, 'uploaded/upload.html', {'form': form})


#@group_required("guest_list")
def guest_list(request):
    guests = Guest.objects.order_by('created_date')
    return render(request, 'guests/guest_list.html', {"guests": guests})

#@group_required("inventory_edit")
def inventory_edit(request, pk):
    inventory = get_object_or_404(inventory, pk=pk)
    if request.method == "POST":
        form = inventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.author = request.user
            inventory.published_date = timezone.now()
            inventory.save()
            return redirect('inventory_detail', pk=pk)
    else:
        form = inventoryForm(instance=inventory)
    return render(request,
    'inventory/inventory_edit.html', {'form': form})


#inventory
#@group_required("inventory_new")
def inventory_new(request):
    if request.method == "POST":
#        user = None
#        if request.user.is_authenticated():
#            user = request.user.pk
        form = inventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.author = request.user
            inventory.published_date = timezone.now()
            inventory.save()
            return redirect('inventory_detail', pk=inventory.pk)
    else:
        form = inventoryForm()
    return render(request,
    'inventory/inventory_edit.html', {'form': form})

#not used
def getUserGroups(user):
    user_group = UserPerm.objects.get(name=user)
    a = user_group.user_groups.all()
    dic = []
    [dic.append(k.group) for k in a]
    return dic

def userAccess(user, inventory):
    a = False
    useraccess = UserAccessinventory.objects.filter(users_inventory=user, inventory=inventory)
    user_creator = inventory.objects.filter(author=user, pk=inventory.pk)
    if ((useraccess.count() + user_creator.count()) > 0):
        a = True

    return a


@login_required
#@group_required("inventory_list")
"""
def inventory_list(request):
    user = request.user
    useraccess = UserAccessinventory.objects.filter(users_inventory=user)
    inventorys = inventory.objects.filter(author=user).order_by('-created_date')

    other_inventorys = inventory.objects.filter(author=user).order_by('-created_date')
    debugtext = ""

    return render(request, 'inventory/inventory_list.html',
         {"inventorys": inventorys,
         "useraccess": useraccess,
         "debugtext": debugtext,
         })
"""

class inventoryDetailAdinstration(View):
        def get(self, request):
            user = request.user
            inventorys = inventory.objects.filter(author=user, pk=pk)
            inventory = get_object_or_404(inventory, pk=pk)
            useraccess = UserAccessinventory.objects.filter(inventorys=inventory)

            guest_list = Guest.objects.filter(inventory=pk).order_by('-created_date')

            return render(request, 'inventory/inventory_detail_administration.html',
            {"inventorys": inventorys,
            "useraccess": useraccess,
            "inventory": inventory,
            })


def inventory_detail_administration(request, pk):
    user = request.user

#    inventorys = inventory.objects.order_by('published_date')
    inventorys = inventory.objects.filter(author=user, pk=pk)
    inventory = get_object_or_404(inventory, pk=pk)
    useraccess = UserAccessinventory.objects.filter(inventory=inventory)

    guest_list = Guest.objects.filter(inventory=pk).order_by('-created_date')

    return render(request, 'inventory/inventory_detail_administration.html',
         {"inventorys": inventorys,
         "useraccess": useraccess,
         "inventory": inventory,
         })


#@login_required
#@group_required("inventory_list")
def administration_list(request):
    user = request.user
    useraccess = UserAccessinventory.objects.all()
#    inventorys = inventory.objects.order_by('published_date')
    inventorys = inventory.objects.filter(author=user)

    return render(request, 'administration/administration_list.html',
         {"inventorys": inventorys,
         "useraccess": useraccess,
         })


def sub_user_delete(request, est_pk, sub_user_pk):
    query = UserAccessinventory.objects.get(pk=sub_user_pk)
    query.delete()
    return redirect('inventory_detail_administration', pk=est_pk)

#TODO
def sub_user_new(request, est_pk):
    if request.method == "POST":
        user = None
        if request.user.is_authenticated():
            user = request.user.pk

        form = SubUserForm(request.POST)
        inventory = inventory.objects.filter(pk=est_pk)
        if form.is_valid():
            sub_user = form.save(commit=False)
            sub_user.created_date = timezone.now()
            sub_user.inventory_id = est_pk
            sub_user.save()
            return redirect('inventory_detail_administration', pk=est_pk)
    else:
        form = SubUserForm()
    return render(request, 'administration/sub_user_edit.html', {'form': form})


#@login_required
#@group_required("flagsearch_list")
"""
def flagsearch_list(request, pk):

    guest_list = ""  #Guest.objects.filter(inventory=pk)
    employee_list = ""
    contractor_list = ""
"""

# need list of actual
    guest_name_search = request.GET.get("srch-term")
    if(guest_name_search):

        #TODO first find integer value for sa id if that fails get the next values
        try:
            guest_list = GuestFlag.objects.filter(Q(guest__SAidentityNo=int(guest_name_search)))
        except:
            pass

        guest_list = GuestFlag.objects.filter(Q(guest__show_name__contains=guest_name_search) | \
         Q(guest__emailAddress=guest_name_search)  | Q(guest__PassportNo=guest_name_search)   | Q(guest__cellPhoneNumber=guest_name_search))
        employee_list = EmployeeFlag.objects.filter(Q(employee__show_name__contains=guest_name_search))
        contractor_list = ContractorFlag.objects.filter(Q(contractor__show_name__contains=guest_name_search))


#| Q(guest__SAidentityNo=int(guest_name_search))
    return render(request, 'findflag/findflag_detail.html',
         {"guest_list": guest_list,
          "employee_list": employee_list,
          "contractor_list": contractor_list,
         })


@login_required
#@group_required("inventory_detail_employees")
def inventory_detail_employees(request, pk):
    inventory = get_object_or_404(inventory, pk=pk)

    employee_list = Employee.objects.filter(inventory=pk).order_by('-created_date')

    employee_name_search = request.GET.get("srch-term-employee")
    if(employee_name_search):
        employee_list = Employee.objects.filter(Q(inventory=pk),  Q(show_name__contains=employee_name_search))

    paginator = Paginator(employee_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)


    return render(request, 'inventory/inventory_detail_employees.html',
    {"employees": employees,
    "inventory": inventory, })


@login_required
#@group_required('test')
#fundme
#@group_required("inventory_detail_guests")
def inventory_detail_guests(request, pk):
    inventory = get_object_or_404(inventory, pk=pk)

    debugtext = userAccess(request.user, inventory)
#FINDME
    if not debugtext:
        send_simple_message()
        return redirect('denied')

    guest_list = Guest.objects.filter(inventory=pk).order_by('-created_date')

#for global search leave out estabishment serach
    guest_name_search = request.GET.get("srch-term-guest")
#    print(guest_name_search)
    if(guest_name_search):
        guest_list = Guest.objects.filter(Q(inventory=pk),  Q(show_name__contains=guest_name_search) | \
         Q(emailAddress=guest_name_search)  | Q(PassportNo=guest_name_search)   | Q(cellPhoneNumber=guest_name_search))


    paginator = Paginator(guest_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        guests = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        guests = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        guests = paginator.page(paginator.num_pages)

    return render(request, 'inventory/inventory_detail_guests.html',
    {"guests": guests,
     "debugtext": debugtext,
    "inventory": inventory, })


#@login_required
#@group_required("inventory_detail_contractors")
def inventory_detail_contractors(request, pk):
    inventory = get_object_or_404(inventory, pk=pk)

#contractors

    contractor_list = Contractor.objects.filter(inventory=pk).order_by('-created_date')

    contractor_name_search = request.GET.get("srch-term-contractor")
    if(contractor_name_search):
        contractor_list = Contractor.objects.filter(Q(inventory=pk),  Q(show_name__contains=contractor_name_search))

    paginator = Paginator(contractor_list, 5)  # Show 25 contacts per page
    page = request.GET.get('pagec')
    try:
        contractors = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contractors = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contractors = paginator.page(paginator.num_pages)

    return render(request, 'inventory/inventory_detail_contractors.html',
    {"contractors": contractors,
    "inventory": inventory, })


# Not used
@login_required
def inventory_detail(request, pk):

    #group = Group(name="Editor")
    #group.save()                  # save this new group for this example
    #user = User.objects.get(pk=1) # assuming, there is one initial user
    #user.groups.add(group)        # user is now in the "Editor" group
    #userg = user.groups.all() #returns [<Group: Editor>]

#    empoyee_name_search = ""

    inventory = get_object_or_404(inventory, pk=pk)
    #inventory = inventory.objects.get(pk=pk)
    guest_list = Guest.objects.filter(inventory=pk)

#for global search leave out estabishment serach

    guest_name_search = request.GET.get("srch-term")
    if(guest_name_search):
        guest_list = Guest.objects.filter(Q(inventory=pk),  Q(show_name__contains=guest_name_search) | Q(SAidentityNo=str(guest_name_search)) | \
         Q(emailAddress=guest_name_search)  | Q(PassportNo=guest_name_search)   | Q(cellPhoneNumber=guest_name_search))

    paginator = Paginator(guest_list, 5)  # Show 25 contacts per page
    pageg = request.GET.get('page')
    try:
        guests = paginator.page(pageg)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        guests = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        guests = paginator.page(paginator.num_pages)

#employees
    employee_list = Employee.objects.filter(inventory=pk)

    employee_name_search = request.GET.get("srch-term-employee")
    if(employee_name_search):
        employee_list = Employee.objects.filter(Q(inventory=pk),  Q(show_name__contains=employee_name_search))


    paginator = Paginator(employee_list, 5)  # Show 25 contacts per page
    page = request.GET.get('pagee')
    try:
        employees = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        employees = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        employees = paginator.page(paginator.num_pages)

#contractors

    contractor_list = Contractor.objects.filter(inventory=pk)

    contractor_name_search = request.GET.get("srch-term-contractor")
    if(contractor_name_search):
        contractor_list = Contractor.objects.filter(Q(inventory=pk),  Q(show_name__contains=contractor_name_search))

    paginator = Paginator(contractor_list, 5)  # Show 25 contacts per page
    page = request.GET.get('pagec')
    try:
        contractors = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contractors = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contractors = paginator.page(paginator.num_pages)


    return render(request, 'inventory/inventory_detail.html',
    {"inventory": inventory,
    "guests": guests, "employees": employees,
    "contractors": contractors})

@ajax
def check_sa_id_for_flag(reqest, SAID):
    c = 2 + 3
    return {'result': c}

#SAID info
#    {YYMMDD}{G}{SSS}{C}{A}{Z}
#YYMMDD : Date of birth.
#G  : Gender. 0-4 Female; 5-9 Male.
#SSS  : Sequence No. for DOB/G combination.
#C  : Citizenship. 0 SA; 1 Other.
#A  : Usually 8, or 9 [can be other values]
#Z  : Control digit calculated in the following section:

"""
