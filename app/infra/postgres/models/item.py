from tortoise import fields
from tortoise.models import Model


class Item(Model):
    name = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    brand = fields.CharField(max_length=255)
    pictures = fields.JSONField(null=True, default=[])
    price = fields.FloatField()
    rating = fields.FloatField(null=True)
    city = fields.ForeignKeyField(
        "models.City", related_name="items", on_delete="SET NULL", null=True
    )
    thumbnail = fields.CharField(max_length=255)
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
