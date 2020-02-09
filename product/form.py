from django import forms

class productForm(forms.Form):
    image=models.ImageField(
        label=("Product Image"),
        blank=False,
    )
    title=models.CharField(
        label=("Product Title"),
        max_length=100,
        blank=False
        )
    description=models.CharField(
        label=("Product Description"),
        max_length=1500,
        )
