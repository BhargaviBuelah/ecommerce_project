from django.shortcuts import render,redirect
from django.http import HttpResponse
from todoapp.models import Product
from django.db.models import Q
from todoapp.forms import Empform,ProductForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    print("Hello")
    #return redirect('/index')
    return HttpResponse("Hello from index")



def uname(request,username):
    
    #str1="hello from edit function"
    print(username)
    return HttpResponse("Entered username is :"+username)



def home(request):

    content={}
    #content['x']='Itvedant Eclass'
    #content['y']=100
    #content['x']=100
    #content['y']=70
    content['data']=[10,20,30,40,50,60]
    return render(request,'index.html',content)
def contact(request):
    return render(request,'contact.html')

def product(request):
    return render(request,'product.html')




    '''
return statement returns response object.
Response object is created by using
1) HttpResponse():It is used to create Response Object and 
                   that object is returned to the Client
2) render():  This function can return html file as a response 
    to the browser.
    render(request,'html file',data)

class student:



student()
'''

#product management system
def edit(request,rid):
    
    #str1="hello from edit function"
    #print(rid)
    #return HttpResponse("ID to be Edited:"+rid)
    if request.method=="POST":
        upname=request.POST['pname']
        udesc=request.POST['pdesc']
        uprice=request.POST['pprice']
        ucat=request.POST['cat']

        x=Product.obj1.filter(id=rid)
        x.update(name=upname,pdesc=udesc,price=uprice,cat=ucat)
        return redirect('/pdashboard')
    else:
        rec=Product.obj1.get(id=rid)
        #print(rec)
        content={}
        content['data']=rec
        return render(request,'editproduct.html',content)

def delete(request,rid):

    #print("ID to be deleted:"+rid)
    #return HttpResponse("ID to be deleted:"+rid)

    #Hard Delete
    #x=Product.objects.get(id=rid)
    #x.delete()
    
    #Soft delete
    x=Product.obj1.filter(id=rid)
    x.update(is_deleted="Y")
    return redirect('/pdashboard')


def dash_product(request):
    user_id=request.user.id# to fech id of the logged in user
    #print("Method",request.method)
    print(user_id)
    if request.method=="POST":
        #retrive data send from the form into python variable and store in the database
        #print("IN POST section")
        pname=request.POST['pname']
        desc=request.POST['pdesc']
        price=request.POST['pprice']
        cat=request.POST['cat']
        #print("Product Name",pname)
        #print("Product desc",desc)
        #print("Product price",price)
        #print("Product category",cat)
        p1=Product.obj1.create(name=pname,pdesc=desc,price=price,cat=cat,is_deleted="N",uid=user_id)
        #print(p1)
        p1.save()
        #return HttpResponse("Record Inserted Successfully")
        return redirect('/pdashboard')

    else:
        #show empty form
        #print("IN GET Section")
        #records=Product.objects.all()
        #select * from todoapp_product where uid=user_id and is_deleted="N";
        q1=Q(uid=user_id)
        q2=Q(is_deleted="N")
        records=Product.obj1.filter(q1 & q2)
        #print(records)
        content={}
        content['data']=records
        return render(request,'product_dashboard.html',content)

'''
1) cat=E
2) is_deleted="N"

select * from todoapp_product where cat="E" and is delete="N";
'''
'''
def filter_electronics(request):
    q1=Q(cat="E")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

def filter_grocery(request):
    q1=Q(cat="G")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

def filter_cloths(request):
    q1=Q(cat="C")
    q2=Q(is_deleted="N")
    rec=Product.objects.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

'''
def filter(request,vcat):
    #print(vcat)
    if vcat=="elec":
        f='E'
    elif vcat=="groc":
        f='G'
    elif vcat=="cloths":
        f='C'

    q1=Q(cat=f)
    q2=Q(is_deleted="N")
    rec=Product.obj1.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)


#inequality
def pfilter(request,p):
    if p=='>10000':
        #q1=Q(price__gt=10000)
        q1=Q(price__gte=10000)
    elif p=='<10000':
        #q1=Q(price__lt=10000)
        q1=Q(price__lte=10000)

    q2=Q(is_deleted="N")
    rec=Product.obj1.filter(q1 & q2)
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

#sorting

def sort(request,sv):

    if sv=='ltoh':
        #rec=Product.objects.order_by('price')
        #rec=Product.obj1.filter(is_deleted="N").order_by('price')
        rec=Product.cobj1.sortfilterasc()    
    elif sv=='htol':
        #rec=Product.objects.order_by('-price')
        #rec=Product.obj1.filter(is_deleted="N").order_by('-price')
        rec=Product.cobj1.sortfilterdesc() 
    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

#prange function
def prange(request):

    if request.method=="POST":
        min=request.POST['from']
        max=request.POST['to']
        print(min)
        print(max)
        q1=Q(price__gte=min)#1st condition: price grater than or equal to min
        q2=Q(price__lte=max)#2st condition: price less than or equal to max
        q3=Q(is_deleted="N")# product should  ot be deleted
        rec=Product.obj1.filter(q1 & q2 & q3)

    content={}
    content['data']=rec
    return render(request,'product_dashboard.html',content)

#formapi view function

def empform(request):
    if request.method=="POST":

        return HttpResponse("IN The Pos Section")
    else:
        efm=Empform()
        return render(request,'formapi.html',{'form':efm})

def productform(request):
    if request.method=="POST":

        pass
    else:
        pfn=ProductForm()
        return render(request,'modelformapi.html',{'mform':pfn})


def register(request):
    
    if request.method=="POST":
        #uname=request.POST['username']
        fmdata=RegisterForm(request.POST)
        #print(fmdata)
        if fmdata.is_valid():
            fmdata.save()
            #return HttpResponse("User Registered successfully")
            return redirect('/login')
        else:
            return HttpResponse("fail to create user")
    else:
        #rfm=UserCreationForm()
        rfm=RegisterForm()
        return render(request,'register.html',{'rform':rfm})

def user_login(request):

    if request.method=="POST":
        lfm=AuthenticationForm(request=request,data=request.POST)
        #print(lfm)
        if lfm.is_valid():
            uname=lfm.cleaned_data['username']
            upass=lfm.cleaned_data['password']
            #print(uname)
            #print(upass)
            #select * from auth_user where username=name and password=pass
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u) #It start session for that logged in user and store id of that user in the session
                return redirect('/pdashboard')
        else:
                return HttpResponse("Invalid username or password")
    else:
        lfm=AuthenticationForm()
        print("In user_login else part")
        return render(request,'login.html',{'lform':lfm})


def setcookie(request):
    r=render(request,'setcookie.html')
    r.set_cookie('name','ITVEDANT')
    r.set_cookie('rno','35')
    return r

def getcookie(request):
    data={}
    data['n']=request.COOKIES['name']
    data['r']=request.COOKIES['rno']
    return render(request,'getcookie.html',data)

def setsession(request):

    request.session['user']="ITVEDANT"
    return render(request,'setsession.html')

def getsession(request):

    d=request.session['user']="ITVEDANT"
    return render(request,'getsession.html',{'data':d})

def user_logout(request):

    logout(request)#This functionality destroy session
    return redirect('/login')



