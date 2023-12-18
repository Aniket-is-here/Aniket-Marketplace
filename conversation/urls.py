from django.urls import path
from . import views


app_name = 'conversation'
urlpatterns = [
    path('',views.inbox,name='inbox'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete_convo,name='delete'),
    path('new/<int:item_pk>/',views.new_conversation,name='new')
]