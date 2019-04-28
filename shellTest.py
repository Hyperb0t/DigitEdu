from main import restApi
from main.models import Student, Subject, PointList

last_sem = list(PointList.objects.filter(subject=Subject.objects.get(pk=1)).order_by('semester'))[-1].semester
points = PointList.objects.filter(subject=Subject.objects.get(pk=1), semester=last_sem).order_by(
    'point').reverse()
print(points)