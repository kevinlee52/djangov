from django.db import models

# Create your models here.
class AutoCiGp1100X(models.Model):
    case_key = models.CharField(primary_key=True, max_length=128)
    result = models.CharField(max_length=4, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    test_bed = models.CharField(max_length=128, blank=True, null=True)
    tester = models.CharField(max_length=45, blank=True, null=True)
    script = models.CharField(max_length=256, blank=True, null=True)
    headline = models.CharField(max_length=512, blank=True, null=True)
    log = models.CharField(max_length=256, blank=True, null=True)
    runner_host = models.CharField(max_length=45, blank=True, null=True)
    issue_tickets = models.CharField(max_length=45, blank=True, null=True)
    ci_online = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_ci_GP1100X'

class AutoCiGs4227Xgs(models.Model):
    case_key = models.CharField(primary_key=True, max_length=128)
    result = models.CharField(max_length=4, blank=True, null=True)
    error_message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    test_bed = models.CharField(max_length=128, blank=True, null=True)
    tester = models.CharField(max_length=45, blank=True, null=True)
    script = models.CharField(max_length=256, blank=True, null=True)
    headline = models.CharField(max_length=512, blank=True, null=True)
    log = models.CharField(max_length=256, blank=True, null=True)
    runner_host = models.CharField(max_length=45, blank=True, null=True)
    issue_tickets = models.CharField(max_length=45, blank=True, null=True)
    ci_online = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auto_ci_GS4227_XGS'

