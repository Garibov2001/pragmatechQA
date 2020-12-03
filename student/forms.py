from django import forms
from student.models import Question, QuestionImage, Comment, CommentImage
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

    def clean_title(self):
        data = self.cleaned_data['title']
        azeriChar = ['ə','ü','ö','ğ','ı','ç','ş']
        for char in data.lower():
            if (ord(char)>=32 and ord(char) <=126) or (char in azeriChar) :
                pass
            else:
                raise ValidationError("Daxil etdiyiniz başlıq standartlara uyğun deyil")
        return data

    def clean_tags(self):
        data = self.cleaned_data['tags']
        if (len(data)>5):
             raise ValidationError("Bir mövzuya maximum 5 tag əlavə edə bilərsiz.")
        else:
            for eachTag in data:
                if(not IsCorrectTag(eachTag)):
                    raise ValidationError("Daxil etdiyiniz tag standartlara uyğun deyil")
        return [each.lower() for each in data]

class QuestionImageForm(forms.ModelForm):
    class Meta:
        model = QuestionImage
        fields = ['image', 'question']

    def clean_image(self):
        data = self.cleaned_data['image']
        MAX_IMAGE_SIZE = 2097152 # 2 MB
        if (data.size > MAX_IMAGE_SIZE):
            raise ValidationError(f"Daxil etdiyiniz sekil: {data} hecmi coxdur. Max sekil hecmi: {MAX_IMAGE_SIZE}")
        else:
            return data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['question', 'student', 'content']

class CommentImageForm(forms.ModelForm):
    class Meta:
        model = CommentImage
        fields = ['image', 'comment']
    
    def clean_image(self):
        data = self.cleaned_data['image']
        MAX_IMAGE_SIZE = 2097152 # 2 MB
        if (data.size > MAX_IMAGE_SIZE):
            raise ValidationError(f"Daxil etdiyiniz sekil: {data} hecmi coxdur. Max sekil hecmi: {MAX_IMAGE_SIZE}")
        else:
            return data

