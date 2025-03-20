from django.http import HttpResponse


def q3_view(student_id):
    return HttpResponse(f"<h1>Welcome, student number: {student_id}</h1>")
