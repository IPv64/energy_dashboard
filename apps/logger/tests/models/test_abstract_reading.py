from decimal import Decimal

import datetime
import pytz

from django.test import TestCase

from apps.logger.models import GasReading as Reading


class AbstractReadingTestCase(TestCase):
    """
    Use GasReading as it's the only vanilla implementation of AbstractReading.
    """

    def setUp(self):
        self.tz = pytz.timezone('UTC')

    def test_save(self):
        Reading.objects.create(
            value_total=Decimal('10.000'),
            datetime=self.tz.localize(datetime.datetime.now())
        )
        reading = Reading.objects.create(
            value_total=Decimal('10.123'),
            datetime=self.tz.localize(datetime.datetime.now())
        )

        self.assertEqual(reading.value_increment, Decimal('0.123'))

    def test_save_without_previous_record(self):
        reading = Reading.objects.create(
            value_total=Decimal('10'),
            datetime=self.tz.localize(datetime.datetime.now())
        )

        self.assertEqual(reading.value_increment, Decimal('0'))
