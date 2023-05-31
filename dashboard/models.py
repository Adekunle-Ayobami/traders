import random
from django.db import models

class Trader(models.Model):
    name = models.CharField(max_length=100)
    initial_balance = models.IntegerField(blank=True, null=True)
    current_balance = models.IntegerField(blank=True, null=True)

    def simulate_profit_loss(self):
        # Simulate a random profit or loss
        profit_loss = random.uniform(-100, 100)
        self.current_balance += profit_loss
        self.save()