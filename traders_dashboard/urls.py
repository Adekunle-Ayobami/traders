from django.contrib import admin
from django.urls import path
from dashboard.views import dashboard, add_trader, edit_trader, simulate_profit_loss, profit_loss_graph

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/add/', add_trader, name='add_trader'),
    path('dashboard/edit/<int:trader_id>/', edit_trader, name='edit_trader'),
    path('dashboard/simulate-profit-loss/', simulate_profit_loss, name='simulate_profit_loss'),
    path('dashboard/profit-loss-graph/', profit_loss_graph, name='profit_loss_graph'),
]
