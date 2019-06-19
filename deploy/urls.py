from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    #显示公司下需要部署的服务器详情
    # url(r'detail_company/(?P<company_id>\d+)/$', views.detail_company, name='detail_company'),
    # 主页
    url(r'^$',views.deploy,name='deploy'),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

