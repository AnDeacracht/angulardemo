from django.db import models


class PartOfSpeech(models.Model):
    definition = models.CharField("Definition", max_length=30)

    def __str__(self) -> str:
        return "{}".format(self.definition)


class Word(models.Model):
    definition = models.CharField("Definition", max_length=255)
    translation = models.CharField("Translation", max_length=255)
    partOfSpeech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} - {} - {}".format(self.definition, self.translation, self.partOfSpeech)
