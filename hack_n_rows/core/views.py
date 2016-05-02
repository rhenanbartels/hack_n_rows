from django.shortcuts import render

from .forms import UploadForm


def home(request):
    template_name = 'home.html'
    context = {}
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            pass
    else:
        upload_form = UploadForm()
    context['upload_form'] = upload_form
    return render(request, template_name, context)
