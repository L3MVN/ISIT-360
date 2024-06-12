from django.db import models

# Create your models here

class Department(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["title"]

class Employee(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField()
    projects = models.ManyToManyField(Project, related_name='employees')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]
