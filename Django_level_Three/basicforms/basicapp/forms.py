from django import forms
from django.core import  validators


# custom validators
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("Name needs to start with z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)



    # to check the verify email field or any field the method whcih is called
    # automatically is 'clean _'it is like clean_<name of the feald> or to check
    # entire form use method clean()
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("make sure email match!")

    # botcatcher = forms.CharField(required=False,
    #                              widget=forms.HiddenInput,
    #                              validators=[validators.MaxLengthValidator(0)])

    # it is like clean botcater ...this is type of valiadtion in the form
    # like it check if any robot fill the form
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.validationError("GOTCHA BOT!")

    #     return botcatcher