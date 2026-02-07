from django.db import models

class TennisClub(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=40)
    price = models.IntegerField()
    quantity = models.IntegerField(default=3)
    image_main = models.ImageField(upload_to='tennis_clubs/', blank=True)
    image_hover1 = models.ImageField(upload_to='tennis_clubs/', blank=True)
    image_hover2 = models.ImageField(upload_to='tennis_clubs/', blank=True)
    def __str__(self):
        return f"{self.name} | {self.location} | {self.price} | {self.quantity}"
    


class SlotAvailability(models.Model):
    TennisClub = models.ForeignKey(TennisClub, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    taken = models.IntegerField(default=1)


    class Meta:
        unique_together = ('TennisClub', 'date', 'time')

    def __str__(self):
        return f"{self.TennisClub.name} | {self.date} | {self.time} | {self.taken}"
    




# class BookingSchedule(models.Model):
#     court = models.ForeignKey(Court, on_delete=models.CASCADE)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()

#     def __str__(self):
#         return f"{self.court.name} | {self.start_time} | {self.end_time}"
