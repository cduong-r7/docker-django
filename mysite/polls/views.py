#from django.shortcuts import render

#from django.http import HttpResponse


#def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#from django.views.generic import TemplateView

#class IndexView(TemplateView):
#    template_name = 'index.html'


# Create your views here.


from django.shortcuts import render 

def home(request):
    return render(request, 'index.html')

