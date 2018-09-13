from django.db import models

# Create your models here.
class Users(models.Model):
	username=models.CharField(max_length=100)
	email=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	def __str__(self):
		return "Users: {}".format(self.username)

class Books(models.Model):
	book_title=models.CharField(max_length=100)
	book_description=models.TextField(blank=False)
	book_author=models.CharField(max_length=100)
	book_pages=models.IntegerField(blank=False)
	book_category=models.CharField(max_length=100)
	book_front=models.CharField(max_length=500)
	book_pdf=models.CharField(max_length=500)
	book_user=models.ForeignKey(Users, related_name="books",on_delete=models.CASCADE)
	def __self__(self):
		return "Cards: {}".format(self.book_title)