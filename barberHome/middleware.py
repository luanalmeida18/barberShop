from django.conf import settings
from django.contrib.auth import logout
from django.utils import timezone
from datetime import datetime

class InactivityLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()
            timeout = settings.INACTIVITY_TIMEOUT

            if last_activity:
                last_activity_dt = datetime.fromisoformat(last_activity)
                if (now - last_activity_dt).seconds > timeout:
                    logout(request)

            request.session['last_activity'] = now.isoformat()

        response = self.get_response(request)
        return response