from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[

    ############### admin
    path('add/',views.addadmin,name='addadmin'),
    path('loginadmin/',views.login_check,name='login_checkadmin'),
    path('loginadminview/',views.loginviewadmin,name='loginadminview'),




    path('logincustomer/',views.customerlogin_check,name='login_checkcustomer'),
    path('logincustomerview/',views.loginviewcustomer,name='logincustomerview'),






    path('addapi/',views.AddCustomer,name='AddCustomer'),
    path('viewallapi/',views.ViewCustomerall,name='ViewCustomerall'),
    path('viewapi/<fetchid>',views.ViewCustomer,name='ViewCustomer'),
    path('upload/',views.upload,name='upload'),
    path('upload_image/',views.upload_image,name='upload_image'),



    #####################################################################################################


    path('register/',views.register,name='register'),
    path('searchview/',views.search_customer,name='search_customer'),
    path('search/',views.searchapi,name='searchapi'),
    path('view/',views.viewall,name='viewall'),

    path('update/',views.update,name='update'),
    path('update_api/',views.update_data_read,name='update_data_read'),
    path('update_search_api/',views.update_search_api,name='update_search_api'),

    path('delete_search_api/',views.delete_search_api,name='delete_search_api'),
    path('delete/',views.delete,name='delete'),
    path('delete_api/',views.delete_data_read,name='delete_data_read'),



    ### HTML
    path('welcome/',views.myHeaderPage,name='myHeaderPage'),

    path('prepaidplans/',views.myPrepaidplans,name='myPrepaidplans'),
    path('postpaidplans/',views.myPostpaidplans,name='myPostpaidplans'),

    path('viewallprepaidplans/',views.myViewAllPrepaidplans,name='myViewAllPrepaidplans'),
    path('viewallpostpaidplans/',views.myViewAllPostpaidplans,name='myViewAllPostpaidplans'),

    path('deleteprepaidplans/',views.myDeleteprepaidplans,name='myDeleteprepaidplans'),
    path('deletepostpaidplans/',views.myDeletepostpaidplans,name='myDeletepostpaidplans'),

    

    #### API 
    path('add_prepaidplans/',views.Prepaidplans_Page,name='Prepaidplans_Page'),
    path('add_postpaidplans/',views.Postpaidplans_Page,name='Postpaidplans_Page'),
    
    path('viewall_prepaidplans/',views.Prepaidplans_List,name='Prepaidplans_List'),
    path('viewall_postpaidplans/',views.Postpaidplans_List,name='Postpaidplans_List'),

    path('delete_prepaidplans/<id>',views.Prepaidplans_Delete,name='Prepaidplans_Delete'),
    path('delete_postpaidplans/<id>',views.Postpaidplans_Delete,name='Postpaidplans_Delete'),

    path('deletereadprepaidplans/',views.DeleteReadprepaidplans,name='Deleteprepaidplans'),
    path('deletereadpostpaidplans/',views.DeleteReadpostpaidplans,name='Deletepostpaidplans'),

    path('delete_prepaidplans/',views.DeleteSearchprepaidplans,name='DeleteSearchprepaidplans'),
    path('delete_postpaidplans/',views.DeleteSearchpostpaidplans,name='DeleteSearchpostpaidplans'),


#############QUERY######################
    path('addquery/',views.AddQuery,name='Addqueryapi'),
    path('deletequery/<id>',views.Query_Delete,name='query_Deleteapi'),
    path('viewallq/',views.Query_List,name='Query_List'),
    path('deletereadquery/',views.DeleteReadQuery,name='Deletereadquery'),
    path('deletequeries/',views.DeleteSearchQuery,name='DeleteSearchprepaidplans'),








path('registerquery/',views.registerquery,name='registerquerypage'),
path('viewallqueries/',views.myViewAllQuery,name='myViewAllQuerypage'),
path('deletequery/',views.myDeleteQuery,name='myDeleteQuerypage'),







##########DONGLE HTML##################
    path('dongleprepaidplans/',views.myDonglePrepaidplans,name='myDonglePrepaidplans'),
    path('donglepostpaidplans/',views.myDonglePostpaidplans,name='myDonglePostpaidplans'),

    path('dongleviewallprepaidplans/',views.myDongleViewAllPrepaidplans,name='myDongleViewAllPrepaidplans'),
    path('dongleviewallpostpaidplans/',views.myDongleViewAllPostpaidplans,name='myDongleViewAllPostpaidplans'),

    path('dongledeleteprepaidplans/',views.myDongleDeleteprepaidplans,name='myDongleDeleteprepaidplans'),
    path('dongledeletepostpaidplans/',views.myDongleDeletepostpaidplans,name='myDongleDeletepostpaidplans'),





#####DONGLE API#################
    path('add_dongleprepaidplans/',views.DonglePrepaidplans_Page,name='DonglePrepaidplans_Page'),
    path('add_donglepostpaidplans/',views.DonglePostpaidplans_Page,name='DonglePostpaidplans_Page'),

    path('viewall_dongleprepaidplans/',views.DonglePrepaidplans_List,name='DonglePrepaidplans_List'),
    path('viewall_donglepostpaidplans/',views.DonglePostpaidplans_List,name='DonglePostpaidplans_List'),
 
    path('delete_dongleprepaidplans/<id>',views.DonglePrepaidplans_Delete,name='DonglePrepaidplans_Delete'),
    path('delete_donglepostpaidplans/<id>',views.DonglePostpaidplans_Delete,name='DonglePostpaidplans_Delete'),

    path('dongledeletereadprepaidplans/',views.DongleDeleteReadprepaidplans,name='DongleDeleteprepaidplans'),
    path('dongledeletereadpostpaidplans/',views.DongleDeleteReadpostpaidplans,name='DongleDeletepostpaidplans'),

    path('dongledelete_prepaidplans/',views.DongleDeleteSearchprepaidplans,name='DongleDeleteSearchprepaidplans'),
    path('dongledelete_postpaidplans/',views.DongleDeleteSearchpostpaidplans,name='DongleDeleteSearchpostpaidplans'),




    ##############CUSTOMER HOMPAGE URLS#####################3
    path('home/',views.Home_Page,name='Home_Page'),
    path('contactus/',views.contact_us,name='contact_us'),
    path('aboutus/',views.About_us,name='about_us'),


    path('rechargeprepaidplans/',views.customerrechargepre,name='customerrechargepre'),
    path('rechargeprepaid/',views.myprepaidrecharge,name='myprepaidrecharge'),

    path('prepaidviewonly/',views.myViewonlyPrepaidplans,name='myprepaidrecharge'),
    path('postpaidviewonly/',views.myViewonlyPostpaidplans,name='myprepaidrecharge'),




    path('logout/',views.logout_user,name='logout_user'),




    




    
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)