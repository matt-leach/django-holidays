from django.views import generic
from django.contrib.auth.models import User

from holidays.models import Holiday



class AddHolidayView(generic.CreateView):
    model = Holiday
    
    
class GetYearlyHolidaysView(generic.TemplateView):
    template_name = "holidays/holidayTable.html"
    
    def get_context_data(self, **kwargs):
        context = super(GetYearlyHolidaysView, self).get_context_data(**kwargs)
        
        # This can easily fail
        user_id = self.request.GET["userid"]
        context['staff'] = User.objects.get(id=user_id)
        context['year'] = self.request.GET["year"]

        return context