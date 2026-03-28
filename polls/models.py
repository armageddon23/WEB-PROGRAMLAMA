import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Anket Sorusu")
    pub_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """Soru son 24 saat içinde mi yayınlandı?"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # Admin panelinde gösterim için dekoratör
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Yeni mi yayınlandı?"
    )
    def was_published_recently_admin(self):
        """Admin panelinde gösterilecek versiyon"""
        return self.was_published_recently()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Seçenek Metni")
    votes = models.IntegerField(default=0, verbose_name="Oy Sayısı")

    def __str__(self):
        return self.choice_text