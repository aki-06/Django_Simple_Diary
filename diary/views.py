from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

def index(request):
	context = {
		'day_list': Day.objects.all(),
	}
	return render(request, 'diary/day_list.html', context)


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


def update(request, pk):
	# urlのpkを基にDayを取得
	day = get_object_or_404(Day, pk=pk)

	# フォームに取得したDayを紐付ける
	form = DayCreateForm(request.POST or None, instance=day)

	# 入力に問題がなければ
	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('diary:index')

	# 入力に誤りがある場合
	context = {
		'form': form
	}
	return render(request, 'diary/day_form.html', context)


def delete(request, pk):
	# urlのpkを基にDayを取得
	day = get_object_or_404(Day, pk=pk)

	# 入力に問題がなければ
	if request.method == 'POST':
		day.delete()
		return redirect('diary:index')

	# 入力に誤りがある場合
	context = {
		'day': day
	}
	return render(request, 'diary/day_confirm_delete.html', context)