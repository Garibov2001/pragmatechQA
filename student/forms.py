from django import forms
from student.models import Question
from django.core.exceptions import ValidationError
import re


def IsCorrectTag(argTag):
    pattern = r'^[a-zA-Z0-9]{1,17}(-([a-zA-Z0-9]){1,17}){0,3}$'
    if re.match(pattern, argTag):
        return True
    return False


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'content', 'tags']

    def clean_tags(self):
        data = self.cleaned_data['tags']
        if (len(data)>5):
             raise ValidationError("Bir mövzuya maximum 5 tag əlavə edə bilərsiz.")
        else:
            for eachTag in data:
                if(not IsCorrectTag(eachTag)):
                    raise ValidationError("Daxil etdiyiniz tag standartlara uyğun deyil")
        return data