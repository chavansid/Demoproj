from django.db import models
from django.db.models import Model 

# Create your models here.

class TaskCategory(models.Model):
    task_category = models.CharField(max_length=200)
    catagory_summery = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.task_category

class CheckPoints(models.Model):
    task_checkpoint = models.CharField(max_length=200)
    task_category = models.ForeignKey(TaskCategory,default=1,verbose_name="Category",on_delete=models.SET_DEFAULT)
    checkpoint_content = models.CharField(max_length=200)
    checkpoint_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Checkpoints"
    
    def __str__(self):
        return self.task_checkpoint
    
class Tasks(models.Model):
    task_title=models.CharField(max_length=200)
    task_describtion = models.TextField()
    task_checkpoint = models.ForeignKey(CheckPoints,default=1,verbose_name="Checkpoint",on_delete=models.SET_DEFAULT)
    task_duration = models.DateTimeField("Date of Complition")
    task_slug = models.CharField(max_length=200)

    def __str__(self):
        return self.task_title

