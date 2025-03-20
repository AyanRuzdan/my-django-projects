from django.shortcuts import render
def q2_view(request, book_name):
    book_name = book_name.replace('-', ' ').title()
    context = {'book_name': book_name}
    return render(request, 'q2.html', context)
