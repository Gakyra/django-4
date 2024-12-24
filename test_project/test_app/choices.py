from django.db import models


class SubscriptionTypeChoices(models.TextChoices):
    FREE = 'free', 'Free'
    ADVANCED = 'advanced', 'Advanced'
    PRO = 'pro', 'Pro'
