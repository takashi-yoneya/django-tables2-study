# Generated by Django 3.1.6 on 2021-02-27 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TorihikiModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=100, verbose_name='アカウントID')),
                ('yahoo_account_id', models.CharField(max_length=100, verbose_name='ヤフーID')),
                ('item_name', models.CharField(max_length=256, verbose_name='商品名')),
                ('buied_price', models.IntegerField(default=0, verbose_name='落札価格')),
                ('shipping_data', models.CharField(default=0, max_length=1024, verbose_name='落札価格')),
                ('torihiki_stat', models.IntegerField(default=0, verbose_name='取引ステータス')),
                ('matome_flg', models.BooleanField(default=False, verbose_name='まとめフラグ')),
                ('eval_flg', models.BooleanField(default=False, verbose_name='評価済フラグ')),
                ('shipping_notice_flg', models.BooleanField(default=False, verbose_name='発送連絡済フラグ')),
                ('auction_id', models.CharField(max_length=20, null=True, verbose_name='オークションID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('rakusatsu_at', models.DateTimeField(null=True, verbose_name='更新日時')),
                ('shipped_at', models.DateTimeField(null=True, verbose_name='発送完了日時')),
                ('completed_at', models.DateTimeField(null=True, verbose_name='取引完了日時')),
            ],
            options={
                'db_table': 't_torihiki_data',
            },
        ),
    ]