from django import forms

OPTIONS = (
        (1, 'CSV'),
        (2, 'HTML'),
)

class  UploadForm(forms.Form):

    file_to_convert = forms.FileField(label="")
    options = forms.ChoiceField(choices=OPTIONS
    )

