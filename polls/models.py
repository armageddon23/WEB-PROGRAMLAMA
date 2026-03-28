import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    # Örneğin: "İstanbul'da yaşamaktan ne kadar memnunsunuz?"
    question_text = models.CharField(max_length=200, verbose_name="Anket Sorusu")
    pub_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi")

    # Panelde nesne ismi olarak sorunun kendisini gösterir
    def __str__(self):
        return self.question_text

    # Soru son 24 saat içinde mi yayınlandı?
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Soru silinirse o soruya ait tüm şehir seçenekleri de silinir
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Seçenekler: "Çok seviyorum", "Memnun değilim" vb.
    choice_text = models.CharField(max_length=200, verbose_name="Seçenek Metni")
    # Başlangıçta oy sayısı 0'dır
    votes = models.IntegerField(default=0, verbose_name="Oy Sayısı")

    def __str__(self):
        return self.choice_text