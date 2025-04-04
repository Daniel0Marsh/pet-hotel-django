from django.urls import path
from .views import SelectDatesView, SelectRoomView, SelectTransportationView, SelectGroomingView, SelectTrainingView, SelectWaterSportsView, SelectMealsView, MoreDetailsView, ConfirmBookingView, BookingCompleteView, CancelBooking

urlpatterns = [
    path('booking/select-dates', SelectDatesView.as_view(), name='select_dates'),
    path('booking/select-room', SelectRoomView.as_view(), name='select_room'),
    path('booking/select-transportation', SelectTransportationView.as_view(), name='select_transportation'),
    path('booking/select-grooming', SelectGroomingView.as_view(), name='select_grooming'),
    path('booking/select-training', SelectTrainingView.as_view(), name='select_training'),
    path('booking/select-water_sports', SelectWaterSportsView.as_view(), name='select_water_sports'),
    path('booking/select-meals', SelectMealsView.as_view(), name='select_meals'),
    path('booking/more_details', MoreDetailsView.as_view(), name='more_details'),
    path('booking/confirm-booking', ConfirmBookingView.as_view(), name='confirm_booking'),
    path('booking/booking-complete', BookingCompleteView.as_view(), name='booking_complete'),
    path('booking/cancel/<int:booking_id>/', CancelBooking.as_view(), name='cancel_booking'),
]
