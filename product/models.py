from django.db import models

User = get_user_model()

# Create your models here.

class product(models.Model):
    image=models.ImageField(
        _("Product Image"),
        blank=False,
    )
    title=models.CharField(
        _("Product Title"),
        max_length=100,
        blank=False
        )
    description=models.CharField(
        _("Product Description"),
        max_length=1500,
        )
    uploader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True)
    date = models.DateTimeField(
        default=datetime.now,
        blank=True)

    def save_model(self, request, obj, form, change):
    if not obj.pk:
        # Only set added_by during the first save.
        obj.added_by = request.user
    super().save_model(request, obj, form, change)
