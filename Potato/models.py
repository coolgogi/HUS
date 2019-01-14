from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, default = "제목없음")
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    contents = models.TextField()
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('board2:postDetail', kwargs={"pk":self.pk})
        # return reverse('board2:postList') //list로 돌아가려고 할 때