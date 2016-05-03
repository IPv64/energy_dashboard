import datetime

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.logger.models import ElectricityUsedReading, GasReading


class ElectricityUsageActual(APIView):

    def get(self, request, format=None):

        return Response(ElectricityUsedReading.reports.actual())


class ElectricityUsageTotal(APIView):

    def get(self, request, format=None):
        end = timezone.now()
        start = end - datetime.timedelta(days=1)

        start = datetime.datetime(2016, 4, 24)
        end = start + datetime.timedelta(days=1)

        return Response(
            ElectricityUsedReading.reports.used(
                start=start,
                end=end
            )
        )


class GasUsageTotal(APIView):

    def get(self, request, format=None):
        end = timezone.now()
        start = end - datetime.timedelta(days=1)
        start = datetime.datetime(2016, 4, 24)
        end = start + datetime.timedelta(days=1)
        return Response(
            GasReading.reports.used(
                start=start,
                end=end
            )
        )