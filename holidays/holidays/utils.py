from django.contrib.auth.models import User
from django.conf import settings


def holidays_remaining(user, year):
    """
    Calculates the number of days remaining.
    
    Currently no weekend or bank holiday support.
    """
    allowed = settings.YEARLY_HOLS
    taken = 0
    
    hols_this_year = user.holidays.filter(start_date__year = year)
    
    for hol in hols_this_year:
        taken += (hol.end_date - hol.start_date).days + 1
        
    return allowed - taken
        
    
    
def convert_date(date):
    """
    Converts from dd/mm/yyyy to yyyy-mm-dd
    
    Raises ValueError if fails
    """
    import datetime
    try:
        d = datetime.datetime.strptime(date, '%d/%m/%Y')
        return d.strftime('%Y-%m-%d')
    
    except:
        raise ValueError