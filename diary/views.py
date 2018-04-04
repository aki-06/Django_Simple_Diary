from django.shortcuts import render, redirect
from .forms import DayCreateForm

def index(request):
	return render(request, 'diary/day_list.html')


def add(request):
	# 送信内容を基にフォームを作る。POSTじゃなければ空のフォーム
	form = DayCreateForm(request.POST or None)

	# 入力内容に問題がなければ
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('diary:index')

	# 入力内容に誤りがある場合
	context = {
		'form': form
	}
	return render(request, 'diary/day_form.html', context)