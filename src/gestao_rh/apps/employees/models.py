from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    STATUS = (
        (1, 'Enabled'),
        (0, 'Disabled')
    )
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departments = models.ManyToManyField('core.Department',
                                         related_name='employee',
                                         blank=True)
    company = models.ForeignKey('core.Company',
                                on_delete=models.SET_NULL,
                                null=True, blank=True)
    on_vacation = models.BooleanField()
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def overtime_total(self):
        return self.overtime_set.annotate(
            interval=models.ExpressionWrapper(
                models.F('ends') - models.F('starts'), output_field=models.DateTimeField()
            )
        ).aggregate(models.Sum('interval')).get('interval__sum')

    def __str__(self):
        return self.name
