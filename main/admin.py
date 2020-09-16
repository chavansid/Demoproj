from django.contrib import admin
from .models import Tasks,TaskCategory,CheckPoints
from tinymce.widgets import TinyMCE
from django.db import models
from django.db.models import Model 
class AdminTask(admin.ModelAdmin):

    #fields=["task_title","task_duration","task_describtion"]
    fieldset = [("titel/time",{"fields":["task_title","task_duration"]}),("content",{"field":["task_describtion"]})]
    fancycontent={models.TextField : {'widget':TinyMCE()}}

admin.site.register(TaskCategory)
admin.site.register(CheckPoints)

admin.site.register(Tasks,AdminTask)
