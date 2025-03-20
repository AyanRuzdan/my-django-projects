from django.shortcuts import render


def q1_view(request, post_id):
    context = {'post_id': post_id}
    return render(request, "q1.html", context)
