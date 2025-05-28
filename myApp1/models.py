from django.db import models

class ComputerBuild(models.Model):
    name = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    gpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name
class Component(models.Model):
    CATEGORY_CHOICES = [
        ('CPU', 'Процессор'),
        ('GPU', 'Видеокарта'),
        ('RAM', 'Оперативная память'),
        ('SSD', 'Накопитель'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"

class PCConfiguration(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cpu = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='cpu_orders', limit_choices_to={'category': 'CPU'})
    gpu = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='gpu_orders', limit_choices_to={'category': 'GPU'})
    ram = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='ram_orders', limit_choices_to={'category': 'RAM'})
    ssd = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='ssd_orders', limit_choices_to={'category': 'SSD'})
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.cpu.price + self.gpu.price + self.ram.price + self.ssd.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ #{self.id} от {self.customer_name}"
    
class WhoIsDFS(models.Model):
    text = models.CharField(max_length=255)
    text_2 = models.CharField(max_length=255)
    img = models.URLField()
    
    def __str__(self):
        return str(self.id)