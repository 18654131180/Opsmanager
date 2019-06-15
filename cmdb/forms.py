from django import forms
from .models import *
class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name','contactsusr','phonenumber','projectname','account','password','balance','Cspname','group']
		labels = {'name':'公司名称',
                  'contactsusr':'联系人',
                  'phonenumber': '电话号码',
                  'projectname':'项目名称',
                  'account':'账号',
                  'password':'密码',
                  'balance':'余额',
                  'Cspname':'云服务商',
                  'group':'项目组'
                  }

class ServerForm(forms.ModelForm):
    class Meta:
        model = Servers
        fields = ['roles','usage','pub_ipaddress','private_ipaddress','customer','password','cpu','mem','bandwidth','port','area','expiration_time','company']
        labels = {'roles':'角色','usage':'用途','pub_ipaddress':'公网','private_ipaddress':'私网','customer':'月费用','password':'密码','cpu':'CPU','mem':'内存','bandwidth':'带宽','port':'远程端口','area':'地区','expiration_time':'到期时间','company':'所属公司'}














