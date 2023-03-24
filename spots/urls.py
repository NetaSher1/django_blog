from django.urls import path
from . import views
app_name = 'spots'

urlpatterns = [
    path('spots/', views.home_page, name="spot"),
    path('<slug:slug>/', views.spot_detail, name="detail"),
    path('<slug:slug>/comment/',views.add_comment, name='add_comment')
]
