from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from models import UserProfile

class UserProfileForm(forms.ModelForm):


	class Meta:
		model = UserProfile
		fields = ('name',)




class RegisterForm(UserCreationForm):
	name = forms.CharField(label="Name", min_length=3)
	username = forms.CharField(label="username", min_length=3)
	password1 = forms.CharField(widget=forms.PasswordInput, min_length=8)

	class Meta:
		model = User
		fields = ('name','username', 'password1', 'password2')
	def save(self, commit=True):
		user = super(RegisterForm, self).save(commit=False)
		user.name = self.cleaned_data['name']
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()

			return user





# class RegisterForm(UserCreationForm):
# 	email = forms.EmailField(label="Email Address")
	# name = forms.CharField(label="Name")
# 	class Meta:
# 		model = User
# 		fields = ('name','username','email', 'password1', 'password2')
# 	def save(self, commit=True):
# 		user = super(RegisterForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		user.name = self.cleaned_data['name']
# 		user.set_password(self.cleaned_data['password1'])
# 		if commit:
# 			user.save()
# 			return user
