# Generated by Django 4.2.4 on 2023-08-22 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Название кампании')),
                ('refer_id', models.PositiveIntegerField(verbose_name='Telegram ID кампании')),
                ('refer_url', models.URLField(verbose_name='Ссылка на кампанию')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
            ],
            options={
                'verbose_name': 'Рекламная кампания',
                'verbose_name_plural': 'Рекламные кампании',
            },
        ),
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bouquets', verbose_name='Изображение')),
                ('name', models.CharField(max_length=40, verbose_name='Название букета')),
                ('meaning', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Букет',
                'verbose_name_plural': 'Букеты',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(verbose_name='Telegram ID')),
                ('first_name', models.CharField(max_length=40, null=True, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('personal_data_consent', models.BooleanField(default=False, verbose_name='Согласие на обработку персональных данных')),
                ('advertisement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='shopbot.advertisement', verbose_name='Рекламная кампания')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='Consulting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('contact_phone', models.CharField(max_length=40, verbose_name='Контактный телефон')),
                ('first_call_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время звонка')),
                ('occasion_text', models.CharField(blank=True, max_length=40, verbose_name='Повод (уточнение)')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consultings', to='shopbot.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Консультация',
                'verbose_name_plural': 'Консультации',
            },
        ),
        migrations.CreateModel(
            name='ConsultingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус консультации',
                'verbose_name_plural': 'Статусы консультаций',
            },
        ),
        migrations.CreateModel(
            name='Gamma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Гамма')),
            ],
            options={
                'verbose_name': 'Гамма',
                'verbose_name_plural': 'Гаммы',
            },
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Повод')),
            ],
            options={
                'verbose_name': 'Повод',
                'verbose_name_plural': 'Поводы',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveBigIntegerField(verbose_name='Telegram ID')),
                ('first_name', models.CharField(max_length=40, null=True, verbose_name='Имя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('last_name', models.CharField(max_length=40, verbose_name='Фамилия')),
                ('role', models.CharField(choices=[('admin', 'Админ'), ('florist', 'Флорист'), ('currier', 'Курьер')], max_length=40, verbose_name='Роль')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата начала работы')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата увольнения')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('processing', 'В обработке'), ('ready', 'Готов'), ('delivered', 'Доставлен'), ('canceled', 'Отменен')], max_length=40, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('delivery_date', models.DateTimeField(verbose_name='Дата доставки')),
                ('delivery_address', models.CharField(max_length=200, verbose_name='Адрес доставки')),
                ('contact_phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
                ('contact_name', models.CharField(max_length=40, verbose_name='Контактное лицо')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shopbot.bouquet', verbose_name='Букет')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shopbot.client', verbose_name='Клиент')),
                ('consultation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shopbot.consulting', verbose_name='Консультация')),
                ('currier', models.ForeignKey(blank=True, limit_choices_to={'role': 'currier'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='shopbot.staff', verbose_name='Курьер')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название цветка')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='flowers', to='shopbot.colors', verbose_name='Цвет')),
            ],
            options={
                'verbose_name': 'Цветок',
                'verbose_name_plural': 'Цветы',
            },
        ),
        migrations.CreateModel(
            name='ConsultingStatusHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('consulting', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_history', to='shopbot.consulting', verbose_name='Консультация')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_history', to='shopbot.consultingstatus', verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'История статусов консультации',
                'verbose_name_plural': 'Истории статусов консультаций',
            },
        ),
        migrations.AddField(
            model_name='consulting',
            name='florist',
            field=models.ForeignKey(limit_choices_to={'role': 'florist'}, on_delete=django.db.models.deletion.PROTECT, related_name='consultings', to='shopbot.staff', verbose_name='Флорист'),
        ),
        migrations.AddField(
            model_name='consulting',
            name='gamma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consultings', to='shopbot.gamma', verbose_name='Гамма'),
        ),
        migrations.AddField(
            model_name='consulting',
            name='occasion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='consultings', to='shopbot.occasion', verbose_name='Повод'),
        ),
        migrations.AddField(
            model_name='consulting',
            name='status',
            field=models.ManyToManyField(through='shopbot.ConsultingStatusHistory', to='shopbot.consultingstatus'),
        ),
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Количество')),
                ('bouquet', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='composition', to='shopbot.bouquet', verbose_name='Букет')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='composition', to='shopbot.flower', verbose_name='Цветок')),
            ],
            options={
                'verbose_name': 'Состав',
                'verbose_name_plural': 'Составы',
            },
        ),
        migrations.AddField(
            model_name='bouquet',
            name='flowers',
            field=models.ManyToManyField(related_name='bouquets', through='shopbot.Composition', to='shopbot.flower', verbose_name='Цветы'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='occasion',
            field=models.ManyToManyField(related_name='bouquets', to='shopbot.occasion', verbose_name='Повод'),
        ),
    ]