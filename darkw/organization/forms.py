from django import forms
from main.models import Players, Organizations


class InviteForm(forms.Form):
    invited = forms.ChoiceField(required=False, choices=[])

    def __init__(self, *args, **kwargs):
        super(InviteForm, self).__init__(*args, **kwargs)
        self.fields['invited'] = forms.ChoiceField(choices=[(nickname, nickname) for nickname in Players.objects.all()])
        
class AcceptForm(forms.Form):
    akcepted = forms.BooleanField(required=True)