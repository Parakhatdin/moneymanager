from django.contrib import admin
from mainapp.models import Category
from mainapp.models import Envelope
from mainapp.models import Family
from mainapp.models import Member
from mainapp.models import MemberAuthdata
from mainapp.models import Transaction

# Register your models here.
admin.site.register(Category)
admin.site.register(Envelope)
admin.site.register(Family)
admin.site.register(Member)
admin.site.register(MemberAuthdata)
admin.site.register(Transaction)
