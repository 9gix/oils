from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
User = get_user_model()

from .. import models
from .. import get_backend
from oils.apps.catalog import models as catalog_models
from oils.apps.account import models as account_models
from oils.apps.shelving import models as shelving_models

import crispy_forms


class LoanForm(forms.Form):
    patron = forms.ModelChoiceField(
            widget=forms.TextInput(),
            label=_("Patron"),
            queryset=User.objects.filter(patron__isnull=False),
            to_field_name='username')

    def clean_patron(self):
        user = self.cleaned_data['patron']
        try:
            models.Loan(patron=user.patron).clean_patron()
        except models.ValidationError as e:
            raise forms.ValidationError(e.message_dict['patron'], code='invalid')
        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = crispy_forms.helper.FormHelper()
        self.helper.form_tag = False


class LoanItemBaseForm(forms.ModelForm):
    item = forms.ModelChoiceField(
            widget=forms.TextInput(),
            label=_("Item Code"),
            queryset=shelving_models.Item.objects.all(),
            to_field_name='code')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = crispy_forms.helper.FormHelper()
        self.helper.form_tag = False


LoanFormSet = forms.inlineformset_factory(
        account_models.Patron, models.Loan, fields=('item',),
        form=LoanItemBaseForm,
        can_delete=False,
        widgets={'item': forms.TextInput()},
        min_num=1, validate_min=True, extra=3)
        
class LoanRenewalForm(forms.Form):
    item = forms.ModelChoiceField(
            widget=forms.TextInput(),
            label=_("Item Code"),
            queryset=shelving_models.Item.objects.filter(loan__in=models.Loan.opens.all()),
            to_field_name='code',
            error_messages={
                'invalid_choice': 'This item is not being loaned out'
            })


    def clean_item(self):
        backend = get_backend()
        item = self.cleaned_data['item']
        last_loan = item.loan_set.last()
        backend.validate(last_loan)
        return item

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = crispy_forms.helper.FormHelper()
        self.helper.add_input(crispy_forms.layout.Submit('submit', 'Submit'))


class LoanReturnForm(forms.Form):
    item = forms.ModelChoiceField(
            widget=forms.TextInput(),
            label=_("Item Code"),
            queryset=shelving_models.Item.objects.filter(loan__in=models.Loan.opens.all()),
            to_field_name='code',
            error_messages={
                'invalid_choice': 'This item is not being loaned out'
            })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = crispy_forms.helper.FormHelper()
        self.helper.add_input(crispy_forms.layout.Submit('submit', 'Submit'))

