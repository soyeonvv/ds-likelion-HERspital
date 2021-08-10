from django.db import models
from account import models as account_models

# Create your models here.
class Community(models.Model):
    # 제목
    title = models.CharField(max_length=200)
    # 공개설정
    publicSetting = models.BooleanField()
    # 비밀번호
    password_Post = models.IntegerField(blank=True, null=True)
    # 연령 태그
    age_tag = models.CharField(max_length=100)
    # 사진
    image = models.ImageField(upload_to = "community/", blank=True, null=True)
    # 내용
    body = models.TextField()
    # 작성 날짜
    pub_date = models.DateTimeField()
    # 작성자 <- 익명으로 표시되지만, '자신이 쓴 글 보기'와 '성별 표시'를 위해서 글 작성자의 정보를 저장해야 함
    author = models.ForeignKey(account_models.CustomUser,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def summary(self): #제목 글자수가 길면 끊어서 보여주도록
        return self.title[:30]

class Expert(models.Model):
    # 제목
    title = models.CharField(max_length=200)
    # 공개설정
    publicSetting = models.BooleanField()
    # 비밀번호
    password_Post = models.IntegerField(blank=True, null=True)
    # 연령 태그
    age_tag = models.CharField(max_length=100)
    # 사진
    image = models.ImageField(upload_to = "community/", blank=True, null=True)
    # 내용
    body = models.TextField()
    # 작성 날짜
    pub_date = models.DateTimeField()
    # 작성자 <- 익명으로 표시되지만, '자신이 쓴 글 보기'와 '성별 표시'를 위해서 글 작성자의 정보를 저장해야 함
    author = models.ForeignKey(account_models.CustomUser,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def summary(self): #제목 글자수가 길면 끊어서 보여주도록
        return self.title[:30]
<<<<<<< HEAD
=======

class ExpertRe(models.Model):
    #작성자(전문의) 외래키
    author = models.ForeignKey(account_models.CustomUser, on_delete=models.CASCADE, null=True)
    #질문글id 외래키
    # post = models.ForeignKey(Expert, on_delete=models.CASCADE, null=True)
    postId = models.CharField(max_length=100)
    #좋아요 개수
    thumbsUp = models.IntegerField(blank=True, default=0, null=True)
    # 답변 내용
    body = models.TextField()
    # 작성 날짜
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.body[:30]

class Reply(models.Model):
    # 내용
    body = models.TextField()
    # 작성 날짜
    pub_date = models.DateTimeField()
>>>>>>> f4e1960f4566f5330a5a8e5cb6ad0365223a61f2
