from django.db import models

from test_app.choices import SubscriptionTypeChoices


class Subscription(models.Model):
    user = models.OneToOneField('test_app.User', on_delete=models.CASCADE, related_name='subscription')
    type = models.CharField(max_length=100, choices=SubscriptionTypeChoices.choices)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


class FreeSubscriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='free')

class StandardSubscriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='standard')

class PremiumSubscriptionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type='premium')




class FreeSubscription(Subscription):
    class Meta:
        proxy = True

    objects = FreeSubscriptionManager()

class StandardSubscription(Subscription):
    class Meta:
        proxy = True

    objects = StandardSubscriptionManager()

class PremiumSubscription(Subscription):
    class Meta:
        proxy = True

    objects = PremiumSubscriptionManager()
