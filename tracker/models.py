from django.db import models

class BMIRecord(models.Model):
    weight = models.FloatField()  # in kilograms
    height = models.FloatField()  # in meters or centimeters
    bmi = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_bmi(self):
        """Calculates BMI and ensures height is in meters."""
        if self.height and self.weight:
            # If height is greater than 10, assume it's in centimeters and convert it to meters
            if self.height > 10:
                self.height /= 100  # Convert height from cm to meters
            self.bmi = self.weight / (self.height ** 2)
            self.save()

    def __str__(self):
        return f"BMI Record {self.id} - BMI: {self.bmi}"