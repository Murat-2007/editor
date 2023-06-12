from django import forms
from .models import Post


banned_email_list=['ahmet@gmail.com', 'deneme1@gmail.com', 'deneme2@gmail.com']

class Personal_infoForm(forms.Form):
    name     = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), 
                               max_length=40, label='Name', required=True)
    surname  = forms.CharField(max_length=40, label='Surname', required=True)
    email    = forms.EmailField(max_length=40, label='Email', required=True)
    content   = forms.CharField(max_length=1000, label='Content', required=True)

    def __init__(self, *args, **kwargs):
        super(Personal_infoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['content'].widget=forms.Textarea(attrs={'class':'form-control'})


    def clean_name(self):
            name = self.cleaned_data.get('name')
            if name == 'ahmet':
                raise forms.ValidationError('Lutfen Ahmet dışında bir isim giriniz')
            return name
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email in banned_email_list:
            raise forms.ValidationError('Lütfen banlı email adresleri dışında bir email giriniz')
        return email
    """
    def clean(self):
        email  = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            self.add_error('email2', 'emailler eşleşmedi')
            self.add_error('email', 'emailler eşleşmedi')
    """

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'docfile', 'categories']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}
        self.fields['content'].widget.attrs['rows']=10