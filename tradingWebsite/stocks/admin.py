from django.contrib import admin
from .models import Portfolio, Stock


@admin.register(Portfolio)
class PortfolioAdminView(admin.ModelAdmin):
    list_display = ("user", "money_left")
    search_fields = ("user",)


@admin.register(Stock)
class StockAdminView(admin.ModelAdmin):
    list_display = ("name", "shares", "portfolio")
    ordering = ('name',)
    search_fields = ("name", "porfolio")
    list_filter = ("name", "portfolio")
