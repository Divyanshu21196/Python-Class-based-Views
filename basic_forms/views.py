from django.http import HttpResponse
from django.shortcuts import render
from . import forms
from django.views import View

# Create your views here.

#-------------------class based view--------------------------------
class FormsData(View):

    def get(self,request):
        form = forms.FormName()
        return render(request,'basicapp/form_basic.html',{'form':form})

    def post(self,request):
        form = forms.FormName(request.POST)
        if form.is_valid():
            return HttpResponse('Data submitted successfully')




#-------------------function based view--------------------------------
def index(request):
    return render(request,'basicapp/index.html')



# def form_name_view(request):
#     form = forms.FormName()

#     if request.method == 'POST':
#         form = forms.FormName(request.POST)

#         if form.is_valid():
#             print('Form is valid')
#             print(f'Name: {form.cleaned_data["name"]}')
#             print(f'Email: {form.cleaned_data["email"]}')
#             print(f'Text: {form.cleaned_data["text"]}')

#         else:
#             print('no a valid form')            

#     return render(request,'basicapp/form_basic.html',{'form':form})