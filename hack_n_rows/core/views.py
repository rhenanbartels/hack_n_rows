from django.http import HttpResponse
from django.shortcuts import render

from .forms import UploadForm
from hack_n_rows.core.utils import ConvertedFile, get_file_extension

#TODO: These are not view responsibilties. Create modules to deal with the files
#TODO: view is getting to big. Refactor!
def home(request):
    template_name = 'home.html'
    context = {}
    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            file_to_convert = upload_form.cleaned_data['file_to_convert']
            choosen_file_extension =  upload_form.cleaned_data['options']
            uploaded_file_extension = get_file_extension(file_to_convert.name)
            if is_extensions_equals(uploaded_file_extension, choosen_file_extension):
                upload_form.add_error("file_to_convert", "Select another extension")
                context['upload_form'] = upload_form
                return render(request, template_name, context)
            else:
                uploaded_file_name = _prepare_download_file_name(file_to_convert.name)
                converted_file_object = ConvertedFile()
                converted_file_object.convert(
                        file_to_convert,
                        uploaded_file_extension,
                        choosen_file_extension.lower()
                )
                converted_file_object.unlink()
                return _create_file_response(
                        converted_file_object,
                        uploaded_file_name,
                        choosen_file_extension
                )
    else:
        upload_form = UploadForm()
    context['upload_form'] = upload_form
    return render(request, template_name, context)

def _create_file_response(file_object, uploaded_file_name, file_extension):
    response = HttpResponse(file_object.temp_file.read(),
            content_type=file_object.file_type)
    response['Content-Disposition'] = 'attachment; filename={0}.{1}'.\
            format(uploaded_file_name, file_extension)
    return response

def _prepare_download_file_name(file_name):
    return ''.join(file_name.split(".")[0:-1])

def is_extensions_equals(uploaded_file_name, choosen_file_extension):
    return uploaded_file_name == choosen_file_extension

