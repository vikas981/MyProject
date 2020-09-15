from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from TestCase.models import Testcasedetail


class TestcasedetailForm(forms.ModelForm):
    class Meta:
        model = Testcasedetail
        fields = ('Test_Step_Id', 'Test_Step_Description', 'Keyword', 'status')

        widgets = {
            'Test_Step_Id': forms.TextInput(attrs={'class': 'form-control'}),
            'Test_Step_Description': forms.TextInput(attrs={'class': 'form-control'}),
            'Keyword': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


class TestcasedetailCreateForm(forms.ModelForm):
    class Meta:
        model = Testcasedetail
        fields = '__all__'

        widgets = {
            'Test_Step_Id': forms.TextInput(attrs={'class': 'form-control'}),
            'Test_Step_Description': forms.TextInput(attrs={'class': 'form-control'}),
            'Keyword': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'testcase': forms.Select(attrs={'class': 'form-control'})
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
