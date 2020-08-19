from django.shortcuts import render,redirect
from django.db.utils import IntegrityError
from django.core.paginator import Paginator
from django.contrib import messages
from e_mall.models import ProductsSales,Admin,Users,Products

def showIndex(request):
    pro = Products.objects.filter(status="active")
    pg = Paginator(pro, 2)
    page_number = request.GET.get("page_number", 1)
    page = pg.page(page_number)
    r = request.COOKIES
    l = dict(r)
    le=len(l)
    if le==1:
        le=0
        return render(request, "index.html", {"page": page, "length": le})
    else:
        le-=1
        return render(request,"index.html",{"page":page,"length":le})

def admin_login(request):
    r = request.COOKIES
    l = dict(r)
    le = len(l)
    if le == 1:
        le = 0
        return render(request, "admin_login.html", {"length": le})
    else:
        le -= 1
        return render(request, "admin_login.html", {"length": le})

def admin_verify(request):
    un=request.POST.get("uname")
    up=request.POST.get("upass")
    try:
        Admin.objects.get(username=un,password=up)
        return redirect('admin_home')
    except Admin.DoesNotExist:
        messages.error(request, "Invalid Credentials")
        return redirect('admin_login')


def admin_home(request):
    return render(request,"admin_home.html")


def admin_products(request):
    res=Products.objects.all()
    print(res[0].photo.url)
    pg=Paginator(res,5)
    page_no=request.GET.get("page_no",1)
    page=pg.page(page_no)
    return render(request, "admin_products.html", {"data": page})

def save_product(request):
    na=request.POST.get("pname")
    pr=request.POST.get("pprice")
    qty=request.POST.get("pqty")
    desc=request.POST.get("desc")
    img=request.FILES.get("pimg")
    st="active"
    Products(name=na,price=pr,quantity=qty,description=desc,photo=img,status=st).save()
    messages.success(request,"Successfully Added")
    return redirect('admin_products')


def register(request):
    r = request.COOKIES
    l = dict(r)
    le = len(l)
    if le == 1:
        le = 0
        return render(request, "register.html", {"length": le})
    else:
        le -= 1
        return render(request, "register.html", {"length": le})


def register_user(request):
    name=request.POST.get("name")
    email=request.POST.get("email")
    contact = request.POST.get("contactno")
    gender=request.POST.get("r1")
    uname=request.POST.get("username")
    password=request.POST.get("password")
    status="Pending"
    try:
        Users(name=name,email=email,contactno=contact,gender=gender,username=uname,password=password,status=status).save()
        return render(request,"register.html",{"mess":"Successfully Registered"})
    except IntegrityError:
        return render(request,"register.html",{"mess1":"Data Already Exist"})



def admin_all_users(request):
    return render(request,"admin_all_users.html")

def admin_see_users(request):
    c1 = request.POST.get("c1")
    c2 = request.POST.get("c2")
    c3 = request.POST.get("c3")
    if c1==None:
        c1=""
    if c2==None:
        c2=""
    if c3==None:
        c3=""
    print(c1,c2,c3)
    if c1=="Pending" and c2=="" and c3=="":
        res1=Users.objects.filter(status=c1)
        res11=reversed(res1)
        return render(request,"admin_see_users.html",{"data1":res11})
    elif c2=="Approved" and c1=="" and c3=="":
        res2 = Users.objects.filter(status=c2)
        res22=reversed(res2)
        return render(request, "admin_see_users.html", {"data2": res22})
    elif c3=="Declined" and c1=="" and c2=="":
        res3 = Users.objects.filter(status=c3)
        res33=reversed(res3)
        return render(request, "admin_see_users.html", {"data3": res33})
    elif c1=="Pending" and c2=="Approved" and c3=="":
        res1 = Users.objects.filter(status=c1)
        res2 = Users.objects.filter(status=c2)
        rev1=reversed(res1)
        rev2=reversed(res2)
        return render(request, "admin_see_users.html", {"data1": rev1,"data2":rev2})
    elif c1=="" and c2=="Approved" and c3=="Declined":
        res2 = Users.objects.filter(status=c2)
        res3 = Users.objects.filter(status=c3)
        rev2=reversed(res2)
        rev3=reversed(res3)
        return render(request, "admin_see_users.html", {"data2": rev2,"data3":rev3})
    elif c1=="Pending" and c2=="" and c3=="Declined":
        res1 = Users.objects.filter(status=c1)
        res3 = Users.objects.filter(status=c3)
        rev1=reversed(res1)
        rev3=reversed(res3)
        return render(request, "admin_see_users.html", {"data1": rev1,"data3":rev3})
    elif c1=="Pending" and c2=="Approved" and c3=="Declined":
        res1 = Users.objects.filter(status=c1)
        res2 = Users.objects.filter(status=c2)
        res3 = Users.objects.filter(status=c3)
        rev1=reversed(res1)
        rev2=reversed(res2)
        rev3=reversed(res3)
        return render(request, "admin_see_users.html", {"data1": rev1,"data2":rev2,"data3":rev3})
    else:
        return render(request,"admin_see_users.html")


def approve_user(request):
    id=request.POST.get("approve")
    res=Users.objects.filter(id=id)
    res.update(status="Approved")
    return render(request,'admin_all_users.html')

def decline_user(request):
    id=request.POST.get("decline")
    res=Users.objects.filter(id=id)
    res.update(status="Declined")
    return render(request,'admin_all_users.html')


def admin_update_product(request):
    no=request.POST.get("update")
    res=Products.objects.filter(no=no)
    return render(request,"admin_update_product.html",{"data":res})


def admin_save_product(request):
    no=request.POST.get("no")
    na = request.POST.get("pname")
    pr = request.POST.get("pprice")
    qty = request.POST.get("pqty")
    img = request.FILES.get("pimg")
    desc=request.POST.get("desc")
    st = "active"
    if img==None:
        a=Products.objects.get(no=no)
        img=a.photo
    try:
        res = Products.objects.get(no=no)
        res.no=no
        res.name=na
        res.price=pr
        res.quantity=qty
        res.status=st
        res.photo=img
        res.description=desc
        res.save()
        messages.success(request, "Successfully Updated")
        return redirect('admin_products')
    except IntegrityError:
        return render(request,"admin_products.html",{"mess":"Already Available"})


def admin_deactive_product(request):
    no = request.POST.get("deactive")
    res = Products.objects.get(no=no)
    if res.status=="inactive":
        res.status = "active"
    else:
        res.status="inactive"
    res.save()
    return redirect('admin_products')


def user_login(request):
    r = request.COOKIES
    l = dict(r)
    le = len(l)
    if le == 1:
        le = 0
        return render(request, "user_login.html", {"length": le})
    else:
        le -= 1
        return render(request, "user_login.html", {"length": le})


def validate_user(request):
    uname=request.POST.get("uname")
    upass=request.POST.get("upass")
    try:
        res = Users.objects.get(username=uname,status="Approved")
        if res.username == uname:
            if res.password == upass:
                request.session["user"]=uname
                return render(request, "user_login_successfully.html", {"data1": "Welcome " + uname,"data2":Products.objects.filter(status="active")})
            else:
                return render(request, "user_login.html", {"data1":"Invalid Password"})
        else:
            return render(request, "user_login.html", {"data": "Invalid Username"})
    except:
        return render(request, "user_login.html", {"data": "Invalid Credentials"})


def user_forget_password(request):

    return render(request,"user_forget_password.html")


def user_reset_password(request):
    email=request.POST.get("email")
    newpass=request.POST.get("newpass")
    conpass=request.POST.get("conpass")
    try:
        res = Users.objects.get(email=email,status="Approved")
        if newpass==conpass:
            res.password=conpass
            res.save()
            return render(request, "user_forget_password.html", {"data1": "Reset Successfully. Please Login"})
        else:
            return render(request, "user_forget_password.html", {"data2": "New And Confirm Password Must Be Same"})

    except:
        return render(request,"user_forget_password.html",{"data":"Invalid Email"})


def user_main(request):
    pro = Products.objects.filter(status="active")
    pg = Paginator(pro, 4)
    page_num = request.GET.get("page_number", 1)
    page = pg.page(page_num)
    return render(request, "user_login_successfully.html", {"data": page})

def cart_items(request):
    r = request.COOKIES
    l = dict(r)
    le = len(l)
    if le == 2:
        le = 1
        return render(request, "cart_items.html", {"length": le,"data":request.COOKIES})
    else:
        le -= 1
        return render(request, "cart_items.html", {"length": le,"data":request.COOKIES})


def save_cart_items(request):
    no=request.GET.get("no")
    name=request.GET.get("name")
    response=redirect('main')
    response.set_cookie(no,name)
    return response

def del_cart(request):
    k=request.GET.get("key")
    response=redirect('cart_items')
    response.delete_cookie(k)
    return response


def buyproduct(request):
    if request.session.has_key("user"):
        idno=request.GET.get("idno")
        pro=Products.objects.filter(no=idno)
        return render(request,"buyproduct.html",{'data':pro})
    else:
        return redirect('user_login')


def place_order(request):
    if request.session.has_key("user"):
        usr=request.session.get("user")
        print(usr)
        us=Users.objects.get(username=usr)
        usrid=us.id
        idno=request.POST.get("idno")
        qty=request.POST.get("qty")
        price=request.POST.get("price")
        t_bill=request.POST.get("t_bill")
        ps=ProductsSales(qty=qty,total_bill=t_bill)
        ps.save()
        ps.product_id.set(idno)
        ps.user_id.set(str(usrid))
        return render(request,"payment_success.html",{"success":"Payment Successfull , Order Placed , Thankyou"})
    else:
        return redirect('user_login')


def productdetails(request):
    idno=request.GET.get("idno")
    pr=Products.objects.filter(no=idno)
    return render(request,"productdetails.html",{"details":pr})


def userorders(request):
    if request.session.has_key("user"):
        usr = request.session.get("user")
        print(usr)
        us = Users.objects.get(username=usr)
        usrid = us.id
        ps=ProductsSales.objects.filter(user_id=usrid)
        return render(request,"userorders.html",{"orders":ps})
    else:
        return redirect('user_main')


def userlogout(request):
    del request.session["user"]
    return redirect('main')