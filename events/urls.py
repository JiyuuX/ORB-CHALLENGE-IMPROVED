from django.urls import path
from .views import create_event, delete_event, update_event, UpcomingEventListAPIView

urlpatterns = [
    path('create/', create_event, name='create-event'),
    path('delete/<int:event_id>/', delete_event, name='delete-event'),
    path('update/<int:event_id>/', update_event, name='update-event'),
    path('upcoming/', UpcomingEventListAPIView.as_view(), name='upcoming-event-list'),
]
