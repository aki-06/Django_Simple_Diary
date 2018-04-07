from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import DayCreateForm
from .models import Day

# 関数で定義
# def index(request):
# 	context = {
# 		'day_list': Day.objects.all(),
# 	}
# 	return render(request, 'diary/day_list.html', context)

# 汎用viewで書き換え
class IndexView(generic.ListView):
	model = Day
	paginate_by = 3

	def get_queryset(self):
		return super().get_queryset().order_by('-date')

# 関数で定義
# def add(request):
# 	# 送信内容を基にフォームを作る。POSTじゃなければ空のフォーム
# 	form = DayCreateForm(request.POST or None)

# 	# 入力内容に問題がなければ
# 	if request.method == 'POST' and form.is_valid():
# 		form.save()
# 		return redirect('diary:index')

# 	# 入力内容に誤りがある場合
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'diary/day_form.html', context)

# 汎用viewで書き換え
class AddView(LoginRequiredMixin, generic.CreateView):
	model = Day
	form_class = DayCreateForm
	success_url = reverse_lazy('diary:index')


# 関数で定義
# def update(request, pk):
# 	# urlのpkを基にDayを取得
# 	day = get_object_or_404(Day, pk=pk)

# 	# フォームに取得したDayを紐付ける
# 	form = DayCreateForm(request.POST or None, instance=day)

# 	# 入力に問題がなければ
# 	if request.method == 'POST' and form.is_valid():
# 		form.save()
# 		return redirect('diary:index')

# 	# 入力に誤りがある場合
# 	context = {
# 		'form': form
# 	}
# 	return render(request, 'diary/day_form.html', context)

# 汎用viewで書き換え
class UpdateView(LoginRequiredMixin,generic.UpdateView):
	model = Day
	form_class = DayCreateForm
	success_url = reverse_lazy('diary:index')


# 関数で定義
# def delete(request, pk):
# 	# urlのpkを基にDayを取得
# 	day = get_object_or_404(Day, pk=pk)

# 	# 入力に問題がなければ
# 	if request.method == 'POST':
# 		day.delete()
# 		return redirect('diary:index')

# 	# 入力に誤りがある場合
# 	context = {
# 		'day': day
# 	}
# 	return render(request, 'diary/day_confirm_delete.html', context)

# 汎用viewで書き換え
class DeleteView(LoginRequiredMixin, generic.DeleteView):
	model = Day
	success_url = reverse_lazy('diary:index')

# 関数で定義
# def detail(request, pk):
# 	# urlのpkを基にDayを取得
# 	day = get_object_or_404(Day, pk=pk)

# 	# 入力に誤りがある場合
# 	context = {
# 		'day': day
# 	}
# 	return render(request, 'diary/day_detail.html', context)

# 汎用viewで書き換え
class DetailView(generic.DetailView):
	model = Day