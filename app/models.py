from django.db import models
from django.contrib.auth.models import User
import uuid

class Room(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="room_user")

    def __str__(self):
        return f"{self.user.email}"

class RequestFormModel(models.Model):
    titel = models.CharField(max_length=255)
    context = models.TextField()
    is_universal = models.BooleanField(default=False)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f"{self.titel} || universal {self.is_universal}"

    def save(self, *args, **kwargs):
        super(RequestFormModel, self).save(*args, **kwargs)
        users = self.user.all()
        
        pre_instance = NotificationBox.objects.filter(request_from_id = self.id)
        if pre_instance.exists():
            if len(users) == len(pre_instance):
                for pre_noti in pre_instance:
                   pre_noti.titel = self.titel
                   pre_noti.context = self.context
                   pre_noti.save()
        else:
            
            print(users, "hsgdcvhsgcvsnhgvc")
            for user in users:
                NotificationBox.objects.create(
                    room=room,
                    title=self.titel,
                    context=self.context,
                    type="universal" if self.is_universal else "individual",
                )

class NotificationBox(models.Model):
    request_from = models.ForeignKey(RequestFormModel, on_delete=models.CASCADE, related_name="request_from_model")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="notifyroom")
    title = models.CharField(max_length=255)
    context = models.TextField()
    type_msg = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.room.user.email} - {self.title}"







