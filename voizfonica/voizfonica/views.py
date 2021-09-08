from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from voizfonica.models import Admin ,Customer,Prepaidplans,Postpaidplans,Query,DonglePrepaidplans,DonglePostpaidplans
from voizfonica.serializers import AdminSerializer,CustomerSerializer,PrepaidplansSerializer,PostpaidplansSerializer,QuerySerializer,DonglePrepaidplansSerializer,DonglePostpaidplansSerializer,PrepaidplanusageSerializer
from django.contrib.auth import logout

from rest_framework.parsers import JSONParser
from rest_framework import status
import requests
from django.core.files.storage import FileSystemStorage
@csrf_exempt
def addadmin(request):
    if (request.method=="POST"):
        
       

        mydata=JSONParser().parse(request)
        admin_serialize=AdminSerializer(data=mydata)
        
        if (admin_serialize.is_valid()):
            admin_serialize.save()
            
            return JsonResponse(admin_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'adminview.html',{"data":admin_serializer.data})
        


    else:
        return HttpResponse("Invalid Credentials")

def loginviewadmin(request):
    return render(request,"adminlogin.html")


@csrf_exempt
def AddCustomer(request):

#Kanchana implementation

    # if(request.method=="POST"):
    #     # mydata=JSONParser().parse(request)
    #     customer_serialize=CustomerSerializer(data=request.POST)
    #     if(customer_serialize.is_valid()):
    #         customer_serialize.save()
    #         return redirect(viewall)
    #         # return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
    #     else:
    #         return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)    
      
    # else:
    #     return HttpResponse("No GET method Allowed",status=status.HTTP_404_NOT_FOUND)
    
###############################################################################################################
#implementation from userblog preventing duplicate mobile number

    if (request.method == "POST"):

        try:
            getCname = request.POST.get("Cname")
            getCadhar = request.POST.get("Cadhar")
            getCemail = request.POST.get("Cemail")
            getCaddress = request.POST.get("Caddress")
            getCalternatemobilenumber = request.POST.get("Calternatemobilenumber")
            getTypeofcustomer = request.POST.get("Typeofcustomer")
            getNewnumber = request.POST.get("Newnumber")
            getpassword = request.POST.get("password")
            getCustomer = Customer.objects.filter(Newnumber=getNewnumber)
            customer_serialiser = CustomerSerializer(getCustomer, many=True)
            print(customer_serialiser.data)
            if (customer_serialiser.data):
                
                return HttpResponse("customer Already Exists")


            else:
                customer_serialize = CustomerSerializer(data=request.POST)
                if (customer_serialize.is_valid()):
                    customer_serialize.save()  #Save to Db
                    #return redirect(loginview)
                    return redirect(viewall)
 
                else:
                    return HttpResponse("Error in Serilization",status=status.HTTP_400_BAD_REQUEST)        
            
            
        except Customer.DoesNotExist:
            return HttpResponse("Invalid customername or Password ", status=status.HTTP_404_NOT_FOUND)
        except:
            return HttpResponse("Something went wrong")


     
        
   

    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


def register(request):
    return render(request,'register.html')
def viewall(request): 
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewallapi/").json()
    return render(request,'view.html',{"data":fetchdata})

############################################################################################################

@csrf_exempt
def ViewCustomerall(request):
    if(request.method=="GET"):
        customer=Customer.objects.all()
        customer_serializer=CustomerSerializer(customer,many=True)
        return JsonResponse(customer_serializer.data,safe=False)


@csrf_exempt
def ViewCustomer(request,fetchid):
    try:
        customer=Customer.objects.get(id=fetchid)
        if(request.method=="GET"):
            customer_serializer=CustomerSerializer(customer)
            return JsonResponse(customer_serializer.data,safe=False,status=status.HTTP_200_OK)
        if(request.method=="DELETE"):
            customer.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
        if(request.method=="PUT"):
            mydata=JSONParser().parse(request)
            customer_serialize=CustomerSerializer(customer,data=mydata)
            if(customer_serialize.is_valid()):
                customer_serialize.save()
                return JsonResponse(customer_serialize.data,status=status.HTTP_200_OK)
            else:
                return JsonResponse(customer_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    
    except Customer.DoesNotExist:
        return HttpResponse("Invalid ID ",status=status.HTTP_404_NOT_FOUND)



##################### search
def search_customer(request):
    return render(request,'search.html') 

@csrf_exempt
def searchapi(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"search.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND)
##################################

def update(request):
    return render(request,'update.html') 

@csrf_exempt
def update_search_api(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"update.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid Mobile number",status=status.HTTP_404_NOT_FOUND) 

@csrf_exempt
def update_data_read(request):
    getId=request.POST.get("newid")

    getcname=request.POST.get("newcname")    
    getcadhar=request.POST.get("newcadhar")
    getcemail=request.POST.get("newcemail")
    getcaddress=request.POST.get("newcaddress")
    getcalternatemobilenumber=request.POST.get("newalternatemobilenumber")
    gettypeofcustomer=request.POST.get("newtypeofcustomer")
    getnewnumber=request.POST.get("newcnumber")
    
    mydata={'Cname':getcname,'Cadhar':getcadhar,'Cemail':getcemail,'Caddress':getcaddress,'Calternatemobilenumber':getcalternatemobilenumber,'Typeofcustomer':gettypeofcustomer,'Newnumber':getnewnumber}
    jsondata=json.dumps(mydata)
    ApiLink="http://127.0.0.1:8000/voizfonica/viewapi/" + getId
    requests.put(ApiLink,data=jsondata)
    return redirect(viewall) 

####################### delete

def delete(request):
    return render(request,'delete.html')  

@csrf_exempt
def delete_data_read(request):
   
    getId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/viewapi/" + getId
    requests.delete(ApiLink)
    return redirect(viewall)

@csrf_exempt
def delete_search_api(request):
    try:
        getnumber=request.POST.get("Newnumber")
        getnumbers=Customer.objects.filter(Newnumber=getnumber)
        customer_serialize=CustomerSerializer(getnumbers,many=True)
        return render(request,"delete.html",{"data":customer_serialize.data})
    except:   
        return HttpResponse("Invalid mobile number")

def upload(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'register.html')

def upload_image(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document_image']
        # print(uploaded_file.name)
        # print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'register.html')




################PLANS###################
#### Add Prepaid Plans
@csrf_exempt
def Prepaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplans_serialize=PrepaidplansSerializer(data=request.POST)
        if(prepaidplans_serialize.is_valid()):
            prepaidplans_serialize.save()
            return redirect(myViewAllPrepaidplans)
            # return JsonResponse(prepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Add Postpaid Plan
@csrf_exempt
def Postpaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        postpaidplans_serialize=PostpaidplansSerializer(data=request.POST)
        if(postpaidplans_serialize.is_valid()):
            postpaidplans_serialize.save()
            return redirect(myViewAllPostpaidplans)
            # return JsonResponse(postpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Viewall Prepaid Plan
@csrf_exempt
def Prepaidplans_List(request):
    if(request.method=="GET"):
        prepaidplan=Prepaidplans.objects.all()
        prepaidplans_serializer=PrepaidplansSerializer(prepaidplan,many=True)
        return JsonResponse(prepaidplans_serializer.data,safe=False)


#### Viewall Postpaid Plan
@csrf_exempt
def Postpaidplans_List(request):
    if(request.method=="GET"):
        postpaidplan=Postpaidplans.objects.all()
        postpaidplans_serializer=PostpaidplansSerializer(postpaidplan,many=True)
        return JsonResponse(postpaidplans_serializer.data,safe=False)

#### Delete Prepaid Plans
@csrf_exempt
def Prepaidplans_Delete(request,id):
    try:
        prepaidplan=Prepaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                prepaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete Postpaid Plans
@csrf_exempt
def Postpaidplans_Delete(request,id):
    try:
        postpaidplan=Postpaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
            postpaidplan.delete()
            return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete read Prepaid Plans
@csrf_exempt
def DeleteReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_prepaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPrepaidplans)

#### Delete Search Prepaid plans
@csrf_exempt
def DeleteSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getCalls=Prepaidplans.objects.filter(price=getPrice)
        prepaidplans_serializer=PrepaidplansSerializer(getCalls,many=True)
        return render(request,"deletepre.html",{"data":prepaidplans_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Prepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

#### Delete read Postpaid Plans
@csrf_exempt
def DeleteReadpostpaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_postpaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllPostpaidplans)

#### Delete Search Postpaid plans
@csrf_exempt
def DeleteSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getCalls=Postpaidplans.objects.filter(price=getPrice)
        postpaidplans_serializer=PostpaidplansSerializer(getCalls,many=True)
        return render(request,"deletepost.html",{"data":postpaidplans_serializer.data})
        #return JsonResponse(postpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Postpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")



#### Header page
def myHeaderPage(request):
    return render(request,'header.html')

### Register Prepaid Plans
def myPrepaidplans(request):
    return render(request,'prepaidplans.html')

### Register Postpaid Plans
def myPostpaidplans(request):
    return render(request,'postpaidplans.html')

#### Viewall Prepaid plans
def myViewAllPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_prepaidplans/").json()
    return render(request,'viewallpre.html',{"data":fetchdata})

#### Viewall Postpaid plans
def myViewAllPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_postpaidplans/").json()
    return render(request,'viewallpost.html',{"data":fetchdata})

### Delete Prepaid Plans
@csrf_exempt
def myDeleteprepaidplans(request):
    return render(request,'deletepre.html')

### Delete Postpaid Plans
@csrf_exempt
def myDeletepostpaidplans(request):
    return render(request,'deletepost.html')



#### Add Dongle Prepaid Plans
@csrf_exempt
def DonglePrepaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        dongleprepaidplans_serialize=DonglePrepaidplansSerializer(data=request.POST)
        if(dongleprepaidplans_serialize.is_valid()):
            dongleprepaidplans_serialize.save()
            return redirect(myDongleViewAllPrepaidplans)
            # return JsonResponse(dongleprepaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


#### Viewall Dongle Prepaid Plan
@csrf_exempt
def DonglePrepaidplans_List(request):
    if(request.method=="GET"):
        dongleprepaidplan=DonglePrepaidplans.objects.all()
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(dongleprepaidplan,many=True)
        return JsonResponse(dongleprepaidplans_serializer.data,safe=False)


#### Delete Dongle Prepaid Plans
@csrf_exempt
def DonglePrepaidplans_Delete(request,id):
    try:
        dongleprepaidplan=DonglePrepaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                dongleprepaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)


#### Delete Dongle read Prepaid Plans
@csrf_exempt
def DongleDeleteReadprepaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_dongleprepaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myDongleViewAllPrepaidplans)


#### Delete Dongle Search Prepaid plans
@csrf_exempt
def DongleDeleteSearchprepaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getData=DonglePrepaidplans.objects.filter(price=getPrice)
        dongleprepaidplans_serializer=DonglePrepaidplansSerializer(getData,many=True)
        return render(request,"dongledeletepre.html",{"data":dongleprepaidplans_serializer.data})
        #return JsonResponse(dongleprepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePrepaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")


### Register Dongle  Prepaid Plans
def myDonglePrepaidplans(request):
    return render(request,'dongleprepaidplans.html')


#### Viewall Dongle Prepaid plans
def myDongleViewAllPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_dongleprepaidplans/").json()
    return render(request,'dongleviewallpre.html',{"data":fetchdata})


### Delete  Dongle Prepaid Plans
@csrf_exempt
def myDongleDeleteprepaidplans(request):
    return render(request,'dongledeletepre.html')

####################################################

#### Add Dongle Postpaid Plans
@csrf_exempt
def DonglePostpaidplans_Page(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        donglepostpaidplans_serialize=DonglePostpaidplansSerializer(data=request.POST)
        if(donglepostpaidplans_serialize.is_valid()):
            donglepostpaidplans_serialize.save()
            return redirect(myDongleViewAllPostpaidplans)
            # return JsonResponse(donglepostpaidplans_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

#### Viewall Dongle Postpaid Plan
@csrf_exempt
def DonglePostpaidplans_List(request):
    if(request.method=="GET"):
        donglepostpaidplan=DonglePostpaidplans.objects.all()
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(donglepostpaidplan,many=True)
        return JsonResponse(donglepostpaidplans_serializer.data,safe=False)

#### Delete Dongle Postpaid Plans
@csrf_exempt
def DonglePostpaidplans_Delete(request,id):
    try:
        donglepostpaidplan=DonglePostpaidplans.objects.get(id=id)
        if (request.method=="DELETE"):  
                donglepostpaidplan.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

#### Delete Dongle read Postpaid Plans
@csrf_exempt
def DongleDeleteReadpostpaidplans(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/delete_donglepostpaidplans/" + getNewId
    requests.delete(ApiLink)
    return redirect(myDongleViewAllPostpaidplans)

#### Delete Dongle Search Postpaid plans
@csrf_exempt
def DongleDeleteSearchpostpaidplans(request):
    try:
        getPrice=request.POST.get("price")
        getData=DonglePostpaidplans.objects.filter(price=getPrice)
        donglepostpaidplans_serializer=DonglePostpaidplansSerializer(getData,many=True)
        return render(request,"dongledeletepost.html",{"data":donglepostpaidplans_serializer.data})
        #return JsonResponse(donglepostpaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except DonglePostpaidplans.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

### Register Dongle Postpaid Plans
def myDonglePostpaidplans(request):
    return render(request,'donglepostpaidplans.html')

#### Viewall Dongle Postpaid plans
def myDongleViewAllPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_donglepostpaidplans/").json()
    return render(request,'dongleviewallpost.html',{"data":fetchdata})

### Delete  Dongle Postpaid Plans
@csrf_exempt
def myDongleDeletepostpaidplans(request):
    return render(request,'dongledeletepost.html')


###########################QUERY#######################################
@csrf_exempt
def AddQuery(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        Query_serialize=QuerySerializer(data=request.POST)
        if(Query_serialize.is_valid()):
            Query_serialize.save()
            return redirect(myViewAllQuery)
            # return JsonResponse(Query_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in Serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET Method Not Allowed",status=status.HTTP_404_NOT_FOUND)

def registerquery(request):
    return render(request,'registerquery.html')

@csrf_exempt
def Query_List(request):
    if(request.method=="GET"):
        q1=Query.objects.all()
        q_serializer=QuerySerializer(q1,many=True)
        return JsonResponse(q_serializer.data,safe=False)

@csrf_exempt
def Query_Delete(request,id):
    try:
        q1=Query.objects.get(id=id)
        if (request.method=="DELETE"):  
                q1.delete()
                return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def DeleteReadQuery(request):
    getNewId=request.POST.get("newid")
    ApiLink="http://127.0.0.1:8000/voizfonica/deletequeries/" + getNewId
    requests.delete(ApiLink)
    return redirect(myViewAllQuery)

@csrf_exempt
def DeleteSearchQuery(request):
    try:
        getmobile=request.POST.get("mobile")
        getmob=Query.objects.filter(mobile=getmobile)
        q_serializer=QuerySerializer(getmob,many=True)
        return render(request,"deletequery.html",{"data":q_serializer.data})
        #return JsonResponse(prepaidplans_serializer.data,safe=False,status=status.HTTP_200_OK)
    except Query.DoesNotExist:
        return HttpResponse("Invalid",status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something Wrong")

@csrf_exempt
def myDeleteQuery(request):
    return render(request,'deletequery.html')

def myViewAllQuery(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewallq/").json()
    return render(request,'viewallquery.html',{"data":fetchdata})




#############CUSTOMER HOMEPAGE#############

# Create your views here.
def Home_Page(request):
    return render(request,'home.html')


def About_us(request):
    return render(request,'aboutus.html')

def contact_us(request):
    return render(request,'contact.html')


###PREPAID RECHARGE
def myprepaidrecharge(request):
    return render(request,'rechargepre.html')


#####PREPAID RECHARGE API
@csrf_exempt
def customerrechargepre(request):
    if(request.method=="POST"):
        # mydata=JSONParser().parse(request)
        prepaidplansusage_serialize=PrepaidplanusageSerializer(data=request.POST)
        if(prepaidplansusage_serialize.is_valid()):
            prepaidplansusage_serialize.save()
            return HttpResponse("RECHARGED SUCCESSFULLY")
            
            #return response.JsonResponse(prepaidplansusage_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("Get Method Not Allowed",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def customerlogin_check(request):
    #login check
    try:
        getmobile = request.POST.get("Newnumber")
        getPassword = request.POST.get("password")
        getUsers = Customer.objects.filter(Newnumber=getmobile, password=getPassword)
        user_serialiser = CustomerSerializer(getUsers, many=True)
        print(user_serialiser.data)
        if (user_serialiser.data):
            for i in user_serialiser.data:
                getId = i["id"]
                getName = i["Cname"]
                getmobile= i["Newnumber"]
            request.session['uid'] = getId
            request.session['uname'] = getName
            data={"Cname":getName,"Newnumber":getmobile}

            return  render(request,"customerview.html",{"data":data})
            


        else:
            # return HttpResponse("Invalid Credentials")     
            return render(request,"home.html")     
            
            
    except Customer.DoesNotExist:
        return HttpResponse("Invalid Mobile number or Password ", status=status.HTTP_404_NOT_FOUND)
    except:
        return HttpResponse("Something went wrong")

def loginviewcustomer(request):
    return render(request, 'customerlogin.html')

def logout_user(request):
        logout(request)
        # messages.success(request, ("You Were Logged Out!"))
        template='home.html'
        return render(request,template)     


#### Viewall Prepaid plans for customer
def myViewonlyPrepaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_prepaidplans/").json()
    return render(request,'prepaidviewonly.html',{"data":fetchdata})

#### Viewall Postpaid plans fro customer
def myViewonlyPostpaidplans(request):
    fetchdata=requests.get("http://127.0.0.1:8000/voizfonica/viewall_postpaidplans/").json()
    return render(request,'postpaidviewonly.html',{"data":fetchdata})















