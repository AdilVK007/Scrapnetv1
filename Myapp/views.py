import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Myapp.models import *


def login(request):
    return render(request,"indexlogin.html")

def login_post(request):
    uname=request.POST['textfield']
    password = request.POST['textfield2']
    login = Login.objects.filter(username=uname,password=password)
    if login.exists():
        l = Login.objects.get(username=uname,password=password)
        request.session['lid']=l.id
        if l.type == 'admin':
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/admin_home/'</script>''')
        elif l.type == 'police':
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/police_home'</script>''')
        elif l.type == 'RTO':
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/rto_home'</script>''')
        elif l.type == 'ScrapDealer':
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/scrapdealer_home'</script>''')
        elif l.type == 'User':
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/user_home'</script>''')
        else:
            return HttpResponse('''<script>alert("Welcome! You have successfully logged in.");window.location='/Myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("Sorry, we couldn't find that user. Please check your credentials and try again.");window.location='/Myapp/login/'</script>''')

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
            return HttpResponse('''<script>alert("Your password has been updated successfully...");window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("Oops! The passwords you entered do not match. Please try again.");window.location='/Myapp/change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("Your password has been successfully changed...");window.location='/Myapp/login/'</script>''')


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
    return HttpResponse('''<script>alert("RTO has been successfully added.");window.location='/Myapp/admin_home/'</script>''')

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
    return HttpResponse('''<script>alert("RTO successfully deleted.");window.location='/Myapp/rto_view/'</script>''')

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
    return HttpResponse('''<script>alert("RTO user updated successfully.");window.location='/Myapp/rto_view/'</script>''')

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

    return HttpResponse('''<script>alert("Police station successfully added.");window.location='/Myapp/admin_home/'</script>''')

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

    return HttpResponse('''<script>alert("Police station updated successfully.");window.location='/Myapp/police_station_view/'</script>''')

def deletepolicestation(request,id):
    pd = Policestation.objects.get(id=id)
    pd.delete()
    #Policestation.objects.get(id=id).delete(username=username,email=email,phone=phone,place=place,post=post,district=district,state=state,siname=siname,pin=pin)
    return HttpResponse('''<script>alert("Police station successfully deleted.");window.location='/Myapp/police_station_view/'</script>''')

#scrap dealer view
def scrap_dealer_approve(request):
    s = Scrapdealer.objects.filter(status='Approved')
    # s.status = 'Approved'
    return render(request, "Admin/scrapdealerapprove.html",{'data':s})
    # return HttpResponse('''<script>alert("Scrap Dealer has Successfuly Approved");window.location='/Myapp/scrap_dealer_approve/<>'</script>''')

#approved scrap dealer status on database
def scrapdealer(request,id):
    Scrapdealer.objects.filter(LOGIN_id=id).update(status='Approved')
    Login.objects.filter(id=id).update(type='ScrapDealer')
    # return  render(request,"Admin/scrap_dealer_approve")
    return HttpResponse('''<script>alert("Scrap dealer successfully approved.");window.location='/Myapp/scrap_dealer_approve/'</script>''')

# scrap dealer approve post
def scrap_dealer_approve_post(request):
    search = request.POST['textfield']
    s = Scrapdealer.objects.filter(name__icontains=search)
    return render(request, "Admin/scrapdealerapprove.html",{'data':s})

#rejected scrapdealer(update in database)
def rejectscrapdealer(request,id):
    Scrapdealer.objects.filter(id=id).update(status='Rejected')
    # return render(request, "Admin/scrapdealerapprove.html")
    return HttpResponse('''<script>alert("Scrap Dealer Successfuly Rejected");window.location='/Myapp/scrap_dealer_view/'</script>''')

# view approved scrap dealers
def viewapprovedscrapdealer(request):
    return render(request, "Admin/viewapprovedscrapdealer.html")

def viewapprovedscrapdealer_post(request):
    search = request.POST['textfield']
    s = Scrapdealer.objects.filter(name__icontains=search)
    return render(request,"Admin/scrapdealerview.html",{'data':s})

# logined scrap dealers
def scrap_dealer_view(request):
    res=Scrapdealer.objects.filter(status='Pending')
    return render(request,"Admin/scrapdealerview.html",{'data':res})

def scrap_dealer_view_post(request):
    search = request.POST['textfield']
    s = Scrapdealer.objects.filter(name__icontains=search)
    return render(request,"Admin/scrapdealerview.html",{'data':s})

def view_rejected_scrap_dealer(request):
    r = Scrapdealer.objects.filter(status='Rejected')
    return render(request,"Admin/viewrejectedscrapdealer.html",{'data':r})

#displaying rejected scrapdealers
def view_rejected_scrap_dealer_post(request):
    search = request.POST['textfield']
    s = Scrapdealer.objects.filter(name__icontains=search)
    return render(request,"Admin/viewrejectedscrapdealer.html",{'data':s})

# rto funtion
# def add_vehicle(request):
#     return render(request,"Admin/vehiclemangementadd.html")
#
# def addvehicle_post(request):
#     vehiclename = request.POST['textfield']
#     regnum = request.POST['textfield2']
#     ownername = request.POST['textfield3']
#     regdate = request.POST['textfield4']
#     vehicletype = request.POST['textfield5']
#     contact = request.POST['textfield6']
#     photo = request.POST['fileField']
#     enginenumber = request.POST['textfield7']
#     chasenum = request.POST['textfield8']
#     monthofmanufacture = request.POST['textfield9']
#     yearofmanufacture = request.POST['textfield10']
#     placereg = request.POST['textfield11']
#     return HttpResponse('''<script>alert("Vehicle succesfully added");window.location='/Myapp/vehiclemangementadd/'</script>''')

def scrapped_vehicle_view(request):
    sv = Vehicle.objects.filter(status='scrapping')
    return render(request,"Admin/scrappedvehicleview.html",{'data':sv})

def scrapped_vehicle_view_post(request):
    search = request.POST['textfield']
    s = Vehicle.objects.filter(vehicle_name__icontains=search)
    return render(request, "Admin/scrappedvehicleview.html",{'data':s})

# def editvehicle(request):
#     return render(request,"Admin/viewvehicle.html")

def view_users(request):
    users = User.objects.all()
    return render(request,"Admin/viewusers.html",{'data':users})

def view_users_post(request):
    search = request.POST['textfield']
    s = User.objects.filter(username__icontains=search)
    return render(request,"Admin/viewusers.html",{"data":s})

def admin_home(request):
    return render(request,"Admin/adminindex.html")





#police station

def changepass(request):
    return render(request,"police station/changepass.html")

def changepass_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    l = Login.objects.get(id=request.session['lid'])
    if l.password == currentpassword:
        if newpassword == confirmpassword:
            l.password = newpassword
            l.save()
            return HttpResponse(
                '''<script>alert("Your new password has been updated...");window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Oops! The passwords you entered do not match. Please try again.");window.location='/Myapp/change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("Your password has been changed successfully...");window.location='/Myapp/login/'</script>''')

def addsuspeciousactvity(request):
    res = Vehicle.objects.all()
    return render(request,"police station/addsuspeciousactvity.html",{'data':res})

def addsuspeciousactvity_post(request):
    vehicle = request.POST['vehicle']
    activity = request.POST['textfield2']
    datee = request.POST['textfield3']
    obj = Activity()
    obj.VEHICLE=Vehicle.objects.get(id=vehicle)
    obj.POLICE= Policestation.objects.get(LOGIN_id=request.session['lid'])
    obj.activity=activity
    obj.date=datee
    obj.save()
    return HttpResponse('''<script>alert("New suspicious activity detected and added...");window.location='/Myapp/addsuspeciousactvity/'</script>''')

def viewsusactivity(request):
    viewactivty = Activity.objects.all()
    return render(request,"police station/viewsusactivity.html",{'data':viewactivty})

def editsusactivity(request,id):
    susactivy = Activity.objects.get(id=id)
    ve=Vehicle.objects.all()
    return render(request, "police station/editsuspeciousactvity.html", {'data': susactivy,'data1':ve})

def editsusactivity_post(request):
    vehicle = request.POST['vehicle']
    V = Vehicle.objects.get(id=vehicle)
    activity = request.POST['textfield2']
    date = request.POST['textfield3']
    id = request.POST['id1']
    obj = Activity.objects.get(id=id)
    obj.VEHICLE = V
    obj.activity = activity
    obj.date = date
    obj.save()

    return HttpResponse('''<script>alert("Activity successfully updated..");window.location='/Myapp/viewsusactivity/'</script>''')

def deletesusactity(request,id):
    susactivity = Activity.objects.get(id=id)
    susactivity.delete()
    return HttpResponse('''<script>alert("Actvity Successfully Removed..");window.location='/Myapp/viewsusactivity/'</script>''')

def viewsusactivity_post(request):
    date = request.POST['textfield']
    todate = request.POST['textfield2']
    a = Activity.objects.filter(date__range=[date,todate])
    return render(request,"police station/viewsusactivity.html",{'data':a})

def viewscrappedvehicle(request):
    viewscrapedveh = Vehicle.objects.filter(status='Vehicle Scrapped')
    return render(request,"police station/viewscrappedvehicle.html",{'data':viewscrapedveh})

def viewscrappedvehicle_post(request):
    search = request.POST['textfield']
    w = Vehicle.objects.filter(vehicle_name__icontains=search,status='Vehicle Scrapped')
    return render(request,"police station/viewscrappedvehicle.html",{'data':w})

def police_home(request):
    return render(request,"police station/home.html")



# RTO MODULE
def changepass(request):
    return render(request,"RTO/changepass.html")

def changepass_post(request):
    currentpassword = request.POST['textfield']
    newpassword = request.POST['textfield2']
    confirmpassword = request.POST['textfield3']
    l = Login.objects.get(id=request.session['lid'])
    if l.password == currentpassword:
        if newpassword == confirmpassword:
            l.password = newpassword
            l.save()
            return HttpResponse(
                '''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Passwords are not matching");window.location='/Myapp/change_password/'</script>''')
    else:
        return HttpResponse('''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')

def viewprofile(request):
    r = Rto.objects.get(LOGIN=request.session['lid'])
    return render(request,"RTO/viewprofile.html",{"data":r})

# def viewprofile_post(request):
#     return render(request,"RTO/viewprofile.html")

def vehicleadd(request):
    return render(request,"RTO/vehicleadd.html")

def vehicleadd_post(request):
    vehiclename = request.POST['textfield']
    regnum = request.POST['textfield2']
    ownername = request.POST['textfield3']
    regdate = request.POST['textfield4']
    vehicletype = request.POST['textfield5']
    contact = request.POST['textfield6']
    photo = request.FILES['fileField']
    enginenumber = request.POST['textfield7']
    chasenum = request.POST['textfield8']
    monthofmanufacture = request.POST['textfield10']
    yearofmanufacture = request.POST['textfield9']
    regplace = request.POST['textfield11']
    adhar = request.POST['textfield12']

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
    fs.save(date, photo)
    path = fs.url(date)

    obj = Vehicle()
    obj.vehicle_name=vehiclename
    obj.reg_number=regnum
    obj.owner_name=ownername
    obj.reg_date=regdate
    obj.reg_place=regplace
    obj.Vehicle_type=vehicletype
    obj.contact=contact
    obj.photo=path
    obj.engine_number=enginenumber
    obj.chase_number=chasenum
    obj.month_of_manufacturing = monthofmanufacture
    obj.year_of_manufacturing=yearofmanufacture
    obj.aadhar_no=adhar
    obj.RTO=Rto.objects.get(LOGIN=request.session['lid'])
    obj.save()

    return HttpResponse('''<script>alert("Vehicle succesfully added");window.location='/Myapp/vehicleadd/'</script>''')

def viewveh(request):
    ev = Vehicle.objects.all()
    return render(request, "RTO/viewvehicle.html", {'data':ev})

def viewveh_post(request):
    search = request.POST['textfield']
    w = Vehicle.objects.filter(vehicle_name__icontains=search)
    return render(request, "RTO/viewvehicle.html", {'data': w})

def editveh(request,id):
    ev = Vehicle.objects.get(id=id)
    return render(request, "RTO/editvehicle.html", {'data':ev})

def editveh_post(request):
    vehiclename = request.POST['textfield']
    regnum = request.POST['textfield2']
    ownername = request.POST['textfield3']
    regdate = request.POST['textfield4']
    vehicletype = request.POST['textfield5']
    contact = request.POST['textfield6']
    enginenumber = request.POST['textfield7']
    chasenum = request.POST['textfield8']
    monthofmanufacture = request.POST['textfield9']
    yearofmanufacture = request.POST['textfield10']
    regplace = request.POST['textfield11']
    adhar = request.POST['textfield12']
    id = request.POST['id']
    obj = Vehicle.objects.get(id=id)

    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']

        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)
        obj.photo = path
        obj.save()
    obj.vehicle_name = vehiclename
    obj.reg_number = regnum
    obj.owner_name = ownername
    obj.reg_date = regdate
    obj.reg_place = regplace
    obj.Vehicle_type = vehicletype
    obj.contact = contact
    obj.engine_number = enginenumber
    obj.chase_number = chasenum
    obj.year_of_manufacturing = yearofmanufacture
    obj.month_of_manufacturing = monthofmanufacture
    obj.aadhar_no = adhar
    obj.save()
    return HttpResponse('''<script>alert("Vehicle succesfully Updated");window.location='/Myapp/viewveh/'</script>''')

def deleteveh(request,id):
    delveh = Vehicle.objects.get(id=id)
    delveh.delete()
    return HttpResponse('''<script>alert("Actvity Successfully Removed..");window.location='/Myapp/viewveh/'</script>''')


def viewusers(request):
    users = User.objects.all()
    return render(request,"RTO/viewusers.html",{'data':users})

def viewusers_post(request):
    search = request.POST['textfield']
    s = User.objects.filter(username__icontains=search)
    return render(request, "RTO/viewusers.html", {"data": s})

def viewscrapedveh(request):
    sv = Vehicle.objects.filter(status='Vehicle Scrapped')
    return render(request, "RTO/viewscrappedvehicle.html", {'data': sv})

def viewscrapedveh_post(request):
    search = request.POST['textfield']
    s = Vehicle.objects.filter(vehicle_name__icontains=search)
    return render(request, "RTO/viewscrappedvehicle.html", {'data': s})

def rto_home(request):
    return render(request,"RTO/home.html")

def signup_dealer(request):
    return render(request,"scrap dealer/signup.html")

def signup_dealer_post(request):
    name = request.POST['textfield']
    photo = request.FILES['fileField']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    # state = request.POST['textfield10']
    lic_no = request.POST['textfield9']
    passwd = request.POST['textfield11']
    confirmpass = request.POST['textfield12']
    if passwd == confirmpass:

        l = Login()
        l.username=email
        l.password=passwd
        l.type='pending'
        l.save()
        fs = FileSystemStorage()
        date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
        fs.save(date, photo)
        path = fs.url(date)

        obj = Scrapdealer()
        obj.name = name
        obj.email=email
        obj.phone=phone
        obj.photo = path
        obj.place = place
        obj.post = post
        obj.pin = pin
        obj.district=district
        # obj.state = state
        obj.license_no=lic_no
        obj.status='Pending'
        obj.LOGIN=l
        obj.save()

        return HttpResponse('''<script>alert("Account is successfully created..");window.location='/Myapp/signup_dealer/'</script>''')
    else:
        return HttpResponse('''<script>alert("Password doesn't Matching..");window.location='/Myapp/signup_dealer/'</script>''')

def dealer_viewprofile(request):
    d = Scrapdealer.objects.get(LOGIN=request.session['lid'])
    return render(request,"scrap dealer/viewprofile.html",{'data':d})


def updateprofile(request):
    d = Scrapdealer.objects.get(LOGIN=request.session['lid'])
    return render(request,"scrap dealer/updateprofile.html",{'data':d})

def updateprofile_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    # state = request.POST['textfield10']
    lic_no = request.POST['textfield9']
    # id = request.POST['id']

    l = Login.objects.get(id=request.session['lid'])
    l.username = email
    l.save()

    obj = Scrapdealer.objects.get(LOGIN_id=request.session['lid'])
    if 'fileField' in request.FILES:
        photo = request.POST['fileField']
        if photo != "":
            fs = FileSystemStorage()
            date = datetime.datetime.now().strftime("%Y%M%D-%H%M%S") + ".jpg"
            fs.save(date, photo)
            path = fs.url(date)
            obj.photo = path

    obj.name = name
    obj.email = email
    obj.phone=phone
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.district = district
    # obj.state = state
    obj.license_no=lic_no
    obj.save()

    return HttpResponse('''<script>alert("Account is successfully updated..");window.location='/Myapp/dealer_viewprofile/'</script>''')

def viewrequest(request):
    vr = Request.objects.all()
    return render(request,"scrap dealer/viewrequest.html",{'data':vr})

def viewrequest_post(request):
    search = request.POST['textfield']
    w = Request.objects.filter(requestid_icontains=search)
    return render(request, "scrap dealer/viewrequest.html",{'data': w})

def viewsusAct(request):
    viewactivty = Activity.objects.all()
    return render(request,"scrap dealer/viewsuspeciousactivity.html",{'data':viewactivty})

def viewsusAct_post(request):
    date = request.POST['textfield']
    todate = request.POST['textfield2']
    act = Activity.objects.filter(date__range=[date, todate])
    return render(request, "scrap dealer/viewsuspeciousactivity.html", {'data': act})

def viewverifystats(request):
    return render(request,"scrap dealer/viewverifystats.html")

def viewverifystats_post(request):
    # search = request.POST['textfield']
    # v = Request.objects.filter(requestid_icontains=search)
    return render(request,"scrap dealer/viewverifystats.html")

def scrapstationup(request):
    return render(request,"scrap dealer/updateprofile.html")

def scrapstationup_post(request):
    return render(request,"scrap dealer/updateprofile.html")

def scrapdealer_home(request):
    return render(request,"scrap dealer/home.html")




def usersignup(request):
    return render(request,"user/signup.html")

def usersignup_post(request):
    username = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield5']
    place = request.POST['textfield6']
    post = request.POST['textfield7']
    pin = request.POST['textfield8']
    district = request.POST['textfield9']
    Aadharno = request.POST['textfield10']
    state = request.POST['textfield11']
    pic = request.FILES['textfield12']
    passwd = request.POST['textfield13']
    confirmpass = request.POST['textfield14']

    fs = FileSystemStorage()
    date = datetime.datetime.now().strftime("%Y%m%d-%H%%M%S")+".jpg"
    fn = fs.save(date,pic)
    lobj = Login()
    lobj.username=email
    lobj.password=confirmpass
    lobj.type='User'
    lobj.save()

    u = User()
    u.username = username
    u.email = email
    u.phone=phone
    u.photo=fs.url(date)
    u.gender=gender
    u.dob=dob
    u.place=place
    u.post=post
    u.pin=pin
    u.District=district
    u.state=state
    u.aadhar_no = Aadharno
    u.LOGIN = lobj
    u.save()

    return HttpResponse('''<script>alert("Account is successfully created..");window.location='/Myapp/login/'</script>''')
def changepasswd(request):
    return render(request,"user/changepasswd.html")

def changepasswd_post(request):
    currentpass = request.POST['textfield']
    newpass = request.POST['textfield2']
    confirmpass = request.POST['textfield3']
    l = Login.objects.get(id=request.session['lid'])
    if l.password == currentpass:
        if newpass == confirmpass:
            l.password = newpass
            l.save()
            return HttpResponse(
                '''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')
        else:
            return HttpResponse(
                '''<script>alert("Passwords are not matching");window.location='/Myapp/changepasswd/'</script>''')
    else:
        return HttpResponse('''<script>alert("New password has updated..");window.location='/Myapp/login/'</script>''')

def userviewprofile(request):
    u = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/viewprofile.html",{'data':u})

def edituserprofile(request):
    eu = User.objects.get(LOGIN_id=request.session['lid'])
    return render(request,"user/editprofile.html",{'data':eu})

def edituserprofile_post(request):
    username = request.POST['textfield']
    email = request.POST['textfield2']
    phone = request.POST['textfield3']
    gender = request.POST['RadioGroup1']
    dob = request.POST['textfield5']
    place = request.POST['textfield6']
    post = request.POST['textfield7']
    pin = request.POST['textfield8']
    district = request.POST['textfield9']
    Aadharno = request.POST['textfield10']
    state = request.POST['textfield11']

    u = User.objects.get(LOGIN_id = request.session['lid'])
    if 'textfield12' in request.FILES:
        pic = request.FILES['textfield12']
        if pic != '':
            fs = FileSystemStorage()
            date = datetime.datetime.now().strftime("%Y%m%d-%H%%M%S") + ".jpg"
            fn = fs.save(date, pic)
            u = User.objects.filter(LOGIN_id = request.session['lid'])
            u.photo = fs.url(date)
            u.save()

    u.username = username
    u.email = email
    u.phone = phone
    u.gender = gender
    u.dob = dob
    u.place = place
    u.post = post
    u.pin = pin
    u.District = district
    u.state = state
    u.aadhar_no = Aadharno
    u.save()

    return HttpResponse('''<script>alert("Profile has been updated..");window.location='/Myapp/userviewprofile/'</script>''')

def viewvehicle(request):
    a=User.objects.get(LOGIN_id=request.session['lid']).aadhar_no
    vv = Vehicle.objects.filter(aadhar_no=a)
    return render(request,"user/viewvhicle.html",{'data':vv})

def viewvehicle_post(request):
    search = request.POST['textfield']
    vehv = Vehicle.objects.filter(vehicle_name__icontains=search)
    return render(request,"user/viewvhicle.html",{'data':vehv})

def addscraprequest(request):
    return render(request, "user/Addscraprequest.html")

def addscraprequest_post(request):
    return HttpResponse('''<script>alert("Scrapping Requested to all Scrapping Dealers..");window.location='/Myapp/user_home/'</script>''')

def viewrequeststation(request):
    return render(request, "user/Addscraprequest.html")

def getcertify(request):
    return render(request, "user/Addscraprequest.html")

def user_home(request):
    return render(request,"user/home.html")
