from django.shortcuts import render

# Create your views here.
def loginUser(request):
	return render(request, 'login.html')