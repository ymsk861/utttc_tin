from django.urls import path

from . import views




app_name = 'cms'

urlpatterns = [
    path('', views.index1, name='top'),
    path('circleid-1-2/', views.index2, name='circleid-1-2'),
    path('circleid-1-3/', views.index3, name='circleid-1-3'),
    path('circleid-2-1/', views.index21, name='circleid-2-1'),
    path('circleid-2-2/', views.index22, name='circleid-2-2'),
    path('circleid-2-3/', views.index23, name='circleid-2-3'),
    path('circleid-3-1/<int:circle_id>/', views.index31, name='circleid-3-1'),
    path('circleid-3-2/<int:circle_id>/', views.index32, name='circleid-3-2'),
    path('circleid-3-3/<int:circle_id>/', views.index33, name='circleid-3-3'),
    path('userid/', views.mylist, name='userid'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.UserCreate.as_view(), name='signup'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user_update'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user_delete'),
    path('add/', views.add, name='add'),
    path('dislike/', views.dislike, name='dislike'),
    path('delete/<int:circle_id>/', views.delete, name='delete')
]