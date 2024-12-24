from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from test_app.choices import SubscriptionTypeChoices

from test_project.test_app.constants import ADVANCED_AND_MORE, FREE_AND_MORE, PRO


class UserManager(BaseUserManager):
    def get_free_users(self):
        return self.filter(subscription__type=SubscriptionTypeChoices.FREE)

    def get_advanced_users(self):
        return self.filter(subscription__type=SubscriptionTypeChoices.ADVANCED)

    def get_pro_users(self):
        return self.filter(subscription__type=SubscriptionTypeChoices.PRO)

class User(AbstractUser):
    objects = UserManager()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def is_free_subscription(self):
        return self.subscription.type == SubscriptionTypeChoices.FREE

    @property
    def is_advanced_subscription(self):
        return self.subscription.type == SubscriptionTypeChoices.ADVANCED

    @property
    def is_pro_subscription(self):
        return self.subscription.type == SubscriptionTypeChoices.PRO

    def has_subscription(self, subscription_type):
        return self.subscription.type == subscription_type

    def has_free_and_more_subscription(self):
        return self.subscription.type in FREE_AND_MORE

    def has_advanced_and_more_subscription(self):
        return self.subscription.type in ADVANCED_AND_MORE

    def has_pro_subscription(self):
        return self.subscription.type in PRO




