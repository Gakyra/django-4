from django.contrib.auth.mixins import AccessMixin

from .constants import ADVANCED_AND_MORE, PRO


class SubscriptionLimitationMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if self.subscription_limitation == ADVANCED_AND_MORE:
            if request.user.is_free_subscription:
                return self.handle_no_permission()
        elif self.subscription_limitation == ADVANCED_AND_MORE:
            if request.user.is_free_subscription or request.user.is_advanced_subscription:
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
