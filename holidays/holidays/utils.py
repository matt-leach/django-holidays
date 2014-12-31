from django.contrib.auth.models import User
from django.conf import settings


def holidays_remaining(user, year):
    """
    Calculates the number of days remaining
    """
    allowed = settings.YEARLY_HOLS
    taken = 0
    
    hols_this_year = user.holidays.filter(start_date__year = year)
    for hol in hols_this_year:
        taken += (hol.end_date - hol.start_date).days + 1
        
    return allowed - taken
        
    
    