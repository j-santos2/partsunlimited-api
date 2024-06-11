from django.db import models

NAME_MAX_LENTH = 150
SKU_MAX_LENGTH = 30
DESCRIPTION_MAX_LENGTH = 1024


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=NAME_MAX_LENTH)
    sku = models.CharField(max_length=SKU_MAX_LENGTH)
    description = models.CharField(max_length=DESCRIPTION_MAX_LENGTH)
    weight_ounces = models.IntegerField()
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = "part"
