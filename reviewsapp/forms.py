from .models import Comment, BugReport
from django import forms

# CommentForm taken from "I think therefore I blog"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['contact_reason', 'body']
