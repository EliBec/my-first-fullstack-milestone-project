from django import forms
from .models import Product, Category, Subcategory, Rating
from .widgets import CustomClearableFileInput


class ProductProfileForm(forms.ModelForm):
    class Meta:
        model = Product
        # only include the fields that are editable by user
        fields = ('category', 'subcategory', 'name',
                  'short_desc', 'long_desc', 'sku', 'brand',
                  'price', 'has_sizes', 'image_url', 'image', 'style')

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names_cat = \
            [(c.id, c.get_friendly_name()) for c in categories]

        subcategories = Subcategory.objects.all()
        friendly_names_subcat = \
            [(subc.id, subc.get_friendly_name_sub()) for subc in subcategories]

        self.fields['category'].choices = \
            friendly_names_cat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'

        self.fields['subcategory'].choices = \
            friendly_names_subcat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating

        exclude = ['product', 'customer']

        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'cols': 5,
                                      'placeholder':
                                             "How you use this product?"
                                             " What do you find a great?"
                                             " What do find not so great?"}),

            'rating': forms.NumberInput(attrs={"type": 'number',
                                        "value": 1,
                                               "min": 1,
                                               "max": 5, }),
        }


