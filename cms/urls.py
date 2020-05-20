from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.TopView.as_view(), name='top'),
    path('circleid-1-1/', views.Next11View.as_view(), name='circleid-1-1'),
    path('circleid-1-2/', views.Next12View.as_view(), name='circleid-1-2'),
    path('circleid-1-3/', views.Next13View.as_view(), name='circleid-1-3'),
    path('circleid-2-1/', views.Next21View.as_view(), name='circleid-2-1'),
    path('circleid-2-2/', views.Next22View.as_view(), name='circleid-2-2'),
    path('circleid-2-3/', views.Next23View.as_view(), name='circleid-2-3'),
    path('circleid-3-1/', views.Next31View.as_view(), name='circleid-3-1'),
    path('circleid-3-2/', views.Next32View.as_view(), name='circleid-3-2'),
    path('circleid-3-3/', views.Next33View.as_view(), name='circleid-3-3'),
    path('userid/', views.NextuseridView.as_view(), name='userid'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
]