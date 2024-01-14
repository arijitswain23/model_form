from django import  forms

from app.models import *

class TopicForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'


class WebPageForm(forms.ModelForm):
    class Meta():
        model=WebPage
        fields='__all__'
        #labels={'topic_name':'TN'}
        #widgets={'url':forms.PasswordInput()}


class AccessRecordForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'