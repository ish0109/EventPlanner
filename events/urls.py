from django.urls import path
from .views import (
    event_list, event_detail, create_event, update_event, delete_event
)

urlpatterns = [
    path('', event_list, name='event-list'),
    path('<int:event_id>/', event_detail, name='event-detail'),
    path('create/', create_event, name='create-event'),
    path('update/<int:event_id>/', update_event, name='update-event'),
    path('delete/<int:event_id>/', delete_event, name='delete-event'),
]
