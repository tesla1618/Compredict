from django.db import models
from django.utils import timezone
import os
# from taggit.managers import TaggableManager
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.


class Processor(models.Model):
    pID = models.AutoField(primary_key=True)
    pBrand = models.CharField(max_length=260)
    pName = models.CharField(max_length=260)
    pGen = models.CharField(max_length=260)
    pCore = models.IntegerField()
    pThread = models.IntegerField()
    pSpeed = models.IntegerField()
    pigpu = models.BooleanField()
    pPrice = models.IntegerField()
    pThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.pBrand) +" "+ str(self.pName) + " " +str(self.pGen)
        return totTitle


class Ram(models.Model):
    rID = models.AutoField(primary_key=True)
    rBrand = models.CharField(max_length=260)
    rName = models.CharField(max_length=260)
    rCap = models.IntegerField()
    rSpeed = models.IntegerField()
    rPrice = models.IntegerField()
    rThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.rBrand) +" "+ str(self.rName) + " " +str(self.rCap) + "GB"
        return totTitle


class SSD(models.Model):
    sID = models.AutoField(primary_key=True)
    sBrand = models.CharField(max_length=260)
    sName = models.CharField(max_length=260)
    sCap = models.IntegerField()
    sInterface = models.CharField(max_length=260)
    sPrice = models.IntegerField()
    sThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.sBrand) +" "+ str(self.sName) + " " +str(self.sCap) + "GB"
        return totTitle


class HDD(models.Model):
    hID = models.AutoField(primary_key=True)
    hBrand = models.CharField(max_length=260)
    hName = models.CharField(max_length=260)
    hCap = models.IntegerField()
    hPrice = models.IntegerField()
    hThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.hBrand) +" "+ str(self.hName) + " " +str(self.hCap) + "GB"
        return totTitle


class GPU(models.Model):
    gID = models.AutoField(primary_key=True)
    gBrand = models.CharField(max_length=260)
    gName = models.CharField(max_length=260)
    # gGen = models.CharField(max_length=260)
    # pCore = models.IntegerField()
    # pThread = models.IntegerField()
    gCap = models.IntegerField()
    # pigpu = models.BooleanField()
    gPrice = models.IntegerField()
    gThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.gBrand) +" "+ str(self.gName) + " " +str(self.gCap) + "GB"
        return totTitle


class Mobo(models.Model):
    mID = models.AutoField(primary_key=True)
    mBrand = models.CharField(max_length=260)
    mName = models.CharField(max_length=260)
    # gGen = models.CharField(max_length=260)
    # pCore = models.IntegerField()
    # pThread = models.IntegerField()
    # gCap = models.IntegerField()
    isAmdorIntel = models.BooleanField()        # 0 for Intel 1 for AMD
    mPrice = models.IntegerField()
    mThumb = models.ImageField()

    def __str__(self):
        totTitle = str(self.mBrand) +" "+ str(self.mName)
        return totTitle


