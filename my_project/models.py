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
        return self.address+"~"+str(self.errorType)+"~"+str(self.h1Count)+"~"+str(self.h2Count)+"~"+str(self.h3Count)+"~"+str(self.h4Count)+"~"+str(self.h5Count)+"~"+str(self.h6Count)+"~"+self.version+"~"+str(self.internalLinkCount)+"~"+str(self.externalLinkCount)+"~"+self.title+"~"+str(self.inaccessibleLinkCount)+"~"+str(self.statusCode)+"~"+str(self.timeStamp)+"~"+str(self.loginForm)+"~"+str(self.errorMessage)
