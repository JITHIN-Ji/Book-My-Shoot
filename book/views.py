from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from django.core.files.storage import FileSystemStorage




# Create your views here.

def logins(request):
    if request.method=='POST':
        usname=request.POST['uname']
        password=request.POST['password']
        try:
            logs=login.objects.get(username=usname,password=password)
            request.session['lid']=logs.pk
            if logs.usertype=='admin':
                return HttpResponse("<script> alert('login sucessful');window.location='/adminhome'</script>")
            elif logs.usertype=='user':
                us=user.objects.get(log_id=request.session['lid'])
                request.session['uid']=us.pk
                return HttpResponse("<script> alert('login sucessful');window.location='/userhome'</script>")
        except:
            return HttpResponse("<script> alert('invalid username or password');window.location='login'</script>")

    return render(request,'login.html')


def adminhome(request):
    return render(request,'adminhome.html')


def index(request):
    return render(request,'index.html')

def userreg(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        password=request.POST['password']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        pla_ce=request.POST['place']
        phon_e=request.POST['phone']
        ema_il=request.POST['email']
        lg=login(username=user_name,password=password,usertype='user')
        lg.save()
        reg=user(fname=first_name,lname=last_name,place=pla_ce,phone=phon_e,email=ema_il,log=lg)
        reg.save()
    return render (request,'userreg.html')

def user_home(request):
    return render(request,'userhome.html')

def up_profile(request):
    if request.method=='POST':
        profname=request.POST['pname']
        detail=request.POST['details']
        sin_ce=request.POST['since']
        key_license=request.POST['license']
        profil=profile(name=profname,details=detail,since=sin_ce,keylicense=key_license)
        profil.save()
    return render(request,'profile.html')

def admin_view_user(request):
    view = user.objects.all()
    return render(request,'viewuser.html',{'view':view})

def admin_category(request):
    if request.method=='POST':
        catgory=request.POST['category']
        cate=category(category=catgory)
        cate.save()

    view=category.objects.all()
    return render (request,'category.html',{'view':view})

def adm_service(request):
    if request.method=='POST':
        adm_service=request.POST['service']
        adm_amount=request.POST['amount']
        adm_details=request.POST['details']
        adm_cate=request.POST['cate']

        adm_ser=service(service=adm_service,amount=adm_amount,details=adm_details,catgor_id=adm_cate)
        adm_ser.save()
    vie_ws=category.objects.all()
    vie_w=service.objects.all()
    return render (request,'service.html',{'vie_w':vie_w,'vie_ws':vie_ws})

def update_catagory(request,id):
    up_cate=category.objects.get(id=id)
    if request.method=='POST':
        upcate=request.POST['category']
        up_cate.category=upcate
        up_cate.save()
        return HttpResponse("<script>alert('update sucessfully');window.location='/category'</script>")
    return render(request,'updatecategory.html',{'val':up_cate})
    


def delete_category(request,id):
    deletecategory=category.objects.get(id=id)
    deletecategory.delete()

    return HttpResponse("<script> alert('delete sucessfully');window.location='/category'</script>")

def update_service(request,id):
    updateservice=service.objects.get(id=id)
    upd_category=category.objects.all()


    if request.method=='POST':
        upd_service=request.POST['service']
        upd_service=request.POST['amount']
        upd_service=request.POST['details']
        upd_service=request.POST['cate']
        updateservice.service=upd_service
        updateservice.amount=upd_service
        updateservice.details=upd_service
        updateservice.catgor_id=upd_service
        updateservice.save()
       
    return render(request,'updateservice.html',{'val':updateservice})

def delete_service(request,id):
    del_ser=service.objects.get(id=id)
    del_ser.delete()
    return HttpResponse("<script> alert('delete sucessfully');window.location='/adminservice'</script>")

def user_booking(request,id):
    #userbook=service.objects.get(id=id)

    if request.method=='POST':
        user_venue=request.POST['venue']
        user_place=request.POST['place']
        user_date=request.POST['date']
        
        userbooking=booking(venue=user_venue,place=user_place,date=user_date,status='pending',ser_id=id,use_id_id=request.session['uid'])
        userbooking.save()

    return render(request,'booking.html',)


def user_view_service(request):
    viewservice=service.objects.all()
    view_service=category.objects.all()
    return render(request,'userviewservice.html',{'viewservice':viewservice,'view_service':view_service})

def admin_view_booking(request):
    view=booking.objects.all()
    return render(request,'adminviewbooking.html',{'view':view})

def adm_accept_booking(request,id):
    admin_accept=booking.objects.get(id=id)
    admin_accept.status='approved'
    admin_accept.save()
    return HttpResponse("<script>alert('approved');window.location='/adminviewbooking'</script>")

def adm_delete_booking(request,id):
    admin_delete=booking.objects.get(id=id)
    admin_delete.status='deleted'
    admin_delete.save()
    
    return HttpResponse("<script>alert('deleted');window.location='/adminviewbooking'</script>")

def user_view_booking(request,):

    view=booking.objects.filter(use_id_id=request.session['uid'])
    return render (request,'userviewbooking.html',{'view':view})

def user_payment(request,id):
    if request.method=='POST':
        user_amount=request.POST['amount']
        user_date=request.POST['date']
        pay=payment(amount=user_amount,date=user_date,book_id_id=id)
        pay.save()
    return render(request,'payment.html')

def adm_view_advance_payment(request,id):
    view=payment.objects.filter(book_id_id=id)
    
        
    return render(request,'adminviewadvancepayment.html',{'view':view})

def admin_advance_payment(request,id):
 
    sucess_advancepayment=booking.objects.get(id=id)
    sucess_advancepayment.status='advance paid sucessfully'
    sucess_advancepayment.save()
    return HttpResponse("<script>alert('advance payment paid sucessfully');window.location='/adminviewbooking'</script>")


def userfullpayment(request,id):
    up_pay=payment.objects.get(book_id_id=id)
    book=booking.objects.get(id=id)
    serv=service.objects.get(id=book.ser_id)
    diff = int(serv.amount) - int(up_pay.amount)
    
    if request.method =='POST':
        
        am = request.POST['amo']
       
        
        
        add = int(up_pay.amount) + diff
        
       

        date=datetime.date.today()

        up_pay.amount = add
        up_pay.date = date
        up_pay.save()
        book.status='payment completed'
            
    return render(request,'full payment.html',{'up_pay':up_pay,'diff':diff})

def feedbacks(request):

    if request.method=='POST':
        feed=request.POST['feed1']
        date=datetime.date.today()

        feed_back = feedback(feedback1=feed,date=date,feedback_user_id=request.session['uid'])
        feed_back.save()
    return render(request,'feedback.html')

def admin_upload_video(request,id):
   
    if  request.method=='POST':
        upload_vi=request.FILES['img']
        up=FileSystemStorage()
        upadmin=up.save(upload_vi.name,upload_vi)
        admin_upload=uploads(ufile=upadmin,utype=upload_vi.content_type,booking_id=id)
        admin_upload.save()
    return render(request,'uplods.html')

    

def admin_work(request):
    if request.method=='POST':
        up_wo=request.FILES['video']
        ad_work=FileSystemStorage()
        ad=ad_work.save(up_wo.name,up_wo)
        admin_up_vi=works(files=ad,utype=up_wo.content_type)
        admin_up_vi.save()
    return render(request,'works.html')

def admin_view_feedback(request):
    view=feedback.objects.all()
    return render(request,'admin_view_feedback.html',{'view':view})

def user_view_upload_file(request,id):
    view=uploads.objects.filter(booking_id=id)
    return render(request,'user_view_works.html',{'view':view})














    



    


    
    



        











