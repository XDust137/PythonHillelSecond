from django.db import models
from django.urls import reverse


class Row(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self): return self.name


class RowSession(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    row = models.ForeignKey(
        "Row",
        on_delete=models.CASCADE,
        related_name="row_sessions"
    )
    date = models.DateField()

    @property
    def display_username(self): return self.user.username

    def get_absolute_url(self): return reverse('row_session-detail', kwargs={'pk': self.pk})

    def __str__(self): return f"{self.user.username} {self.pk}"


class Player(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateField()
    row = models.ForeignKey(
        "RowSession",
        on_delete=models.CASCADE,
        related_name="players"
    )

    @property
    def score(self): return "0"

    def __str__(self): return self.name


class PersonalFrame(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(
        "Player",
        on_delete=models.CASCADE,
        related_name="frames"
    )

    def __str__(self): return self.name

    def frame_sum(self):
        throws = self.throws.all()
        collect_list = [int(i) for i in throws]
        return sum(collect_list)


class PersonalThrow(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=2)
    frame = models.ForeignKey(
        "PersonalFrame",
        on_delete=models.CASCADE,
        related_name="throws"
    )

    def __int__(self):
        if str(self.value).isdigit(): return int(self.value)
        return 0

    def __str__(self): return self.name
