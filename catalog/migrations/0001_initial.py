import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('cat_name', models.CharField(max_length=150,
                                              verbose_name='Наименование')),
                ('description', models.TextField(null=True,
                                                 verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['cat_name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('prod_name', models.CharField(max_length=150,
                                               verbose_name='Наименование')),
                ('description', models.TextField(null=True,
                                                 verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images/',
                                            verbose_name='Изображение')),
                ('category', models.CharField(verbose_name='Категория')),
                ('price', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'),
                                                     ('published', 'Published')],
                                            default='draft', max_length=10)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            to='catalog.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['prod_name'],
            },
        ),
    ]
