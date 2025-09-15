from django import forms


class SecretForm(forms.Form):
    name = (forms.CharField(
        label="name",
        max_length=30,
        required=True,
        error_messages={'required': 'Please, enter your name!'}
    ))


def __init__(self, participants=None, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.participants = participants or []


