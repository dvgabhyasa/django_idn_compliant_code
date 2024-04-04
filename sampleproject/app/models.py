from django.db import models

from parler.models import TranslatableModel, TranslatedFields

class Course(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=90),
        description=models.TextField(),
        date=models.DateField(),
    )
    def __str__(self):
        return self.title
    

