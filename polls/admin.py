from django.contrib import admin
from .models import Choice, Question, VoteRecord


# Seçenekleri sorunun içine satır olarak ekleme (TabularInline daha az yer kaplar)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Varsayılan 3 boş seçenek kutusu

class QuestionAdmin(admin.ModelAdmin):
    # Detay sayfasındaki alan grupları (Fieldsets)
    fieldsets = [
        ("Şehir Sorusu Metni", {"fields": ["question_text"]}),
        ("Tarih Bilgisi", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    # Liste sayfasındaki sütunlar
    list_display = ["question_text", "pub_date", "was_published_recently"]
    
    # Sağ tarafa filtreleme paneli
    list_filter = ["pub_date"]
    
    # Üst tarafa arama kutusu
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

class VoteRecordAdmin(admin.ModelAdmin):
    list_display = ["city", "question", "choice", "created_at"]
    list_filter = ["city", "created_at"]
    search_fields = ["city"]

admin.site.register(VoteRecord, VoteRecordAdmin)