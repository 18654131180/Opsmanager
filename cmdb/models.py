from django.db import models
from django.contrib.auth.models import User
from dateutil.parser import parse
import time
daytime=time.strftime('%Y-%m-%d',time.localtime(time.time()))
class Csp(models.Model):
    """定义云服务商"""
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=40,verbose_name='云服务商名称')
    remark = models.CharField(max_length=50,verbose_name='备注')
    class Meta:
        verbose_name="云服务商"
        verbose_name_plural ="云服务商"
    def __str__(self):
        "返回服务商名称"
        return self.name

class Group(models.Model):
    name=models.CharField(max_length=30,verbose_name='组名称')
    remark = models.CharField(max_length=50, verbose_name='备注')
    class Meta:
        verbose_name_plural ="项目组"
    def __str__(self):
        return self.name

class Company(models.Model):
    """定义公司名称"""
    name=models.CharField(max_length=25,verbose_name='公司名称',unique=True)
    contactsusr=models.CharField(max_length=10,verbose_name='联系人')
    phonenumber=models.IntegerField(verbose_name='联系人手机号')
    projectname=models.CharField(max_length=20,verbose_name='项目名')
    account=models.CharField(max_length=30,verbose_name='登陆账号')
    password=models.CharField(max_length=30,verbose_name='登陆密码')
    balance=models.FloatField(max_length=10,verbose_name='账户余额')

    Cspname=models.ForeignKey(Csp)
    group=models.ForeignKey(Group)
    class Meta:
        verbose_name_plural ="公司"
    def __str__(self):
        "返回公司名称"
        return self.name

class Servers(models.Model):
    """定义服务器属性"""
    roles=models.CharField(max_length=20,verbose_name='服务器角色')
    usage=models.CharField(max_length=20,verbose_name='服务器用途')
    pub_ipaddress=models.GenericIPAddressField(verbose_name='公网地址')
    private_ipaddress=models.GenericIPAddressField(verbose_name='私网地址')
    customer = models.FloatField(max_length=10, verbose_name='月费用')
    password = models.CharField(max_length=30, verbose_name='服务器密码')
    cpu=models.IntegerField(verbose_name='CPU核数')
    mem=models.IntegerField(verbose_name='内存大小')
    bandwidth=models.IntegerField(verbose_name='带宽')
    port=models.IntegerField(verbose_name='远程端口')
    area=models.CharField(max_length=10,verbose_name='地区')
    expiration_time=models.DateField(verbose_name='到期时间')
    company=models.ForeignKey(Company,default=1)

#定义一个方法，判断数据库日期比当前日期是否在5天以内，在模板里可以直接以.is_expiration做条件判断
    @property
    def is_expiration(self):
        if (parse(str(self.expiration_time)) - parse(daytime)).days >= 5:
            return True
    class Meta:
        verbose_name_plural = "服务器"
    def __str__(self):
        return self.roles



