from django.db import models

class Client(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=100)
    comment = models.TextField()

class Mailing(models.Model):
    send_time = models.DateTimeField()
    frequency = models.CharField(max_length=10, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')])
    status = models.CharField(max_length=10, choices=[('completed', 'Completed'), ('created', 'Created'), ('started', 'Started')])

class Message(models.Model):
    subject = models.CharField(max_length=100)
    body = models.TextField()

class MailingLog(models.Model):
    last_attempt = models.DateTimeField()
    status = models.CharField(max_length=10, choices=[('success', 'Success'), ('failure', 'Failure')])
    server_response = models.TextField()
