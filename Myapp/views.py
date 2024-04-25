import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Myapp.models import *


###########################################BC




import json

#to establish connection with ganache(bc)

from web3 import Web3, HTTPProvider
blockchain_address = 'http://127.0.0.1:7545'
web3 = Web3(HTTPProvider(blockchain_address))
web3.eth.defaultAccount = web3.eth.accounts[0]

compiled_contract_path = 'C:\\Users\\Administrator\\PycharmProjects\\scrap\\Myapp\\static\\BC\\build\\contracts\\scrapnet.json'
deployed_contract_addressa = web3.eth.accounts[0]
deployed_contract_address = web3.eth.accounts[0]



#############################################3










# Main login section
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

# change pass for admin
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

# rto management (Add,Edit, delete rto)
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

# police station mangement (Add, edit, delete police)
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

def changepasspolice(request):
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
    return render(request,"police station/policeindex.html")



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
    obj.lic_no=lic_no
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

def certificate_rto(request,vid):
    return render(request,"RTO/certificate.html",{'vid':vid})


def certificate_rto_post(request):
    crtfct= request.FILES['fileField']
    lid=request.session['lid']
    vid=request.POST["vid"]

    RID=Rto.objects.get(LOGIN_id=lid)
    fs=FileSystemStorage()
    date="certificate/"+datetime.datetime.now().strftime("%Y%m%d%H%M%S")+'.jpg'
    fn=fs.save(date,crtfct)
    path=fs.url(date)

    obj = certificate()
    obj.file=path
    obj.VEHICLE_id=vid
    obj.status="Issued"
    obj.save()
    Vehicle.objects.filter(id=vid).update(status="DEACTIVATE")
    return HttpResponse('''<script>alert('issue certificate  Successfully');window.location="/Myapp/rto_home/"</script>''')

def viewsusAct_rto(request, vid):
    ls = Activity.objects.filter(VEHICLE_id=vid)
    request.session['sid'] = vid
    return render(request,"RTO/viewsuspeciousactivity.html",{'data':ls})

def viewsusActrto_post(request):
    date = request.POST['textfield']
    todate = request.POST['textfield2']
    act = Activity.objects.filter(date__range=[date, todate])
    return render(request, "RTO/viewsuspeciousactivity.html", {'data': act})



def rto_home(request):
    return render(request,"RTO/rtoindex.html")


# scrap dealer module

def signup_dealer(request):
    return render(request, "scrap dealer/scrapdealersignupindex.html")

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

        return HttpResponse('''<script>alert("Account is successfully created..");window.location='/Myapp/login/'</script>''')
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
    return render(request, "scrap dealer/viewpendscraprequest.html", {'data':vr})

def viewrequest_post(request):
    search = request.POST['textfield']
    w = Request.objects.filter(requestid_icontains=search)
    return render(request, "scrap dealer/viewpendscraprequest.html", {'data': w})



def pending_scrapreq(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber,"hhhh")
    lq = []
    for i in range(blocknumber, 0, -1):
        print(i,"kkkk")
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            print("jjjjj")

    print(lq)
    tot = 0
    ls = []
    print(lq,"kkkk")
    for i in lq:
            # try:
             # print(i['suspiciousida'], "aaaaaaaaaaaaaaaaa")
            if i["typea"]=="request":
                print(i,"hhhhhhhhhh")
                res2 = User.objects.filter(LOGIN_id=i['lida'])
                print(res2,'222222222222')
                if res2.exists():
                    res2= res2[0]
                    aadhar_no=res2.aadhar_no
                    v = Vehicle.objects.filter(id= i['vehicleida'],aadhar_no=aadhar_no)
                    print(v,'444444')
                    res3 = Request.objects.filter(requestid=i['reqida'], status='pending')
                    print(res3,'rrrrrr')
                    if res3.exists():
                      if v.exists():
                        v= v[0]
                        a = {
                            'reqida': i['reqida'],
                            'name': res2.username,
                            'vehiclename': v.vehicle_name,
                            'regnnum': v.reg_number,
                            'ownername': v.owner_name,
                            'regdate': v.reg_date,
                            'regplace': v.reg_place,
                            'vehicletype': v.Vehicle_type,
                            'contact': v.contact,
                            'photo': v.photo,
                            'enginenumber': v.engine_number,
                            'chassis_number': v.chase_number,
                            'year_of_manufacturing': v.year_of_manufacturing,
                            'month_of_manufacturing': v.month_of_manufacturing,
                            'status': i['statusa'],                        }
                        ls.append(a)
    print(ls,"helllllll")
    return render(request,'scrap dealer/viewpendscraprequest.html',{'data':ls})


def viewapproved_scrapreq(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber,"hhhh")
    lq = []
    for i in range(blocknumber, 0, -1):
        print(i,"kkkk")
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            print("jjjjj")

    print(lq)
    tot = 0
    ls = []
    print(lq,"kkkk")
    for i in lq:
            # try:
             # print(i['suspiciousida'], "aaaaaaaaaaaaaaaaa")
            if i["typea"]=="request":
                print(i,"hhhhhhhhhh")
                res2 = User.objects.filter(LOGIN_id=i['lida'])
                print(res2,'222222222222')
                if res2.exists():
                    res2= res2[0]
                    aadhar_no=res2.aadhar_no
                    v = Vehicle.objects.filter(id= i['vehicleida'],aadhar_no=aadhar_no)
                    print(v,'444444')
                    res3 = Request.objects.filter(requestid=i['reqida'], status='approved')
                    print(res3,'rrrrrr')
                    if res3.exists():
                      if v.exists():
                        v= v[0]
                        a = {
                            'reqida': i['reqida'],
                            'name': res2.username,
                            'vehiclename': v.vehicle_name,
                            'regnnum': v.reg_number,
                            'ownername': v.owner_name,
                            'regdate': v.reg_date,
                            'regplace': v.reg_place,
                            'vehicletype': v.Vehicle_type,
                            'contact': v.contact,
                            'photo': v.photo,
                            'enginenumber': v.engine_number,
                            'chassis_number': v.chase_number,
                            'year_of_manufacturing': v.year_of_manufacturing,
                            'month_of_manufacturing': v.month_of_manufacturing,
                            'status': i['statusa'],                        }
                        ls.append(a)
    print(ls,"helllllll")
    return render(request,'scrap dealer/viewapprovedscraprequest.html',{'data':ls})

def viewrejected_scrapreq(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber,"hhhh")
    lq = []
    for i in range(blocknumber, 0, -1):
        print(i,"kkkk")
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            print("jjjjj")

    print(lq)
    tot = 0
    ls = []
    print(lq,"kkkk")
    for i in lq:
            # try:
             # print(i['suspiciousida'], "aaaaaaaaaaaaaaaaa")
            if i["typea"]=="request":
                print(i,"hhhhhhhhhh")
                res2 = User.objects.filter(LOGIN_id=i['lida'])
                print(res2,'222222222222')
                if res2.exists():
                    res2= res2[0]
                    aadhar_no=res2.aadhar_no
                    v = Vehicle.objects.filter(id= i['vehicleida'],aadhar_no=aadhar_no)
                    print(v,'444444')
                    res3 = Request.objects.filter(requestid=i['reqida'], status='rejected')
                    print(res3,'rrrrrr')
                    if res3.exists():
                      if v.exists():
                        v= v[0]
                        a = {
                            'reqida': i['reqida'],
                            'name': res2.username,
                            'vehiclename': v.vehicle_name,
                            'regnnum': v.reg_number,
                            'ownername': v.owner_name,
                            'regdate': v.reg_date,
                            'regplace': v.reg_place,
                            'vehicletype': v.Vehicle_type,
                            'contact': v.contact,
                            'photo': v.photo,
                            'enginenumber': v.engine_number,
                            'chassis_number': v.chase_number,
                            'year_of_manufacturing': v.year_of_manufacturing,
                            'month_of_manufacturing': v.month_of_manufacturing,
                            'status': i['statusa'],                        }
                        ls.append(a)
    print(ls,"helllllll")
    return render(request,'scrap dealer/viewrejectedscraprequest.html',{'data':ls})

def view_userrequest_rto(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()
    print(blocknumber,"hhhh")
    lq = []
    for i in range(blocknumber, 0, -1):
        print(i,"kkkk")
        a = web3.eth.get_transaction_by_block(i, 0)
        try:
            decoded_input = contract.decode_function_input(a['input'])
            print(decoded_input)
            print("ku")
            print(decoded_input)
            lq.append(decoded_input[1])
        except Exception as a:
            print("jjjjj")

    print(lq)
    tot = 0
    ls = []
    print(lq,"kkkk")
    for i in lq:
            # try:
             # print(i['suspiciousida'], "aaaaaaaaaaaaaaaaa")
            if i["typea"]=="request":
                print(i,"hhhhhhhhhh")
                res2 = User.objects.filter(LOGIN_id=i['lida'])
                print(res2,'222222222222')
                if res2.exists():
                    res2= res2[0]
                    aadhar_no=res2.aadhar_no
                    v = Vehicle.objects.filter(id= i['vehicleida'],aadhar_no=aadhar_no)
                    print(v,'444444')
                    res3 = Request.objects.filter(requestid=i['reqida'], status='approved')
                    print(res3,'rrrrrr')
                    if res3.exists():
                      if v.exists():
                        v= v[0]
                        a = {
                            'reqida': i['reqida'],
                            'name': res2.username,
                            'vid': v.id,

                            'vehiclename': v.vehicle_name,
                            'regnnum': v.reg_number,
                            'ownername': v.owner_name,
                            'regdate': v.reg_date,
                            'regplace': v.reg_place,
                            'vehicletype': v.Vehicle_type,
                            'contact': v.contact,
                            'photo': v.photo,
                            'enginenumber': v.engine_number,
                            'chassis_number': v.chase_number,
                            'year_of_manufacturing': v.year_of_manufacturing,
                            'month_of_manufacturing': v.month_of_manufacturing,
                            'status': i['statusa'],                        }
                        ls.append(a)
    print(ls,"helllllll")
    return render(request,'RTO/viewuserscraprequest.html',{'data':ls})






# def pending_scrapreq(request):
#     ls=[]
#     with open(compiled_contract_path) as file:
#         contract_json = json.load(file)  # load contract info as JSON
#         contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
#     contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
#     blocknumber = web3.eth.get_block_number()
#     print(blocknumber)
#     l1 = []
#     for i in range(blocknumber, 0, -1):
#
#         a = web3.eth.get_transaction_by_block(i, 0)
#         decoded_input = contract.decode_function_input(a['input'])
#         c = decoded_input[1]
#
#         print(c)
#
#         if c['typea']=="request":
#             m=c["vehicleida"]
#             v=Vehicle.objects.filter(id=m, status="pending")
#             if v.exists():
#                 v=v[0]
#                 s=User.objects.get(aadhar_no=v.aadhar_no)
#
#                 ls.append({
#
#                     'reqida': i['reqida'],
#
#                     'vehicle':v,'u':s,
#                            'name': s.username,
#                            'vehiclename':v.vehicle_name,
#                            'regnnum':v.reg_number,
#                            'ownername':v.owner_name,
#                            'regdate':v.reg_date,
#                            'regplace':v.reg_place,
#                            'vehicletype':v.Vehicle_type,
#                            'contact':v.contact,
#                            'photo':v.photo,
#                            'enginenumber':v.engine_number,
#                            'chassis_number': v.chase_number,
#                            'year_of_manufacturing': v.year_of_manufacturing,
#                            'month_of_manufacturing': v.year_of_manufacturing,
#                            'status': v.status,
#                            })
#
#     return render(request,'scrap dealer/viewpendscraprequest.html',{'data':ls})



def approve_user_request(request,id):
    aa=Request.objects.filter(requestid=id).update(status='approved')
    return HttpResponse('''<script>alert("Forward");window.location='/Myapp/pending_scrapreq/cript>''')

def reject_user_request(request,id):
    aa = Request.objects.filter(requestid=id).update(status='rejected')
    return HttpResponse('''<script>alert("Rejected");window.location='/Myapp/pending_scrapreq/'</script>''')

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
    return render(request,"scrap dealer/scrapdealerindex.html")


# user module

def usersignup(request):
    return render(request, "user/usersignupindex.html")

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
    lic_no = request.POST['textfield15']

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
    u.lic_no = lic_no
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
#
# def viewvehicle(request):
#     a=User.objects.get(LOGIN_id=request.session['lid']).aadhar_no
#     vv = Vehicle.objects.filter(aadhar_no=a)
#     return render(request,"user/viewvhicle.html",{'data':vv})
#

def viewvehicle(request):
    a=User.objects.get(LOGIN_id=request.session['lid']).aadhar_no
    vv = Vehicle.objects.filter(aadhar_no=a)
    v = certificate.objects.filter(VEHICLE__aadhar_no=a)
    certs = [i.VEHICLE.id for i in v]
    return render(request,"user/viewvhicle.html",{'data':vv, 'certs':certs})

def viewvehicle_post(request):
    search = request.POST['textfield']
    vehv = Vehicle.objects.filter(vehicle_name__icontains=search)
    return render(request,"user/viewvhicle.html",{'data':vehv})
#
def userviewcertificate(request,id):
    vs = certificate.objects.filter(VEHICLE_id=id)
    a=User.objects.get(aadhar_no = vs[0].VEHICLE.aadhar_no)
    return render(request, "user/view_usercertificate.html",{'data':vs, 'User':a,'vid':id})



def userviewscrapdealer(request):
    vs = Scrapdealer.objects.filter(status='Approved')
    return render(request, "user/scrapdealerview.html",{'data':vs})


def userviewscrapdealer_post(request):
    search = request.POST['textfield']
    vs = Scrapdealer.objects.filter(name__icontains=search)
    return render(request, "user/scrapdealerview.html",{'data':vs})

def addscraprequest(request,id):
    return render(request,"user/Addscraprequest.html",{'id':id})

#bc
def addscraprequest_post(request,id):
    # vehid = request.POST['vid']
    # scrapdealerid = request.POST['sid']
    # vv=Vehicle.objects.filter(id=id).update(status="pending")
    vv=Vehicle.objects.filter(id=id)


    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        print(contract_abi)
    contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
    blocknumber = web3.eth.get_block_number()

    # scrapdealerid = int(scrapdealerid)
    vehicle_id = int(id)

    if  Vehicle.objects.filter(id=id,status='pending').exists():
        return HttpResponse(
            '''<script>alert("Request Already exist!");window.location='/Myapp/viewvehicle/'</script>''')

    from datetime import datetime
    date = datetime.now().date()
    types = "request"
    status='pending'


    obj = Request()
    obj.status = 'pending'
    rid = blocknumber
    obj.requestid = int(rid)
    obj.save()
    # Vehicle.objects.filter(id=vv).update(status='requested')

    message2 = contract.functions.addrequest(int(rid), int(request.session['lid']),  int(vehicle_id),
                                             str(types), str(date),str(status)).transact({'from': web3.eth.accounts[0]})
    return HttpResponse('''<script>alert("successfully Requested");window.location='/Myapp/viewvehicle/'</script>''')

#bc
def viewscrappingstatus(request):
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
        # print(contract_abi)
        contract = web3.eth.contract(address=deployed_contract_addressa, abi=contract_abi)
        blocknumber = web3.eth.get_block_number()
        ls = []
        for j in range(blocknumber, 0, -1):
            a = web3.eth.get_transaction_by_block(j, 0)
            try:
                # print(contract.decode_function_input(a['input']))
                decoded_input = contract.decode_function_input(a['input'])
                i = decoded_input[1]
                if i['typea'] == 'request' and str(i['lida']) == str(request.session['lid']):
                    print(i)

                    res2 = User.objects.filter(LOGIN_id=i['lida'])
                    if res2.exists():
                        res2 = res2[0]
                        adharno = res2.aadhar_no

                        res = Vehicle.objects.filter(id=i['vehicleida'], aadhar_no=adharno)
                        if res.exists():
                            res = res[0]

                            res3 = Request.objects.filter(requestid=i['reqida'], status="approved")

                            if res3.exists():
                                a = {
                                    'date': i['datea'],
                                    'reqida': i['reqida'],
                                    'vehicle_name': res.vehicle_name,
                                    'owner_name': res.owner_name,
                                    'photo': res.photo,
                                    'reg_number': res.reg_number,
                                    'reg_place': res.reg_place,
                                    'contact': res.contact,
                                    'reg_date': res.reg_date,
                                    'chase_number': res.chase_number,
                                    'engine_number': res.engine_number,
                                    'year_of_manufacturing': res.year_of_manufacturing,
                                    'month_of_manufacturing': res.month_of_manufacturing,
                                    'aadhar_no': res.aadhar_no,
                                    'status': res.status,
                                    'Vehicle_type': res.Vehicle_type,
                                    # 'name': res2.name,
                                    # 'idproof': res2.idproof,
                                    # 'housename': res2.housename,
                                    # 'pincode': res2.pincode,
                                    # 'district': res2.district,
                                    # 'state': res2.state,
                                    # 'place':res2.place,
                                    # 'mail':res2.mail,
                                    # 'phone':res2.phone,
                                }
                                print(a)
                                ls.append(a)
            except Exception as a:
                print(a, 'exception')
                pass
    print(ls)
    return render(request,"User/viewscrappingstatus.html",{'data':ls})


def viewrequeststation(request):
    return render(request, "user/Addscraprequest.html")

def getcertificate(request,id):
    c = certificate.objects.get(VEHICLE_id=id)[0]
    a = User.objects.get(LOGIN_id = request.session['lid']).aadhar_no

    return render(request, "user/view_usercertificate.html",{''})

def user_home(request):
    return render(request,"user/userindex.html")