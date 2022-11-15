from django.contrib import admin
from django.urls import path, include
from home import views
from gdp_analysis import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('Andhra_Pradesh', views.Andhra_Pradesh, name='Andhra_Pradesh'),
    path('states', views.states, name='states'),
    path('contact',views.contact,name='contact'),
    path('analysis',views.analysis,name='analysis'),
    path('Meghalaya', views.Meghalaya, name='Meghalaya'),
    path('Mizoram', views.Mizoram, name='Mizoram'),
    path('Nagaland', views.Nagaland, name='Nagaland'),
    path('Odisha', views.Odisha, name='Odisha'),
    path('Punjab', views.Punjab, name='Punjab'),
    path('Rajasthan', views.Rajasthan, name='Rajasthan'),
    path('Sikkim', views.Sikkim, name='Sikkim'),
    path('Tamil_Nadu', views.Tamil_Nadu, name='Tamil_Nadu'),
    path('Telangana', views.Telangana, name='Telangana'),
    path('Tripura', views.Tripura, name='Tripura'),
    path('Uttar_Pradesh', views.Uttar_Pradesh, name='Uttar_Pradesh'),
    path('Uttarakhand', views.Uttarakhand, name='Uttarakhand'),
    path('West_Bengal', views.West_Bengal, name='West_Bengal'),
    path('Delhi', views.Delhi, name='Delhi'),
    path('Puducherry', views.Puducherry, name='Puducherry'),
    path('analysis2',views.analysis2,name='analysis2'),
    path('analysis3',views.analysis3,name='analysis3'),
    path('Andaman_and_nicobar', views.Andaman_and_nicobar, name='Andaman_and_nicobar'),
    path('Arunachal_Pradesh',views.Arunachal_Pradesh, name='Arunachal_Pradesh'),
    path('Assam',views.Assam, name='Assam'),
    path('Bihar',views.Bihar, name='Bihar'),
    path('Chandigarh',views.Chandigarh, name='Chandigarh'),
    path('Chattisgarh',views.Chattisgarh, name='Chattisgarh'),
    path('Goa',views.Goa, name='Goa'),   
    path('Gujarat',views.Gujarat, name='Gujarat'),
    path('Haryana',views.Haryana, name='Haryana'),
    path('Himachal_Pradesh',views.Himachal_Pradesh, name='Himachal_Pradesh'),
    path('Jammu_and_Kashmir',views.Jammu_and_Kashmir, name='Jammu_and_Kashmir'),
    path('Jharkhand',views.Jharkhand, name='Jharkhand'),
    path('Karnataka',views.Karnataka, name='Karnataka'),
    path('Kerala',views.Kerala, name='Kerala'),
    path('Madhya_Pradesh',views.Madhya_Pradesh, name='Madhya_Pradesh'), 
    path('Maharashtra',views.Maharashtra, name='Maharashtra'),
    path('Manipur',views.Manipur, name='Manipur'),
     path('analysis4',views.analysis4,name='analysis4'),
     path('Chhattisgarh',views.Chhattisgarh,name='Chhattisgarh'),
     
  
    


  



    
 
    
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)