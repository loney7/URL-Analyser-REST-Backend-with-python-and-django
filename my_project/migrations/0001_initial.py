from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
                ('h1Count', models.IntegerField()),
                ('h2Count', models.IntegerField()),
                ('h3Count', models.IntegerField()),
                ('h4Count', models.IntegerField()),
                ('h5Count', models.IntegerField()),
                ('h6Count', models.IntegerField()),
                ('version', models.CharField(max_length=100)),
                ('internalLinkCount', models.IntegerField()),
                ('externalLinkCount', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('inaccessibleLinkCount', models.IntegerField()),
                ('statusCode', models.IntegerField()),
                ('timeStamp', models.CharField(max_length=100)),
                ('loginForm', models.BooleanField()),
            ],
        ),
    ]
