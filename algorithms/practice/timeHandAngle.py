def angle_between_hour_min(hh,mm):
    return 30*(hh%12) - (5.5*mm)

def angle_between_min_sec(mm, ss):
    return 6*(mm%60) - 6*(ss%60)

def angle_between_hour_sec(hh, mm, ss):
    return (30*(hh%12) + .5*mm) - 6*(ss%60)
