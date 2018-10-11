from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='errorMessage',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='webpage',
            name='errorType',
            field=models.IntegerField(default=0),
        ),
    ]
