import random
from django.shortcuts import render, redirect
from .models import Trader
from .forms import TraderForm
from matplotlib import pyplot as plt

def dashboard(request):
    traders = Trader.objects.all()
    return render(request, 'dashboard.html', {'traders': traders})

def add_trader(request):
    if request.method == 'POST':
        form = TraderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TraderForm()
    return render(request, 'add_trader.html', {'form': form})

def edit_trader(request, trader_id):
    trader = Trader.objects.get(id=trader_id)
    if request.method == 'POST':
        form = TraderForm(request.POST, instance=trader)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TraderForm(instance=trader)
    return render(request, 'edit_trader.html', {'form': form, 'trader': trader})

def profit_loss_graph(request):
    traders = Trader.objects.all()
    
    # Get profit/loss data for each trader
    data = []
    for trader in traders:
        data.append((trader.name, trader.current_balance - trader.initial_balance))
    
    # Sort traders by profit/loss
    data.sort(key=lambda x: x[1], reverse=True)
    
    # Extract trader names and profit/loss values
    trader_names = [item[0] for item in data]
    profit_loss_values = [item[1] for item in data]
    
    # Plot the profit/loss graph
    plt.bar(trader_names, profit_loss_values)
    plt.xlabel('Trader')
    plt.ylabel('Profit/Loss')
    plt.title('Profit/Loss of Traders')
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Save the graph to a file
    graph_file = 'dashboard/static/dashboard/profit_loss_graph.png'
    # plt.savefig(graph_file)
    
    return render(request, 'profit_loss_graph.html', {'graph_file': graph_file})


def simulate_profit_loss(request):
    traders = Trader.objects.all()
    for trader in traders:
        trader.simulate_profit_loss()
    return redirect('dashboard')
