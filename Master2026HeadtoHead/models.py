from django.db import models
from django.contrib.auth.models import User



class AllGolfers(models.Model):
    name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=100, blank=True)
    tour = models.CharField(max_length=50)
    rating = models.IntegerField()

    day_1_score_Masters26 = models.IntegerField(null=True, blank=True)
    day_2_score_Masters26 = models.IntegerField(null=True, blank=True)
    day_3_score_Masters26 = models.IntegerField(null=True, blank=True)
    day_4_score_Masters26 = models.IntegerField(null=True, blank=True)

    def total_score(self):
        return (
            (self.day_1_score_Masters26 or 0) +
            (self.day_2_score_Masters26 or 0) +
            (self.day_3_score_Masters26 or 0) +
            (self.day_4_score_Masters26 or 0)
        )

    def __str__(self):
        return self.name




class UserTrackedGolfers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    selection1 = models.ForeignKey(AllGolfers, null=True, blank=True, on_delete=models.SET_NULL, related_name="slot1_users")
    selection2 = models.ForeignKey(AllGolfers, null=True, blank=True, on_delete=models.SET_NULL, related_name="slot2_users")
    selection3 = models.ForeignKey(AllGolfers, null=True, blank=True, on_delete=models.SET_NULL, related_name="slot3_users")
    selection4 = models.ForeignKey(AllGolfers, null=True, blank=True, on_delete=models.SET_NULL, related_name="slot4_users")
    selection5 = models.ForeignKey(AllGolfers, null=True, blank=True, on_delete=models.SET_NULL, related_name="slot5_users")