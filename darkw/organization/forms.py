from django import forms
from django.forms import ModelForm
from main.models import Players, Organizations
from organization.models import OrganizationRanks

class InviteForm(forms.Form):
    invited = forms.ChoiceField(required=False, choices=[])

    def __init__(self, *args, **kwargs):
        super(InviteForm, self).__init__(*args, **kwargs)
        self.fields['invited'] = forms.ChoiceField(choices=[(nickname, nickname) for nickname in Players.objects.all()])
        
class AcceptForm(forms.Form):
    akcepted = forms.BooleanField(required=True)
    
class AddRank(ModelForm):
    class Meta:
        model = OrganizationRanks
        fields = ['rank_name','visible_money','visible_ranks','visible_chat','visible_cars','visible_magazine','visible_phone', 'rank_power']