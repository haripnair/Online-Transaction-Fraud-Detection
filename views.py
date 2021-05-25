from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from app1.models import tbl_model
from app1.models import tbl_product
from app1.models import tbl_account
from app1.models import tbl_login
from app1.models import tbl_order
from app1.models import tbl_payment
from app1.models import tbl_review
from app1.models import tbl_delivery
from app1.models import tbl_complaint
from app1.models import tbl_coustomer
from django.http import HttpResponse
import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.
def admin(request):
    return render(request,"admin.html")
def publicheader(request):
    return render(request,"publicheader.html")
def userheader(request):
    return render(request,"userheader.html")
def coustomerheader(request):
    return render(request,"coustomerheader.html")
def coustomerhome(request):
    return render(request,"coustomerhome.html")
def adminheader(request):
    return render(request,"adminheader.html")
def staffheader(request):
    return render(request,"staffheader.html")
def staffhome(request):
    return render(request,"staffhome.html")
def publichome(request):
    return render(request,"publichome.html")
def adminhome(request):
    return render(request,"adminhome.html")
def addmodel(request):
    return render(request,"addmodel.html")
def addmodelsave(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        tc = tbl_model()
        tc.model_no=request.POST.get('modelno')
        tc.model_name=request.POST.get('name')
        tc.feature=request.POST.get('feature')
        tc.Photo=uploaded_file_url
        tc.save()
        tc.status="nv"
        tc.save()
        return render(request,'adminhome.html')
    else:
        return HttpResponse("invalid data type")
def viewaddmodel(request):
    std=tbl_model.objects.all()
    return render(request,'viewaddmodel.html',{'st':std})
def removemodel(request,id):
    std=tbl_model.objects.get(id=id)
    std.delete()
    return render(request,'adminhome.html')
def addproduct(request):
    std=tbl_model.objects.all()
    return render(request,"addproduct.html",{'st':std})
def addproductsave(request):
    if request.method == 'POST':
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(photo.name,photo)
        uploaded_file_url = fs.url(filename)
        tc = tbl_product()
        tc.model_no=request.POST.get('modelno')
        tc.product_name=request.POST.get('name')
        tc.description=request.POST.get('description')
        tc.size=request.POST.get('size')
        tc.colour=request.POST.get('colour')
        tc.price=request.POST.get('price')
        tc.stock=request.POST.get('stock')
        tc.Photo=uploaded_file_url
        tc.save()
        tc.status="nv"
        tc.product_id="null"
        tc.save()
        tid="product_0"+str(tc.id)
        tc.product_id=tid
        tc.save()
        return render(request,'adminhome.html')
    else:
        return HttpResponse("invalid data type")
def viewaddproduct(request):
    std=tbl_product.objects.all()
    return render(request,'viewaddproduct.html',{'st':std})
def removeproduct(request,id):
    std=tbl_product.objects.get(id=id)
    std.delete()
    return render(request,'adminhome.html')
def updateproduct(request,id):
    data=tbl_product.objects.get(product_id=id)
    data1=tbl_product.objects.get(product_id=data.product_id)
    return render(request,'updateproduct.html',{'da':data,'st':data1})
def viewaddproducts(request):
    std=tbl_product.objects.all()
    return render(request,'viewaddproducts.html',{'st':std})
def pupdate(request,id):
    std=tbl_product.objects.get(id=id)
    if request.method=="POST":
        std.model_no=request.POST.get('modelno')
        std.product_name=request.POST.get('name')
        std.description=request.POST.get('description')
        std.size=request.POST.get('size')
        std.colour=request.POST.get('colour')
        std.price=request.POST.get('price')
        std.stock=request.POST.get('stock')
        std.save()
        return render(request,'adminhome.html')
    else:
        return HttpResponse("invalid data type")
def addaccount(request):
    std=tbl_account.objects.all()
    return render(request,"addaccount.html",{'st':std})
def addaccountsave(request):
    if request.method == 'POST':
        data=tbl_account()
        data.name=request.POST.get('name')
        data.account_date=request.POST.get('acdate')
        data.roll=request.POST.get('roll')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.save()
        data.account_id="null"
        data.status="nv"
        data.save()
        tid="account_0"+str(data.id)
        data.account_id=tid
        data.save()
        lg=tbl_login()
        lg.user_id=data.account_id
        lg.password=data.phone
        lg.category="staff"
        lg.save()
        return render(request,"adminhome.html")
    else:
        return HttpResponse("invalid data type")
def viewaddaccount(request):
    std=tbl_account.objects.all()
    return render(request,'viewaddaccount.html',{'st':std})
def removeaccount(request,id):
    std=tbl_account.objects.get(id=id)
    std.delete()
    return render(request,'adminhome.html')
def searchmodel(request):
    std=tbl_model.objects.all()
    return render(request,"searchmodel.html",{'st':std})
def searchproduct(request,id):
    std=tbl_product.objects.filter(model_no=id)
    return render(request,'searchproduct.html',{'st':std})
def login(request):
    return render(request,"login.html")
def loginsave(request):
    if request.method == 'POST':
        data = tbl_login.objects.all()
        un=request.POST.get('user_id')
        pwd=request.POST.get('password')
        
        flag=0
            
        for da in data:
            if un == da.user_id and pwd == da.password:
                type=da.category
                request.session['uid']=un
                flag = 1 
                if type=="admin":
                    return render(request,"adminhome.html")
                elif type=="public":
                    return render(request,"publichome.html")
                elif type=="coustomer":
                    return render(request,"coustomerhome.html")
                elif type=="staff":
                    return render(request,"staffhome.html")
                else:
                    return HttpResponse("Invalid acct type")
        if flag == 0:
		            return HttpResponse("Invalid user")
def coustomerreg(request):
    return render(request,"coustomerreg.html")
def coustomersave(request):
    if request.method == 'POST':
        data=tbl_coustomer()
        data.name=request.POST.get('name')
        data.address=request.POST.get('address')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.save()
        data.coustomer_id="null"
        data.save()
        tid="coustomer_0"+str(data.id)
        data.coustomer_id=tid
        data.save()
        lg=tbl_login()
        lg.user_id=data.coustomer_id
        lg.password=data.phone
        lg.category="customer"
        lg.save()
        return render(request,"publichome.html")
    else:
        return HttpResponse("invalid data type")
def viewcustmodel(request):
    std=tbl_model.objects.all()
    return render(request,"viewcustmodel.html",{'st':std})
def viewcustproduct(request,id):
    std=tbl_product.objects.filter(model_no=id)
    return render(request,'viewcustproduct.html',{'st':std})
def custreview(request,id):
    return render(request,"custreview.html",{'st':id})
def reviewsave(request,id):
    if request.method == 'POST':
        tf=request.session['uid']
        data=tbl_review()
        data.reviews=request.POST.get('reviews')
        data.review_date=request.POST.get('rvdate')
        data.review_id="null"
        data.coustomer_id=tf
        data.product_id=id
        data.save()
        tid="review_0"+str(data.id)
        data.review_id=tid
        data.save()
        return render(request,"coustomerhome.html")
    else:
        return HttpResponse("invalid data type")
def order(request,id):
    data=tbl_product.objects.get(product_id=id)
    data1=tbl_product.objects.get(product_id=data.product_id)
    td=request.session['uid']
    return render(request,'order.html',{'u':td,'da':data,'da1':data1})
def ordersave(request):
    if request.method == 'POST':
        data=tbl_order()
        data.product_id=request.POST.get('product_id')
        data.quantity=request.POST.get('quantity')
        q=int(request.POST.get('quantity'))
        a=int(request.POST.get('amount'))
        tot=int(a*q)
        data.amount=request.POST.get('amount')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        data.order_date= time1
        data.order_id="null"
        data.status="nv"
        data.coustomer_id=request.session['uid']
        data.save()
        tid="order_0"+str(data.id)
        data.order_id=tid
        data.save()
        tf=tbl_payment()
        tf.bank_name=request.POST.get('bank_name')
        tf.cardtype=request.POST.get('cardtype')
        tf.card_no=request.POST.get('card_no')
        now = datetime.datetime.now()
        time1 = now.strftime("%Y-%m-%d")
        tf.payment_date= time1
        tf.amount=request.POST.get('amount')
        tf.order_id=request.POST.get('order_id')
        tf.payment_id="null"
        tf.status="nv"
        tf.order_id=data.order_id
        tf.total=tot
        tf.save()
        tid="pay_0"+str(tf.id)
        tf.payment_id=tid
        tf.save()
        return render(request,"coustomerhome.html")
    else:
        return HttpResponse("invalid data type")
def viewmodel(request):
    std=tbl_model.objects.all()
    return render(request,"viewmodel.html",{'st':std})
def viewproducts(request,id):
    std=tbl_product.objects.filter(model_no=id)
    return render(request,'viewproducts.html',{'st':std})
def viewreview(request,id):
    std=tbl_review.objects.filter(product_id=id)
    return render(request,'viewreview.html',{'st':std})
def allproduct(request):
    std=tbl_product.objects.all()
    return render(request,"allproduct.html",{'st':std})
def complaints(request,id):
    return render(request,"complaints.html",{'st':id})
def complaintsave(request,id):
    if request.method == 'POST':
        tf=request.session['uid']
        data=tbl_complaint()
        data.complaints=request.POST.get('complaints')
        data.complaint_date=request.POST.get('cmdate')
        data.complaint_id="null"
        data.coustomer_id=tf
        data.product_id=id
        data.save()
        tid="complaint_0"+str(data.id)
        data.complaint_id=tid
        data.save()
        return render(request,"coustomerhome.html")
def allproductz(request):
    std=tbl_product.objects.all()
    return render(request,"allproductz.html",{'st':std})
def viewcomplaints(request,id):
    std=tbl_complaint.objects.filter(product_id=id)
    return render(request,'viewcomplaints.html',{'st':std})
def vieworder(request):
    std=tbl_order.objects.filter(status='nv')
    return render(request,"vieworder.html",{'st':std})
def viewcoustomer(request,id):
    std=tbl_coustomer.objects.filter(coustomer_id=id)
    return render(request,'viewcoustomer.html',{'st':std})
def viewpayment(request,id):
    std=tbl_payment.objects.filter(order_id=id)
    return render(request,'viewpayment.html',{'st':std})
def delivery(request,id):
    data=tbl_order.objects.get(order_id=id)
    return render(request,"delivery.html",{'d':data})
def deliverysave(request):
    if request.method == 'POST':
        oid=request.POST.get('order_id')
        da=tbl_order.objects.get(order_id=oid)
        p=da.product_id
        q=int(da.quantity)
        data2=tbl_product.objects.get(product_id=p)
        s=int(data2.stock)
        n=int(s-q)
        if n<0:
            return HttpResponse("out of stock")
        else:

            da.status="process"
            da.save()
            
            data2.stock=n
            data2.save()
            data=tbl_delivery()
            data.order_id=request.POST.get('order_id')
            data.delivery_date=request.POST.get('dvdate')
            data.time=request.POST.get('time')
            data.delivery_id="null"
            data.status="process"
            data.save()
            tid="deliv"+str(data.id)
            data.delivery_id=tid
            data.save()
            return render(request,"staffhome.html")
def viewcustorder(request):
    td=request.session['uid']
    data=tbl_order.objects.filter(coustomer_id=td)
    return render(request,"viewcustorder.html",{'st':data})
def viewdelivery(request,id):
    std=tbl_delivery.objects.filter(order_id=id)
    return render(request,'viewdelivery.html',{'st':std})
def viewstaffall(request):
    std=tbl_account.objects.all()
    return render(request,'viewstaffall.html',{'st':std})
def viewproductall(request):
    std=tbl_product.objects.all()
    return render(request,'viewproductall.html',{'st':std})
def viewcustomerall(request):
    std=tbl_coustomer.objects.all()
    return render(request,'viewcustomerall.html',{'st':std})

    
    
