from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Upload file')

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        #self.fields['file'].widget.attrs['class'] = 'custom-file-input'
        #self.fields['file'].widget.attrs['id'] = 'upload2'
        #id = "upload"
        self.fields['file'].widget.attrs['class'] = 'file-upload-input'
        self.fields['file'].widget.attrs['id'] = '1'
        self.fields['file'].widget.attrs['value'] = 'Hi'
        self.fields['file'].widget.attrs["onchange"]="readURL(event);"
        self.fields['file'].widget.attrs['style']="position:absolute;"
        self.fields['file'].widget.attrs['accept'] = 'application/pdf'

        id = "upload"
