from django.db import models
from django.db.models.fields import TextField
from account import models as account_models

# Create your models here.
class Review(models.Model):
    # 작성자
    author = models.ForeignKey(account_models.CustomUser,on_delete=models.CASCADE, null=True)
    # 병원 이름
    hospital = models.CharField(max_length=100, null=True)
    # 리뷰 내용
    body = models.TextField()
    # 작성 날짜
    pub_date = models.DateTimeField()
    # 별점
    rating = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return self.body[:30]

    def starReview(self):
        if(self.rating == 0):
            return "☆☆☆☆☆(0)"
        elif(self.rating == 1):
            return "★☆☆☆☆(1)"
        elif(self.rating == 2):
            return "★★☆☆☆(2)"
        elif(self.rating == 3):
            return "★★★☆☆(3)"
        elif(self.rating == 4):
            return "★★★★☆(4)"
        else:
            return "★★★★★(5)"