from django.shortcuts import render

# Create your views here.
def groups_page(request):
    return render(request, "GroupUp/create_groups_page.html")