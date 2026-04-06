from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    ticket_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title
