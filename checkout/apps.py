from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    # include the signals here so django knows about them
    def ready(self):
        import checkout.signals
