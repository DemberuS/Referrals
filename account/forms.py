from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account


class RegistrationForm(UserCreationForm):
	phone = forms.CharField(max_length=14, help_text='Необходим действующий телефон.')

	class Meta:
		model = Account
		fields = ('phone', 'password1', 'password2')

	def clean_phone(self):
		phone = self.cleaned_data['phone']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(phone=phone)
		except Account.DoesNotExist:
			return phone
		raise forms.ValidationError(f'{phone} телефон уже используется.')


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('phone', 'password')

	def clean(self):
		if self.is_valid():
			phone = self.cleaned_data['phone']
			password = self.cleaned_data['password']
			if not authenticate(phone=phone, password=password):
				raise forms.ValidationError("Неправильно введены телефон или пароль")