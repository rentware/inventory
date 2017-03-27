
from django.contrib import admin
from .models import GuestVisit
from .models import Guest
from .models import inventory
from .models import Contractor
from .models import Employee
from .models import ContractorType
from .models import EmployeeType
from .models import inventoryType
from .models import VisaType
from .models import GuestFlag
from .models import Offense
from .models import Nationality
from .models import EntityType
from .models import UserGroup
from .models import UserPerm
from .models import Document
from .models import DocummentType
from .models import UserAccessinventory



admin.site.register(GuestVisit)
admin.site.register(Guest)
admin.site.register(inventory)
admin.site.register(Contractor)
admin.site.register(EmployeeType)
admin.site.register(ContractorType)
admin.site.register(Employee)
admin.site.register(inventoryType)
admin.site.register(VisaType)
admin.site.register(GuestFlag)
admin.site.register(Offense)
admin.site.register(Nationality)
admin.site.register(EntityType)
admin.site.register(UserGroup)
admin.site.register(UserPerm)
admin.site.register(Document)
admin.site.register(DocummentType)
admin.site.register(UserAccessinventory)

# Register your models here.
