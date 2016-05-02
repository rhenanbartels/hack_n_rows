import os
import tempfile

import rows

SUPPORTED_EXTENSIONS = (
        'csv',
        'html',
        'xls',
        'xlsx',
)


class ConvertedFile(object):

    def __init__(self):
        self.create()

    def _create_temp_file(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.file_name = self.temp_file.name

    def create(self):
        self._create_temp_file()

    def convert(self, file_object, from_file_extension, to_file_extension):
        #Find a smater way to discover the conversion extension
        if from_file_extension == 'csv':
            rows_object = rows.import_from_csv(file_object)
        elif from_file_extension == 'html':
            rows_object = rows.import_from_html(file_object)
        elif from_file_extension == 'xls':
            temp_xls_file = _write_to_temporary_file(file_object, '.xls')
            rows_object = rows.import_from_xls(temp_xls_file.name)
        elif from_file_extension == 'xlsx':
            pass


        if to_file_extension == 'csv':
            rows.export_to_csv(rows_object, self.file_name)
            self.file_type = 'text/csv'
        elif to_file_extension == 'html':
            rows.export_to_html(rows_object, self.file_name)
            self.file_type = 'text/plain'
        elif to_file_extension == 'xls':
            rows.export_to_xls(rows_object, self.file_name)
            self.file_type = 'application/vnd.ms-excel'
        elif to_file_extension == 'xlsx':
            pass

    def unlink(self):
        os.unlink(self.file_name)

def is_file_extension_not_valid(file_name):
    return not file_name.endswith(SUPPORTED_EXTENSIONS)

def get_file_extension(file_name):
    return file_name.split(".")[-1]

def _write_to_temporary_file(file_object, suffix):
    temp_file = tempfile.NamedTemporaryFile(suffix=suffix, delete=False)
    temp_file.write(file_object.read())
    return temp_file
