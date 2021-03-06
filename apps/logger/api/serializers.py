from rest_framework import serializers


class MetricSerializer(serializers.Serializer):
    datetime = serializers.CharField()
    value = serializers.DecimalField(source='value_increment__sum',
                                     max_digits=8, decimal_places=3)
    costs = serializers.DecimalField(source='costs__sum',
                                     max_digits=9, decimal_places=4)


class MetricActualSerializer(serializers.Serializer):
    datetime = serializers.CharField()
    value = serializers.DecimalField(source='value__avg',
                                     max_digits=8, decimal_places=3)
