from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='boards')
    board_name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)  # ฟิลด์ order
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='created_boards', on_delete=models.CASCADE, null=True, blank=True, editable=False)
    updated_by = models.ForeignKey(User, related_name='updated_boards', on_delete=models.CASCADE, null=True, blank=True, editable=False)

    def __str__(self):
        return self.board_name
