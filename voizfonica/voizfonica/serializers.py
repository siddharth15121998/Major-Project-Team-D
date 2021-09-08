from rest_framework import serializers
from voizfonica.models import Admin ,Customer,Prepaidplans,Postpaidplans,Query,DonglePostpaidplans,DonglePrepaidplans,Prepaidplansusage

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=("id","adminname","username","password")



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','Cname','Cadhar','Cemail','Caddress','Calternatemobilenumber','Typeofcustomer','Newnumber','password')

class PrepaidplansSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prepaidplans
        fields=('id','price','calls','validity','data','messages','offers')

class PostpaidplansSerializer(serializers.ModelSerializer):
    class Meta:
        model=Postpaidplans
        fields=('id','price','calls','data','messages','offers')

class QuerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Query
        fields=('id','name','mobile','message')


class DonglePrepaidplansSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonglePrepaidplans
        fields=('id','price','data','validity','offers')

class DonglePostpaidplansSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonglePostpaidplans
        fields=('id','price','data','offers')


####PREPAID PLAN USAGE############
class PrepaidplanusageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prepaidplansusage
        fields=('id','mobilenumber','plan')




