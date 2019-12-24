from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
	name = forms.CharField(max_length=25)
	email = forms.EmailField()
	email.clean('email@example.com')
	to = forms.EmailField()
	to.clean('email@example.com')
	comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
	query = forms.CharField()

	