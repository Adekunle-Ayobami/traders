from django.contrib import admin
from .models import Trader

class TraderAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_balance', 'current_balance', 'profit_loss')

    def profit_loss(self, obj):
        return obj.current_balance - obj.initial_balance

    profit_loss.short_description = 'Profit/Loss'

admin.site.register(Trader, TraderAdmin)

