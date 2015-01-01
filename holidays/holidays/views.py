import json

from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponse
from django.template.loader import render_to_string

from holidays.models import Holiday
from holidays.utils import convert_date

THIS_YEAR = 2015


class AddHolidayView(generic.CreateView):
    model = Holiday
    
    def post(self, request, *args, **kwargs):
        print request.POST
        return super(AddHolidayView, self).post(request, *args, **kwargs)
    
    
class GetYearlyHolidaysView(generic.TemplateView):
    template_name = "holidays/holidayTable.html"
    
    def get_context_data(self, **kwargs):
        context = super(GetYearlyHolidaysView, self).get_context_data(**kwargs)
        
        # This can easily fail
        user_id = self.request.GET["userid"]
        context['staff'] = User.objects.get(id=user_id)
        context['year'] = self.request.GET["year"]

        return context
    
    
def add_holiday(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.POST.get("user_id"))
        
        if user != request.user:
            return HttpResponseForbidden()
        
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        
        context = {"staff": user, "year": THIS_YEAR, "current": True, "user": user}
        
        start_fail, end_fail = False, False
        try:
            start_date = convert_date(start_date)
        except ValueError:
            start_fail = True

        try:
            end_date = convert_date(end_date)
        except ValueError:
            end_fail = True
            
        if not start_fail or not end_fail:
            hol = Holiday(start_date=start_date, end_date=end_date, user=user)
            hol.save()
            
        else:            
            context["end_fail"] = start_fail
            context["start_date"] = start_date
            context["start_fail"] = end_fail
            context["end_date"] = end_date
        
        print context
        
        return HttpResponse(json.dumps(render_to_string("holidays/holidayTable.html", context)), content_type="application/json")
    else:
        return HttpResponseForbidden()
    
    
    
    
    
    
    
    
    