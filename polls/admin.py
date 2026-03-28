from django.contrib import admin
from .models import Question, Choice

# Modellerimizi buraya kaydediyoruz
admin.site.register(Question)
admin.site.register(Choice)