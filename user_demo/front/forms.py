from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.ModelForm):
    telephone = forms.CharField(max_length=11)
    remember = forms.IntegerField(required=False)


    class Meta:
        model = get_user_model()
        fields = ['password']
        # fields = '__all__'
        # exclude = ['email'] #排除哪些字段