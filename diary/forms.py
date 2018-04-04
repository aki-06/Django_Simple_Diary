from django import forms
from .models import Day


class DayCreateForm(forms.ModelForm):
	"""
	formsのModelFormを継承
	"""

	class Meta:
		# 対象となるモデル
		model = Day
		# 対象となるフィールド
		fields = '__all__' # ('title', 'text', 'date')