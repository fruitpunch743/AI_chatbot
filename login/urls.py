from django.urls import path
from . import views
urlpatterns = [
               
               path('login/',views.login_det),
               path('chatbot/<str:mem_id>', views.open_chat),
               path('home/', views.home_page),
               path('home/<str:mem_id>', views.home_page_log),
               path('companies/<str:mem_id>', views.comp),
            ]