from django.db import models









class MessagesSent(models.Model):

    phone = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending', choices=(('pending', 'pending'), ('sent', 'sent'), ('failed', 'failed')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone