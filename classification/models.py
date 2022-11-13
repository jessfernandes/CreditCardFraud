from email.policy import default
from django.db import models
from django.contrib.postgres.fields import ArrayField

class features(models.Model):
    id = models.AutoField(primary_key=True)
    V1 = models.FloatField()
    V2 = models.FloatField()
    V3 = models.FloatField()
    V4 = models.FloatField()
    V5 = models.FloatField()
    V6 = models.FloatField()
    V7 = models.FloatField()
    V8 = models.FloatField()
    V9 = models.FloatField()
    V10 = models.FloatField()
    V11 = models.FloatField()
    V12 = models.FloatField()
    V13 = models.FloatField()
    V14 = models.FloatField()
    V15 = models.FloatField()
    V16 = models.FloatField()
    V17 = models.FloatField()
    V18 = models.FloatField()
    V19 = models.FloatField()
    V20 = models.FloatField()
    V21 = models.FloatField()
    V22 = models.FloatField()
    V23 = models.FloatField()
    V24 = models.FloatField()
    V25 = models.FloatField()
    V26 = models.FloatField()
    V27 = models.FloatField()
    V28 = models.FloatField()
    Amount = models.FloatField()

    class Meta:
        db_table = 'features'

class predict(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.TextField()
    class_predicted = models.IntegerField()
    probability = ArrayField(models.FloatField(default=None),default=None)
    date_in = models.DateTimeField(auto_now_add=True)
    featuresid = models.ForeignKey(features, on_delete = models.CASCADE)

    class Meta:
        db_table = 'predict'