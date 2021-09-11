from tortoise import fields
from tortoise.models import Model


class City(Model):
    name = fields.CharField(max_length=255)
    last_modified = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)
