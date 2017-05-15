#model

class Customer(models.Model):
    "Model class"
    author = models.ForeignKey('auth.User', null=True)
    AccountCode = models.CharField(max_length=200, unique=True)
    CompanyName = models.CharField(max_length=200, default="")
    VATNumber = models.CharField(max_length=200, default="")

    created_date = models.DateTimeField(
        default=timezone.now)
    update_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    s = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.s = slugify(self.AccountCode)
        self.update_date = timezone.now()
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.CompanyName

#views

class CustomerListView(ListView):
    "Customer list"
    template_name = "customers/customer_list.html"
    model = Customer
    context_object_name = 'all_customers'
    paginate_by = 4


class CustomerDetailView(DetailView):
    "Customer detail"
    template_name = "customer_detail/customer_detail.html"
    context_object_name = 'customer_detail'
    model = Customer

    def get_context_data(self, **kwargs):
            context = super(CustomerDetailView, self).get_context_data(**kwargs)
            context['update_date'] = timezone.now()
            return context

# (?P<slug>[\w\-]+)/$

#urls

    url(r'^customer/(?P<slug>[\w\-]+)/$', CustomerDetailView.as_view(), name='customer_detail'),

    url(r'^customer_list/$', CustomerListView.as_view(), name='customer_list'),
    url(r'^customer/(?P<slug>[0-9]+)/$', CustomerDetailView.as_view(), name='customer_detail'),


#template snippet

{% for g in object_list%}
            <tr>
              <td style="width:10%"><a href="{% url 'customer_detail' pk=g.pk %}" >
              {{ g.AccountCode }}
              </a></td>
....
