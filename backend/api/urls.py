app_name = 'api'
from django.urls import path 
from userauths import views as userauth_views
from customer import views as customer_views 
from vendor import views as vendor_views
from agent import views as agent_views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns = [
    # Authentication
    path('user/register/', userauth_views.RegisterView.as_view(), name='auth_register'),
    path('user/login/', userauth_views.LoginView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/logout/',userauth_views.LogoutView.as_view(), name='logout_user'),
    
    #Customer 
    path('customer/list/vendors/',customer_views.ListVendors.as_view()),
    path('customer/list/vehicles/<int:vendor_id>/', customer_views.ListVehiclesByVendor.as_view()),
    path('customer/create/order/', customer_views.CreateOrder.as_view()),
    path('customer/list/orders/<int:customer_id>/', customer_views.ListOrders.as_view()),
    path('customer/checkin/',customer_views.CheckinVehicle.as_view()),
    path('customer/checkins/info/<int:customer_id>/',customer_views.CheckinStatus.as_view()),
    
    #Vendor 
    path('vendor/assign/qa/',vendor_views.AssignQa.as_view()),
    
    
    #QA Guy 
    path('agent/qa/list/checkis/<int:qa_id>/',agent_views.ListCheckinItemsForQA.as_view()),
    
    #Security Guy

]

