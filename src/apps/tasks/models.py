from django.db import models

    
class Task(models.Model):
    class Prioriry(models.IntegerChoices):
        LOW = 1, 'Low'
        NON_CRITICAL = 2, 'Non critical'
        HIGH = 3, 'High'
        CRITICAL = 4, 'Critical'

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-priority']
     
    title = models.CharField(max_length=64, verbose_name='Title')
    priority = models.PositiveSmallIntegerField(
        choices=Prioriry.choices,
        default=Prioriry.LOW,
        verbose_name='Priority'
    )
    text = models.TextField(verbose_name='Task text')
    
    def __str__(self) -> str:
        return f'{self.title}: {self.text}\n'
