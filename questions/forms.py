from django import forms
from questions.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ("text", )

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})