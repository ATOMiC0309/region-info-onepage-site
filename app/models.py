from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    area_info = models.TextField(blank=True, null=True)
    population = models.IntegerField(null=True, verbose_name="Aholisi")
    population_compared_to = models.IntegerField(null=True)
    image = models.ImageField(upload_to='area_img/', null=True)
    published = models.BooleanField(default=True, verbose_name="Sahifaga chiqarish")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Joylash vaqti")
    parent = models.ForeignKey('self', verbose_name="Joylashgan hudud", on_delete=models.CASCADE, related_name='territories', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Hudud"
        verbose_name_plural = "Hududlar"

