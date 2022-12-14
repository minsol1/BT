from django.db import models
from accounts.models import User
# Create your models here.

class Buy(models.Model):
    CATEGORY_CHOICES = [(0,'식재료'),(1,'생필품'),(2,'OTT'),(3,'배달')]
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False,
                                 null=False,)
    writeDate = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(blank=False,
                                 null=False,)
    category = models.IntegerField(choices=CATEGORY_CHOICES,
                                 blank=False,
                                 null=False,
                                 default=0)
    wpeople = models.IntegerField(blank=False, null=False,)#모집인원
    people = models.IntegerField(null=True,default=1)# 모인사람 
    price = models.IntegerField(blank=False,
                                 null=False,)
    location=models.CharField(max_length=300)
    photo = models.ImageField(blank=True,null=True,upload_to='images/')
    lat = models.FloatField(default=0) #위도
    long = models.FloatField(default=0) #경도
    ID = models.ForeignKey(User,  on_delete=models.CASCADE,blank=False,
                                 null=False,
                                 default="")# 글쓴이 
    like_count = models.PositiveIntegerField(default=0)    
    join_count = models.PositiveIntegerField(default=1) # 참가 신청한 사람 수 
    
    check_chat = models.BooleanField(default = False) # 채팅방 생성되었는지 확인

    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def summaryTitle(self):
        if len(self.title)>15:
            sBody = self.title[:15]+'...'
        else: sBody = self.title
        return sBody
        

    def summary(self):
        if len(self.body)>30:
            sBody = self.body[:30]+'...더보기'
        else: sBody = self.body
        return sBody
        
# class Bookmarks(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Buy, on_delete=models.CASCADE)