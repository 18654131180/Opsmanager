from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    # 编辑公司
    url(r'edit_company/(?P<company_id>\d+)/$', views.edit_company, name='edit_company'),
    # 增加公司
    url(r'new_company', views.new_company, name='new_company'),
     # 主页
    url(r'^$',views.index,name='index'),
    # 公司展示
    url(r'company',views.showcompanys,name='company'),

    # 服务器展示
    url(r'server',views.showservers,name='server'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
