from django.db import models

# Create your models here.

# It means Topic is a table in database and top_name is column in the table
class Topic(models.Model):
    top_name = models.CharField(max_length =256)


    def __str__(self):
        return self.top_name


# it means it webpage is a table and all the variables in the class are table column
class Webpage (models.Model):

    topic = models.ForeignKey(Topic,default=0,on_delete=models.CASCADE,)
    name = models.CharField(max_length = 264, unique = True)
    url = models.URLField(unique = True)


    def __str__(self):
        return self.name;



class AccessRecord(models.Model):
     name = models.ForeignKey(Webpage,default=0, on_delete=models.CASCADE)
     date = models.DateField()


     def __str__(self):
        return str(self.date)



class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=264, unique=True)
