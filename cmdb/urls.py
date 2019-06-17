from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    # 编辑公司
    url(r'edit_company/(?P<company_id>\d+)/$', views.edit_company, name='edit_company'),
    # 展示公司详情
    url(r'show_company/(?P<company_id>\d+)/$', views.show_company, name='show_company'),
    # 增加公司
    url(r'new_company', views.new_company, name='new_company'),
    # 删除公司
    url(r'del_company/(?P<company_id>\d+)/$', views.del_company, name='del_company'),
    #编辑服务器
    url(r'edit_server/(?P<server_id>\d+)/$',views.edit_server,name='edit_server'),
    #增加服务器
    url(r'new_server/',views.new_server,name='new_server'),
    #删除服务器
    url(r'del_server/(?P<server_id>\d+)/$',views.del_server,name='del_server'),
    # 主页
    url(r'^$',views.index,name='index'),
    # 公司展示
    url(r'company',views.showcompanys,name='company'),
    # 服务器展示
    url(r'server',views.showservers,name='server'),

]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
