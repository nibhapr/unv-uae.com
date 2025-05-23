# Generated by Django 5.1.6 on 2025-02-26 06:37

import django.db.models.deletion
import django.utils.timezone
import meta.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(default='default-slug', unique=True)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='category/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, meta.models.ModelMeta),
        ),
        migrations.CreateModel(
            name='CategorySEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, help_text='Max 60 characters for optimal SEO', max_length=60)),
                ('meta_description', models.TextField(blank=True, help_text='Max 160 characters for optimal SEO', max_length=160)),
                ('meta_keywords', models.CharField(blank=True, help_text='Comma-separated keywords', max_length=255)),
                ('og_title', models.CharField(blank=True, help_text='Open Graph title', max_length=60)),
                ('og_description', models.TextField(blank=True, help_text='Open Graph description', max_length=200)),
                ('og_image', models.ImageField(blank=True, upload_to='category/og-images/')),
                ('canonical_url', models.URLField(blank=True, help_text='Canonical URL if different from default')),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seo', to='products.category')),
            ],
            options={
                'verbose_name': 'Category SEO',
                'verbose_name_plural': 'Category SEOs',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('is_featured', models.BooleanField(default=False)),
                ('max_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('sensor', models.CharField(blank=True, max_length=100, null=True)),
                ('day_night', models.CharField(blank=True, max_length=100, null=True)),
                ('shutter', models.CharField(blank=True, max_length=100, null=True)),
                ('adjustment_angle', models.CharField(blank=True, max_length=100, null=True)),
                ('s_n', models.CharField(blank=True, max_length=100, null=True)),
                ('wdr', models.CharField(blank=True, max_length=100, null=True)),
                ('focal_length', models.CharField(blank=True, max_length=100, null=True)),
                ('iris_type', models.CharField(blank=True, max_length=100, null=True)),
                ('iris', models.CharField(blank=True, max_length=100, null=True)),
                ('lens_type', models.CharField(blank=True, max_length=100, null=True)),
                ('video_compression', models.CharField(blank=True, max_length=100, null=True)),
                ('frame_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('video_bit_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('video_stream', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_video_input', models.CharField(blank=True, max_length=100, null=True)),
                ('recording_resolution', models.CharField(blank=True, max_length=100, null=True)),
                ('audio_compression', models.CharField(blank=True, max_length=100, null=True)),
                ('audio_bitrate', models.CharField(blank=True, max_length=100, null=True)),
                ('two_way_audio', models.CharField(blank=True, max_length=100, null=True)),
                ('suppression', models.CharField(blank=True, max_length=100, null=True)),
                ('sampling_rate', models.CharField(blank=True, max_length=100, null=True)),
                ('rca_audio_output', models.CharField(blank=True, max_length=100, null=True)),
                ('edge_storage', models.CharField(blank=True, max_length=100, null=True)),
                ('network_storage', models.CharField(blank=True, max_length=100, null=True)),
                ('sata', models.CharField(blank=True, max_length=100, null=True)),
                ('protocols', models.CharField(blank=True, max_length=100, null=True)),
                ('compatible_integration', models.CharField(blank=True, max_length=100, null=True)),
                ('incoming_bandwidth', models.CharField(blank=True, max_length=100, null=True)),
                ('outgoing_bandwidth', models.CharField(blank=True, max_length=100, null=True)),
                ('network_interface', models.CharField(blank=True, max_length=100, null=True)),
                ('poe', models.CharField(blank=True, max_length=100, null=True)),
                ('hdmi_video_output', models.CharField(blank=True, max_length=100, null=True)),
                ('vga_video_output', models.CharField(blank=True, max_length=100, null=True)),
                ('hdmi_audio_output', models.CharField(blank=True, max_length=100, null=True)),
                ('vga_audio_output', models.CharField(blank=True, max_length=100, null=True)),
                ('power', models.CharField(blank=True, max_length=100, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('material', models.CharField(blank=True, max_length=100, null=True)),
                ('decoding_format', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_main', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('is_available', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('is_mvp', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, meta.models.ModelMeta),
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, default='No phone number provided', max_length=15)),
                ('message', models.TextField(default='No message provided')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductSEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('keywords', models.CharField(blank=True, max_length=500)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('review_count', models.PositiveIntegerField(default=0)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seo', to='products.product')),
            ],
            options={
                'verbose_name': 'Product SEO',
                'verbose_name_plural': 'Product SEOs',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('review', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
