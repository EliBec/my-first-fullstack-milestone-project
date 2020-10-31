from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

    # include the signals here so django knows about them
    def ready(self):
        import products.signals
