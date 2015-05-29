from django.db import models

from apps.donations.models import Blood
from apps.users.models import Hospital


class TransfusionRequest(models.Model):

    pass


class TransfusionConfirmations(models.Model):

    pass


class CompatibilityTest(models.Model):

    blood = models.ForeignKey(Blood, related_name='compatibility_tests')
    hospital = models.ForeignKey(Hospital, related_name='compatibility_tests')


class BloodIssue(models.Model):

    blood = models.OneToOneField(Blood)
