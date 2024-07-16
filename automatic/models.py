from django.db import models


class Worker(models.Model):
    name = models.CharField('Имя', max_length=255)
    phone_number = models.CharField('Номер телефона', max_length=255)

    @property
    def is_authenticated(self):
        return True

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class PointSale(models.Model):
    name = models.CharField('Название', max_length=255)
    worker = models.ForeignKey(Worker, models.RESTRICT,
                               related_name='worker_points',
                               verbose_name='Работник')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.name


class Visit(models.Model):
    date_time = models.DateTimeField('Дата/Время', auto_now_add=True)
    point_sale = models.ForeignKey(PointSale, on_delete=models.CASCADE,
                                   verbose_name='Торговая точка')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE,
                               related_name='worker_visits',
                               verbose_name='Работник')
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещения'

    def __str__(self):
        return f'{self.worker} - {self.date_time}'
