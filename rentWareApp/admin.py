
from django.contrib import admin
from .models import Inventory
from .models import Customer
from .models import Contact
from .models import Upload

from .models import TypeContact
from .models import AddressType
from .models import TypeInventory
from .models import Address
#from .models import EmployeeType
#from .models import inventoryType
#from .models import VisaType
#from .models import Offense
#from .models import Nationality
#from .models import EntityType
#from .models import UserGroup
#from .models import UserPerm
#from .models import Document
#from .models import DocummentType
#from .models import UserAccessinventory



admin.site.register(Inventory)
admin.site.register(Customer)
admin.site.register(Contact)
admin.site.register(Upload)

admin.site.register(TypeContact)
admin.site.register(AddressType)
admin.site.register(Address)
admin.site.register(TypeInventory)

#admin.site.register(ContractorType)
#admin.site.register(Employee)
#admin.site.register(inventoryType)
#admin.site.register(VisaType)
#admin.site.register(Offense)
#admin.site.register(Nationality)
#admin.site.register(EntityType)
#admin.site.register(UserGroup)
#admin.site.register(UserPerm)
#admin.site.register(Document)
#admin.site.register(DocummentType)
#admin.site.register(UserAccessinventory)

# Register your models here.
