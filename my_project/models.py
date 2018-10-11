from django.db import models


class Webpage(models.Model):
    address = models.CharField(max_length=300)
    h1Count = models.IntegerField()
    h2Count = models.IntegerField()
    h3Count = models.IntegerField()
    h4Count = models.IntegerField()
    h5Count = models.IntegerField()
    h6Count = models.IntegerField()
    h6Count = models.IntegerField()
    version = models.CharField(max_length=100)
    internalLinkCount = models.IntegerField()
    externalLinkCount = models.IntegerField()
    title = models.CharField(max_length=1000)
    inaccessibleLinkCount = models.IntegerField()
    statusCode = models.IntegerField()
    timeStamp = models.CharField(max_length=100)
    loginForm = models.BooleanField()
    errorType = models.IntegerField(default=0)
    errorMessage = models.CharField(max_length=100, default="0")

    def __str__(self):
        return self.address
