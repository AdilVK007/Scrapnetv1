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

    # changes after submit
    l = Login()
    l.username = email
    l.password = phone
    l.type = 'RTO'
    l.save()
    r = Rto()
    r.username = username
    r.email = email
    r.phone = phone
    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S")+".jpg"
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
    r = Rto.objects.all()
    return render(request,"Admin/rtoview.html",{'data':r})

def rtoview_post(request):
    search = request.POST['textfield']
    r = Rto.objects.filter(username__icontains=search)
    return render(request, "Admin/rtoview.html", {'data': r})

def deleterto(request,id):
    r = Rto.objects.get(id=id)
    r.delete()
    return HttpResponse('''<script>alert("Successfully Deleted");window.location='/Myapp/rto_view/'</script>''')

def editrto(request,id):
    r = Rto.objects.get(id=id)
    return render(request,"Admin/editrto.html",{'data':r})

def editro_post(request):
    username = request.POST['textfield']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield5']
    district = request.POST['textfield6']
    pin = request.POST['textfield7']
    post = request.POST['textfield8']
    state = request.POST['textfield9']
    id = request.POST['id']

    # changes after submit
    # l = Login()
    # l.username = email
    # l.password = phone
    # l.type = 'rto'
    # l.save()

    r = Rto.objects.get(id=id)
    if 'textfield2' in request.FILES:
        photo = request.FILES['textfield2']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        r.photo = path
        r.save()

    r.username = username
    r.email = email
    r.phone = phone

    r.place = place
    r.post = post
    r.pin = pin
    r.district = district
    r.state = state

    # r.LOGIN = l
    r.save()
    return HttpResponse('''<script>alert("RTO user sucessfully updated");window.location='/Myapp/rto_view/'</script>''')

def police_station(request):
    return render(request,"Admin/policestationmanagement.html")

def policestation_post(request):
    username = request.POST['textfield']
    photo = request.FILES['textfield1']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    state = request.POST['textfield7']
    siname = request.POST['textfield8']
    pin = request.POST['textfield9']

    l = Login()
    l.username = email
    l.password = phone
    l.type = 'Police Station'
    l.save()

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
    fs.save(date, photo)
    path = fs.url(date)

    pd = Policestation()
    pd.username = username
    pd.photo = path
    pd.email = email
    pd.phone = phone
    pd.place = place
    pd.pin = pin
    pd.post = post
    pd.district = district
    pd.state = state
    pd.siname = siname
    pd.LOGIN = l
    pd.save()

    return HttpResponse('''<script>alert("Police station has Successfuly Added");window.location='/Myapp/police_station/'</script>''')

def police_station_view(request):
    obj = Policestation.objects.all()
    return render(request,"Admin/pdstationmanagementview.html",{'data':obj})

def policestationview_post(request):
    search = request.POST['textfield']
    obj = Policestation.objects.filter(username__icontains=search)
    return render(request,"Admin/pdstationmanagementview.html",{'data':obj})

def editpolicestation(request,id):
    p = Policestation.objects.get(id=id)
    return render(request,"Admin/editpolicestation.html",{'data':p})
def editpolicestation_post(request):
    id = request.POST['id']
    username = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    place = request.POST['textfield4']
    post = request.POST['textfield5']
    district = request.POST['textfield6']
    state = request.POST['textfield7']
    siname = request.POST['textfield8']
    pin = request.POST['textfield9']


    if 'textfield1' in request.FILES:
        photo = request.FILES['textfield1']
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        Policestation.objects.filter(id=id).update(photo=path)
        # return HttpResponse('''<script>alert("Police station has Successfuly updated");window.location='/Myapp/police_station/'</script>''')

    Policestation.objects.filter(id=id).update(username=username,email=email,phone=phone,place=place,post=post,district=district,state=state,siname=siname,pin=pin)

    return HttpResponse('''<script>alert("Police station has Successfuly updated");window.location='/Myapp/police_station_view/'</script>''')

def deletepolicestation(request,id):
    pd = Policestation.objects.get(id=id)
    pd.delete()
    #Policestation.objects.get(id=id).delete(username=username,email=email,phone=phone,place=place,post=post,district=district,state=state,siname=siname,pin=pin)
    return HttpResponse('''<script>alert("Successfully Deleted");window.location='/Myapp/police_station_view/'</script>''')

#scrap dealer view
def scrap_dealer_approve(request):
    s = Scrapdealer.objects.filter(status='Approved')
    # s.status = 'Approved'
    return render(request, "Admin/scrapdealerapprove.html",{'data':s})
    # return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Approved");window.location='/Myapp/scrap_dealer_approve/<>'</script>''')

#approved scrap dealer status on database
def scrapdealer(request,id):
    Scrapdealer.objects.filter(id=id).update(status='Approved')
    # return  render(request,"Admin/scrap_dealer_approve")
    return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Approved");window.location='/Myapp/scrap_dealer_approve/'</script>''')

# scrap dealer approve post
def scrap_dealer_approve_post(request):
    search = request.POST['textfield']
    return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Added");window.location='/Myapp/scrap_dealer_approve/'</script>''')

#rejected scrapdealer(update in database)
def rejectscrapdealer(request,id):
    Scrapdealer.objects.filter(id=id).update(status='Rejected')
    # return render(request, "Admin/scrapdealerapprove.html")
    return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Rejected");window.location='/Myapp/scrap_dealer_view/'</script>''')

# view approved scrap dealers
def viewapprovedscrapdealer(request):

    return render(request, "Admin/viewapprovedscrapdealer.html")

def viewapprovedscrapdealer_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/scrapdealerview.html")

# logined scrap dealers
def scrap_dealer_view(request):
    res=Scrapdealer.objects.filter(status='Pending')
    return render(request,"Admin/scrapdealerview.html",{'data':res})

def scrap_dealer_view_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/scrapdealerview.html")

def view_rejected_scrap_dealer(request):
    r = Scrapdealer.objects.filter(status='Rejected')
    return render(request,"Admin/viewrejectedscrapdealer.html",{'data':r})

#displaying rejected scrapdealers
def view_rejected_scrap_dealer_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/viewrejectedscrapdealer.html")

# rto funtion
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
    sv = Vehicle.objects.all()
    return render(request,"Admin/scrappedvehicleview.html",{'data':sv})

def scrapped_vehicle_view_post(request):
    search = request.POST['textfield']
    return render(request, "Admin/scrappedvehicleview.html")

def editvehicle(request):
    return render(request,"Admin/editdelvehicle.html")

def view_users(request):
    return render(request,"Admin/viewusers.html")

def view_users_post(request):
    search = request.POST['textfield']
    return render(request,"Admin/viewusers.html")

def admin_home(request):
    return render(request,"Admin/home.html")