class TimeCard:

    def __init__(self, time_in, time_out, work_hours):
        self._time_in = time_in
        self._time_out = time_out
        self._work_hours = work_hours

    @property
    def work_hours(self):
        return self._work_hours

    @work_hours.setter
    def work_hours(self, work_hours):
        self._work_hours = work_hours
