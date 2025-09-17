from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sobrenome',
            field=models.CharField(default='Sobrenome', max_length=150),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default='Nome de usuário', max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='Nome', max_length=30),
        ),
    ]
