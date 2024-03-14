from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Rto(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100,default='')
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class Policestation(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    pin = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    siname  = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class Scrapdealer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class User(models.Model):
    username = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    photo = models.CharField(max_length=300)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    aadhar_no = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login,on_delete=models.CASCADE)


class Vehicle(models.Model):
    USER = models.ForeignKey(User,on_delete=models.CASCADE)
    RTO = models.ForeignKey(Rto,on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    reg_date = models.DateField()
    reg_place = models.CharField(max_length=100)
    Vehicle_type = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    engine_number = models.CharField(max_length=100)
    chase_number = models.CharField(max_length=100)
    year_of_manufacturing = models.CharField(max_length=100)
    month_of_manufacturing = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Activity(models.Model):
    VEHICLE = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    POLICE = models.ForeignKey(Policestation,on_delete=models.CASCADE)
    date = models.DateField()
    activity = models.CharField(max_length=100)


class Request(models.Model):
    requestid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)