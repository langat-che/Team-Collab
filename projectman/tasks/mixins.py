from datetime import datetime

class WeekMixin:
    def get_week_start_date(self):
        today = datetime.today()
        week_start = today - datetime.timedelta(days=today.weekday())
        return week_start

    def get_week_end_date(self):
        week_start = self.get_week_start_date()
        week_end = week_start + datetime.timedelta(days=6)
        return week_end