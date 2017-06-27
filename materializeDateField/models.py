from django.db import models

import datetime

class ExampleModel(models.Model):
    endDate = models.DateField("Effective through ", default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('LRT:edit', kwargs={'pk': self.pk})

    def __str__(self):
        return self.endDate
