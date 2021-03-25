import math
def cult_grade(zulip_data, git_data, jitsiClasses_data, jitsiSession_data):
    grade = (zulip_data[2] + 
            bool(zulip_data[1]) + 
            git_data[2] + 
            bool(git_data[1]) + 
            0.5*jitsiClasses_data[1] + 
            0.5*jitsiSession_data[1])
    if grade - math.floor(grade) < 0.5:
        grade  = math.floor(grade)
    else: grade =  math.ceil(grade)
    grade = min(10, grade)
    return grade
