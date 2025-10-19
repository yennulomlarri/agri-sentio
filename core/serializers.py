from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument
    to control which fields are displayed dynamically.
    """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class BaseSerializer(serializers.ModelSerializer):
    """
    Base serializer that can be inherited by all other serializers.
    Provides a clean Meta and common representation control.
    """
    class Meta:
        abstract = True

from rest_framework import serializers

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
