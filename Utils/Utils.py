
def get_week_day(week_day):
    if week_day == "monday" or week_day == "segunda":
        day = "MON"
    elif week_day == "tuesday" or week_day == "terca" or week_day == "terça":
        day = "TUE"
    elif week_day == "wednesday" or week_day == "quarta":
        day = "WED"
    elif week_day == "thursday" or week_day == "quinta":
        day = "THU"
    elif week_day == "friday" or week_day == "sexta":
        day = "FRI"
    elif week_day == "saturday" or week_day == "sabado" or week_day == "sábado":
        day = "SAT"
    elif week_day == "sunday" or week_day == "domingo":
        day = "SUN"

    return day

