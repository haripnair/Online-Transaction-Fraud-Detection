"""phone_mart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.publichome),
    path('publicheader/',views.publicheader),
    path('publichome/',views.publichome),
    path('coustomerheader/',views.coustomerheader),
    path('coustomerhome/',views.coustomerhome),
    path('adminheader/',views.adminheader),
    path('staffheader/',views.staffheader),
    path('staffhome/',views.staffhome),
    path('adminhome/',views.adminhome),
    path('addmodel/',views.addmodel),
    path('addmodelsave/',views.addmodelsave),
    path('viewaddmodel/',views.viewaddmodel),
    path('removemodel/<int:id>',views.removemodel),
    path('addproduct/',views.addproduct),
    path('addproductsave/',views.addproductsave),
    path('viewaddproduct/',views.viewaddproduct),
    path('removeproduct/<int:id>',views.removeproduct),
    path('updateproduct/<str:id>',views.updateproduct),
    path('viewaddproducts/',views.viewaddproducts),
    path('pupdate/<int:id>',views.pupdate),
    path('addaccount/',views.addaccount),
    path('addaccountsave/',views.addaccountsave),
    path('viewaddaccount/',views.viewaddaccount),
    path('removeaccount/<int:id>',views.removeaccount),
    path('login/',views.login),
    path('loginsave/',views.loginsave),
    path('coustomerreg/',views.coustomerreg),
    path('coustomersave/',views.coustomersave),
    path('searchmodel/',views.searchmodel),
    path('searchproduct/<str:id>',views.searchproduct),
    path('viewcustmodel/',views.viewcustmodel),
    path('viewcustproduct/<str:id>',views.viewcustproduct),
    path('custreview/<str:id>',views.custreview),
    path('reviewsave/<str:id>',views.reviewsave),
    path('order/<str:id>',views.order),
    path('ordersave/',views.ordersave),
    path('viewmodel/',views.viewmodel),
    path('viewproducts/<str:id>',views.viewproducts),
    path('viewreview/<str:id>',views.viewreview),
    path('allproduct/',views.allproduct),
    path('complaints/<str:id>',views.complaints),
    path('complaintsave/<str:id>',views.complaintsave),
    path('allproductz/',views.allproductz),
    path('viewcomplaints/<str:id>',views.viewcomplaints),
    path('vieworder/',views.vieworder),
    path('viewcoustomer/<str:id>',views.viewcoustomer),
    path('viewpayment/<str:id>',views.viewpayment),
    path('delivery/<str:id>',views.delivery),
    path('deliverysave/',views.deliverysave),
    path('viewcustorder/',views.viewcustorder),
    path('viewdelivery/<str:id>',views.viewdelivery),
    path('viewstaffall/',views.viewstaffall),
    path('viewproductall/',views.viewproductall),
    path('viewcustomerall/',views.viewcustomerall),
    path('logout/',views.publichome),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
