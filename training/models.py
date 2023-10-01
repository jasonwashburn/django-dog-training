from django.conf import settings
from django.db import models
from django.urls import reverse
from PIL import Image, ImageOps


class Pet(models.Model):
    name = models.CharField(max_length=50)
    sex = models.IntegerField(
        blank=True, null=True, choices=[(0, "Male"), (1, "Female")]
    )
    age = models.DateField()
    intact = models.BooleanField()
    owner = models.ForeignKey("Owner", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="pet_photos", blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pet_detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo:
            img = Image.open(self.photo.path)
            img = ImageOps.exif_transpose(img)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.photo.path)


class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    street_address_1 = models.CharField(max_length=50, blank=True, null=True)
    street_address_2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    def get_absolute_url(self):
        return reverse("owner_detail", kwargs={"pk": self.pk})
