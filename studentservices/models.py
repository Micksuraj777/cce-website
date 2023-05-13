from django.db import models

from website.models import Faculty

# Create your models here.
class Artsupdates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField( default="No data")
    date = models.DateField()
    def __str__(self):
        return self.title

class ArtsEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='arts/events')
    def __str__(self):
        return self.title 


class artsTeamStatus(models.Model):
    TEAMS = (("cetus","cetus"),("pegasus","pegasus"),("taurs","taurs"),("lupus","lupus"))
    teamname = models.CharField(max_length=100,choices=TEAMS)
    logo = models.ImageField(upload_to='arts/teams/logos',default='arts/teams/logos/default.png')
    score = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    color = models.CharField(max_length=100,default='red-700')
    image = models.ImageField(upload_to='arts/teams')
    def __str__(self):
        return self.teamname

class ArtsGallery(models.Model):
    image = models.ImageField(upload_to='arts/gallery')
    def __str__(self):
        return self.image.name


class SportsUpdates(models.Model):
    title = models.CharField(max_length=100)
    data = models.TextField( default="No data")
    date = models.DateField()
    def __str__(self):
        return self.title

class SportsEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='sports/events')
    def __str__(self):
        return self.title

class SportsTeamStatus(models.Model):
    TEAMS = (("cetus","cetus"),("pegasus","pegasus"),("taurs","taurs"),("lupus","lupus"))
    teamname = models.CharField(max_length=100,choices=TEAMS)
    logo = models.ImageField(upload_to='sports/teams/logos',default='sports/teams/logos/default.png')
    score = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    color = models.CharField(max_length=100,default='red-700')
    image = models.ImageField(upload_to='sports/teams')
    def __str__(self):
        return self.teamname

class SportsGallery(models.Model):
    image = models.ImageField(upload_to='arts/gallery')
    def __str__(self):
        return self.image.name


class NssFaculty(models.Model):
    faculty = models.ManyToManyField(Faculty)


class NssStudents(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nss/students')
    def __str__(self):
        return self.name

class NssGallery(models.Model):
    image = models.ImageField(upload_to='nss/gallery')
    def __str__(self):
        return self.image.name

class NssEvents(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='nss/events')
    def __str__(self):
        return self.title


class Clubs(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs/logos')
    description = models.CharField(max_length=100)
    link  = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class IICCertificate(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='iic/certificates')
    def __str__(self):
        return self.name

class IICCommitee(models.Model):
    name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    designamtion = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class WomenCellCommitee(models.Model):
    name = models.CharField(max_length=300)
    department = models.CharField(max_length=300)
    designamtion = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Union(models.Model):
    name = models.CharField(max_length=300)
    about = models.TextField()

    def __str__(self) -> str:
        return self.name



class UnionCommitee(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(("Member Image"), upload_to="union/member")
    position = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    

class  CentralLibrary(models.Model):
    data = models.TextField(max_length=250)
    CHOICES = (("Vision", "Vision"), ("Mission", "Mission"),("about","about"))
    name = models.CharField(max_length=10, choices=CHOICES)
    class Meta:
        verbose_name = ("Central Library")
        verbose_name_plural = ("Central Library")

    def __str__(self):
        return self.name
    
class LibraryFaculty(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    role = models.CharField(max_length=10)
    order = models.IntegerField()
    def __str__(self):
        return self.faculty.full_name
    
class DigitalLibrary(models.Model):
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='CentralLibrary/DigitalLibrary/')
    def __str__(self):
        return self.title