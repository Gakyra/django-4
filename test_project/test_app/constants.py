from test_app.choices import SubscriptionTypeChoices


FREE_AND_MORE = {
    SubscriptionTypeChoices.FREE,
    SubscriptionTypeChoices.ADVANCED,
    SubscriptionTypeChoices.PRO,
}
ADVANCED_AND_MORE = {
    SubscriptionTypeChoices.ADVANCED,
    SubscriptionTypeChoices.PRO,
}
PRO = {
    SubscriptionTypeChoices.PRO,
}