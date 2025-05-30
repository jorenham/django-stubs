from django.contrib.admin import HORIZONTAL as HORIZONTAL
from django.contrib.admin import VERTICAL as VERTICAL
from django.contrib.admin import AdminSite as AdminSite
from django.contrib.admin import ModelAdmin as ModelAdmin
from django.contrib.admin import StackedInline as StackedInline
from django.contrib.admin import TabularInline as TabularInline
from django.contrib.admin import action as action
from django.contrib.admin import autodiscover as autodiscover
from django.contrib.admin import display as display
from django.contrib.admin import register as register
from django.contrib.admin import site as site
from django.contrib.gis.admin.options import GISModelAdmin as GISModelAdmin

__all__ = [
    "HORIZONTAL",
    "VERTICAL",
    "AdminSite",
    "ModelAdmin",
    "StackedInline",
    "TabularInline",
    "action",
    "autodiscover",
    "display",
    "register",
    "site",
    "GISModelAdmin",
]
