from django import forms
from .models import *
class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name','contactsusr','phonenumber','projectname','account','password','balance','Cspname']
		labels = {'name':'公司名称',
                  'contactsusr':'联系人',
                  'phonenumber': '电话号码',
                  'projectname':'项目名称',
                  'account':'账号',
                  'password':'密码',
                  'balance':'余额',
                  'Cspname':'云服务商'
                  }

class ServerForm(forms.ModelForm):
    class Meta:
        model = Servers
        fields = ['roles','usage','pub_ipaddress','private_ipaddress','customer','password','cpu','mem','bandwidth','port','area','expiration_time','company']
        labels = {'roles':''}


