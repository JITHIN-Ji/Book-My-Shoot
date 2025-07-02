from django.db import models


# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
class profile(models.Model):
    name=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    since=models.CharField(max_length=100)
    keylicense=models.CharField(max_length=100)


class user(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    log=models.ForeignKey(login,on_delete=models.CASCADE)

class category(models.Model):
    category=models.CharField(max_length=100)
    
class service(models.Model):
    service=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    details=models.CharField(max_length=100)
    catgor=models.ForeignKey(category,on_delete=models.CASCADE)

class booking(models.Model):
    venue=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    ser=models.ForeignKey(service,on_delete=models.CASCADE)
    use_id=models.ForeignKey(user,on_delete=models.CASCADE)

class payment(models.Model):
    amount=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    book_id=models.ForeignKey(booking,on_delete=models.CASCADE)

class uploads(models.Model):
    ufile=models.CharField(max_length=100)
    utype=models.CharField(max_length=100)
    booking=models.ForeignKey(booking,on_delete=models.CASCADE)

class works(models.Model):
    files=models.CharField(max_length=100)
    utype=models.CharField(max_length=100)

class feedback(models.Model):
    feedback1=models.CharField(max_length=500)
    date=models.CharField(max_length=100)
    feedback_user=models.ForeignKey(user,on_delete=models.CASCADE)





