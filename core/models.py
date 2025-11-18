from django.db import models

class Conversation(models.Model):
    user_message = models.TextField()
    ai_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_message} -> {self.ai_message}"
