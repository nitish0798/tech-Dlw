from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

#Models

class Student(models.Model):
    """Model representing individual student"""
    first_name = models.CharField(max_length=50, help_text="Enter student's first name")
    last_name = models.CharField(max_length=50, help_text="Enter student's last name", blank=True)
    school = models.CharField(max_length=100, help_text="Enter the name of your school")
    email = models.EmailField(help_text="Enter your email")
    github = models.URLField(help_text="Enter your github link", null=True, blank=True)
    disp_pic = models.ImageField(upload_to='static/users/', null=True)

    #One student can belong to only one department
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    #One student can take only one project during his intern period
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

    class meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('student-detail', args=[str(self.id)])


class Project(models.Model):
    #Model representing individual project
    name = models.CharField(max_length=100, help_text="Enter project name")
    start_date = models.DateField('Date Started', null=True, blank=True)
    disp_pic = models.ImageField(upload_to='static/users/', null=True)

    #Tuple for project status
    PROJECT_STATUS=(
        ('o', 'Ongoing'),
        ('c', 'Completed')
    )

    status = models.CharField(
        max_length=1,
        choices=PROJECT_STATUS,
        blank=True,
        default='m',
        help_text='Project completion status',
    )
    
    description = models.CharField(max_length=1000, help_text='Brief Description of project')
    srs_link = models.URLField(help_text="Enter the URL to the SRS of this project", null=True, blank=True)
    project_link = models.URLField(help_text="Enter the github link of your project", null=True, blank=True)

    #One project belongs to a single department
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    #One project can belong to many technologies. One technology can be used in many projects
    tech_used = models.ManyToManyField('Technology', help_text='Tech Used in project')

    class meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('project-detail', args=[str(self.id)])


class Department(models.Model):
    #Model representing each department
    name = models.CharField(max_length=200, help_text='Enter department name')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Technology(models.Model):
    #Tech used in the project
    name = models.CharField(max_length=200, help_text='Enter technology used like web, machine learning, etc.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name