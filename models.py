from django.db import models

# Create your models here.
class User(models.Model):
  UserId = models.IntegerField(primary_key = True)
  Email = models.EmailField(max_length=70,blank=True,unique=True)
  Password = models.CharField(max_length=50)

class History(models.Model):
  HistoryId = models.IntegerField(primary_key = True)
  History = models.CharField(max_length=500)
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Blogger(models.Model):
  BloggerId = models.IntegerField(primary_key = True)
  Bio = models.CharField(max_length=1000)
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Reader(models.Model):
  ReaderId = models.IntegerField(primary_key = True)
  Interest = models.CharField(max_length=1000)
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class Category(models.Model):
  CategoryId = models.IntegerField(primary_key = True)
  CategoryName = models.CharField(max_length=50)
  Description = models.CharField(max_length=500)

class BlogPost(models.Model):
  BlogId = models.IntegerField(primary_key = True)
  Title = models.CharField(max_length=50)
  DatePosted = models.DateTimeField()
  Likes = models.IntegerField()
  Comments = models.IntegerField()
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  CategoryId = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

class Like(models.Model):
  LikeId = models.IntegerField(primary_key = True)
  DateLiked = models.DateTimeField()
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  BlogID = models.ForeignKey(BlogPost, null=True, on_delete=models.CASCADE)

class Comment(models.Model):
  CommentId = models.IntegerField(primary_key = True)
  DatePosted = models.DateTimeField()
  Content = models.CharField(max_length=50)
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  BlogID = models.ForeignKey(BlogPost, null=True, on_delete=models.CASCADE)

class Community(models.Model):
  CommunityId = models.IntegerField(primary_key = True)
  CommunityName = models.CharField(max_length=50)
  Description = models.CharField(max_length=500)
  NumberOfMembers = models.IntegerField()

class UserCommunity(models.Model):
  JoinId = models.IntegerField(primary_key = True)
  UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  CommunityID = models.ForeignKey(Community, null=True, on_delete=models.CASCADE)
