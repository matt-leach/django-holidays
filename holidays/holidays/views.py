from django.views import generic
from holidays.models import Holiday

class AddHolidayView(generic.CreateView):
    model = Holiday