from django import forms

from hack_n_rows.core.utils import (is_file_extension_not_valid,
        get_file_extension)

OPTIONS = (
        ('csv', 'CSV'),
        ('html', 'HTML'),
        ('xls', 'XLS'),
)

class  UploadForm(forms.Form):

    file_to_convert = forms.FileField(label="")
    options = forms.ChoiceField(choices=OPTIONS
    )


    def clean_file_to_convert(self):
        """
            Check if the upcoming file is supported in rows
        """
        #File extension
        file_to_convert = self.cleaned_data['file_to_convert']
        if is_file_extension_not_valid(file_to_convert.name):
            file_extension = get_file_extension(file_to_convert.name)
            raise forms.ValidationError("Sorry, we are not able to convert "\
                   ".{0} files. We gonna work on that soon!".format(file_extension))

            #TODO:Check if file format is correct. Maybe a file if wrong extension
            #can be uploaded. Use rows to validate the file

        return file_to_convert


