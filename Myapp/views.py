import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Myapp.models import *


def login(request):
    return render(request,"Admin/login.html")

def login_post(request):
    uname=request.POST['textfield']
    password = request.POST['textfield2']
    login = Login.objects.filter(username=uname,password=password)
    if login.exists():
        l = Login.objects.get(username=uname,password=password)
        request.session['lid']=l.id
        if l.type == 'admin':
            return HttpResponse('''<script>alert("Login Successfully");window.location='/Myapp/admin_home/'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid User..");window.location='/Myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("User not found..");window.location='/Myapp/login/'</script>''')

def change_password(request):
    return render(request,"Admin/changepassword.html")

def change_pass_post(request):
    currentpass=request.POST['textfield']
    newpass = request.POST['textfield2']
    confirmpass = request.POST['textfield3']
    l = Login.objects.get(id=request.session['lid'])
    if l.password == currentpass:
        if newpass == confirmpass:
            l.password = newpass
            l.save()
            return HttpResponse('''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Passwords are not matching");window.location='/Myapp/change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')


def rto_management(request):
    return render(request,'Admin/rtomanagement.html')

def rto_management_post(request):
    username = request.POST['textfield']
    photo = request.FILES['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield5']
    district = request.POST['textfield6']
    pin = request.POST['textfield7']
    post = request.POST['textfield8']
    state = request.POST['textfield9']

    l = Login()
    l.username = email
    l.password = phone
    l.type = 'rto'
    l.save()
    r = Rto()
    r.username = username
    r.email = email
    r.phone = phone
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs.save(date,photo)
    path = fs.url(date)
    r.photo = path
    r.place = place
    r.post = post
    r.pin = pin
    r.district = district
    r.state = state
    r.LOGIN = l
    r.save()

    return HttpResponse('''<script>alert("Successfully Registered");window.location='/Myapp/rto_management/'</script>''')

def rto_view(request):
    return render(request,"Admin/rtoview.html")

def rtoview_post(request):
    search = request.POST['textfield']
    return HttpResponse('''rtoview.html''')

def police_station(request):
    return render(request,"Admin/policestationmanagement.html")

def policestation_post(request):
    username = request.POST['textfield']
    photo = request.POST['textfield1']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    state = request.POST['textfield7']
    siname = request.POST['textfield8']
    return HttpResponse('''<script>alert("Police station has Successfuly Added");window.location='/Myapp/policestationmanagement/'</script>''')

def police_station_view(request):
    return render(request,"Admin/pdstationmanagementview.html")

def policestationview_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/pdstationmanagementview.html")

def scrap_dealer_approve(request):
    return render(request, "Admin/scrapdealerapprove.html")

def scrap_dealer_approve_post(request):
    search = request.POST['textfield']
    return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Added");window.location='/Myapp/scrapdealerapprove/'</script>''')

def viewapprovedscrapdealer(request):
    return render(request, "Admin/viewapprovedscrapdealer.html")

def viewapprovedscrapdealer_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/scrapdealerview.html")

def scrap_dealer_view(request):
    return render(request,"Admin/scrapdealerview.html")

def scrap_dealer_view_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/scrapdealerview.html")

def view_rejected_scrap_dealer(request):
    return render(request,"Admin/viewrejectedscrapdealer.html")

def view_rejected_scrap_dealer_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/viewrejectedscrapdealer.html")

def add_vehicle(request):
    return render(request,"Admin/vehiclemangementadd.html")

def addvehicle_post(request):
    vehiclename = request.POST['textfield']
    regnum = request.POST['textfield2']
    ownername = request.POST['textfield3']
    regdate = request.POST['textfield4']
    vehicletype = request.POST['textfield5']
    contact = request.POST['textfield6']
    photo = request.POST['fileField']
    enginenumber = request.POST['textfield7']
    chasenum = request.POST['textfield8']
    monthofmanufacture = request.POST['textfield9']
    yearofmanufacture = request.POST['textfield10']
    placereg = request.POST['textfield11']
    return HttpResponse('''<script>alert("Vehicle succesfully added");window.location='/Myapp/vehiclemangementadd/'</script>''')

def scrapped_vehicle_view(request):
    return render(request,"Admin/vehicleview.html")

def scrapped_vehicle_view_post(request):
    search = request.POST['textfield']
    return render(request, "Admin/vehicleview.html")

def editvehicle(request):
    return render(request,"Admin/editdelvehicle.html")

def view_users(request):
    return render(request,"Admin/viewusers.html")

def view_users_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/viewusers.html")

def admin_home(request):
    return render(request,"Admin/home.html")