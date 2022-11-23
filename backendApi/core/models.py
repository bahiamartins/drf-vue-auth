import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Message(models.Model):
    """
    A private message from user to user
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField(_("Mensagem"))
    sender = models.ForeignKey(User, related_name='message_from', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='message_to', on_delete=models.CASCADE)
    cc = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sent_at = models.DateTimeField(_("Enviado em"), null=True, blank=True)
    read_at = models.DateTimeField(_("Lido em"), null=True, blank=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['-created_at']
