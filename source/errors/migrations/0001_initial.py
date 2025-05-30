# Generated by Django 5.1.7 on 2025-04-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error_400', models.FileField(default='default/error_400.mp4', help_text='Upload the 400 error video', upload_to='errors/videos/')),
                ('error_403', models.FileField(default='default/error_403.mp4', help_text='Upload the 403 error video', upload_to='errors/videos/')),
                ('error_404', models.FileField(default='default/error_404.mp4', help_text='Upload the 404 error video', upload_to='errors/videos/')),
                ('error_500', models.FileField(default='default/error_500.mp4', help_text='Upload the 404 error video', upload_to='errors/videos/')),
            ],
        ),
    ]
