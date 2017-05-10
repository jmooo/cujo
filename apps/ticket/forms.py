from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, HTML, Div
from crispy_forms.bootstrap import FormActions, PrependedText
from .models import Ticket


class TicketForm(forms.ModelForm):
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            '',
            Div(
                Div(
                    Div('customer'),
                    Div('address'),
                    css_class='col',
                ),
                Div(
                    Div('salesperson'),
                    Div(PrependedText('phone', '<i class="fa fa-phone" aria-hidden="true"></i>')),
                    Div(PrependedText('email', '<i class="fa fa-envelope-o" aria-hidden="true"></i>')),
                    css_class='col'
                ),
                css_class="row",
            ),
            Div(
                Div('work_requested', css_class='col'),
                css_class='row',
            ),
            Div(
                Div('work_completed', css_class='col'),
                css_class='row',
            ),
            Div(
                Div('installers', css_class='col self.helper.form_id'),
                Div(PrependedText('date_completed', '<i class="fa fa-calendar" aria-hidden="true"></i>'),
                                    css_class='col'),
                css_class='row',
            ),
        ),
        FormActions(
            Submit('submit', 'Save', css_class="btn btn-outline-success"),
            HTML("""<a href="{% url "ticket-list" %}" class="btn btn-secondary">Cancel</a>"""),
            HTML("""{% if object %}
                    <a href="{% url "ticket-delete" object.id %}"
                    class="btn btn-outline-danger pull-right">
                    Delete <i class="fa fa-trash-o" aria-hidden="true"></i></button></a>
                    {% endif %}"""),
        )
    )

    class Meta:
        model = Ticket
        fields = ('customer', 'salesperson', 'address', 'phone', 'email',
                    'installers', 'work_requested', 'work_completed', 'date_completed',)
        widgets = {
          'address': forms.Textarea(attrs={'rows':4}),
          'email': forms.TextInput(attrs={'placeholder':'Email'}),
          'phone': forms.TextInput(attrs={'placeholder':'Phone'}),
          'work_requested': forms.Textarea(attrs={'rows':10}),
          'work_completed': forms.Textarea(attrs={'rows':10}),
          'date_completed': forms.DateInput(format='%b %d, %Y'),
        }

    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['address'].label = "Job Address"
        self.fields['email'].label = ""
        self.fields['phone'].label = ""
