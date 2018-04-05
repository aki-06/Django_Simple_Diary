from django.db import models
from django.utils import timezone # Djangoではdatetime.nowの代わりにtimezone.nowで現時刻を取得する


class Day(models.Model):
	# 内部的な処理
	# id = models.AutoField(primary_key=True)
	title = models.CharField('タイトル', max_length=200)
	text = models.TextField('本文')
	date = models.DateTimeField('日付', default=timezone.now)
