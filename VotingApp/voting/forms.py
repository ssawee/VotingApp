from django import forms


class VotingForm(forms.Form):

    CHARACTER_CHOISES = [
    ('ch1', 'character1'),
    ('ch2', 'character2'),
    ('ch3', 'character3'),
    ]

    test_value = forms.MultipleChoiceField(required=False, widget=forms.RadioSelect, choices=CHARACTER_CHOISES)
