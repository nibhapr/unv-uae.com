from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.urls import reverse
from meta.models import ModelMeta
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.core.files import File
import os
# Category Model


class CategorySEO(models.Model):
    category = models.OneToOneField(
        'Category', on_delete=models.CASCADE, related_name='seo')
    meta_title = models.CharField(
        max_length=60, blank=True, help_text="Max 60 characters for optimal SEO")
    meta_description = models.TextField(
        max_length=160, blank=True, help_text="Max 160 characters for optimal SEO")
    meta_keywords = models.CharField(
        max_length=255, blank=True, help_text="Comma-separated keywords")
    og_title = models.CharField(
        max_length=60, blank=True, help_text="Open Graph title")
    og_description = models.TextField(
        max_length=200, blank=True, help_text="Open Graph description")
    og_image = models.ImageField(upload_to='category/og-images/', blank=True)
    canonical_url = models.URLField(
        blank=True, help_text="Canonical URL if different from default")

    def save(self, *args, **kwargs):
        if not self.meta_title and self.category:
            self.meta_title = f"{self.category.name} - Uniview Products"

        if not self.meta_description and self.category:
            self.meta_description = (self.category.description[:157] + '...') if len(
                self.category.description) > 160 else self.category.description

        if not self.meta_keywords and self.category:
            self.meta_keywords = f"{self.category.name}, Uniview, security products, {self.category.name.lower()} products"

        if not self.og_title and self.category:
            self.og_title = self.meta_title

        if not self.og_description and self.category:
            self.og_description = self.meta_description

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Category SEO"
        verbose_name_plural = "Category SEOs"

    def __str__(self):
        return f"SEO for {self.category.name}"


class Category(models.Model, ModelMeta):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, default='default-slug')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='category/%Y/%m/%d/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'slug': self.slug})

    def image_preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" />')
        return ''

# Product Model


class ProductSEO(models.Model):
    product = models.OneToOneField(
        'Product', on_delete=models.CASCADE, related_name='seo')
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    keywords = models.CharField(max_length=500, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    review_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.title and self.product:
            self.title = f"{self.product.name} - {self.product.category.name} | Uniview"

        if not self.description and self.product:
            self.description = (self.product.description[:297] + '...') if len(
                self.product.description) > 300 else self.product.description

        if not self.keywords and self.product:
            keywords = [
                self.product.name,
                self.product.category.name,
                "Uniview",
                "security camera",
                "surveillance",
                self.product.category.name.lower(),
                "Dubai",
                "UAE"
            ]
            self.keywords = ", ".join(keywords)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product SEO"
        verbose_name_plural = "Product SEOs"


class Product(models.Model, ModelMeta):
    # Basic Information
    category = models.ForeignKey(
        'Category', 
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    # Camera Specifications
    max_resolution = models.CharField(max_length=100, blank=True, null=True)
    sensor = models.CharField(max_length=100, blank=True, null=True)
    day_night = models.CharField(max_length=100, blank=True, null=True)
    shutter = models.CharField(max_length=100, blank=True, null=True)
    adjustment_angle = models.CharField(max_length=100, blank=True, null=True)
    s_n = models.CharField(max_length=100, blank=True, null=True)
    wdr = models.CharField(max_length=100, blank=True, null=True)

    # Lens Specifications
    focal_length = models.CharField(max_length=100, blank=True, null=True)
    iris_type = models.CharField(max_length=100, blank=True, null=True)
    iris = models.CharField(max_length=100, blank=True, null=True)

    # Video Specifications
    video_compression = models.CharField(max_length=100, blank=True, null=True)
    frame_rate = models.CharField(max_length=100, blank=True, null=True)
    video_bit_rate = models.CharField(max_length=100, blank=True, null=True)
    video_stream = models.CharField(max_length=100, blank=True, null=True)

    # Audio Specifications
    audio_compression = models.CharField(max_length=100, blank=True, null=True)
    two_way_audio = models.CharField(max_length=100, blank=True, null=True)
    suppression = models.CharField(max_length=100, blank=True, null=True)
    sampling_rate = models.CharField(max_length=100, blank=True, null=True)

    # Storage
    edge_storage = models.CharField(max_length=100, blank=True, null=True)
    network_storage = models.CharField(max_length=100, blank=True, null=True)

    # Network
    protocols = models.CharField(max_length=100, blank=True, null=True)
    compatible_integration = models.CharField(
        max_length=100, blank=True, null=True)

    # General Specifications
    power = models.CharField(max_length=100, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)

    # Images
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    # Metadata
    list_date = models.DateTimeField(default=timezone.now, blank=True)
    is_published = models.BooleanField(default=True)
    is_mvp = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    _meta_title = 'name'
    _meta_description = 'description'
    _meta_image = 'photo_main'

    def save(self, *args, **kwargs):
        # Generate slug if not present
        if not self.slug:
            self.slug = slugify(self.name)

        # Save the product first
        super(Product, self).save(*args, **kwargs)

        # Create or update SEO information
        seo, created = ProductSEO.objects.get_or_create(product=self)

        # Update SEO fields with location-specific optimization
        if not seo.title:
            seo.title = f"{self.name} - Security Camera Price in Dubai, UAE | Uniview"

        if not seo.description:
            seo.description = f"Buy {self.name} in UAE at best prices. Professional Uniview security camera with expert installation in Dubai, Abu Dhabi & Sharjah. Contact for latest CCTV prices."

        if not seo.keywords:
            # Enhanced keywords with location targeting
            base_keywords = [
                f"Uniview {self.name}",
                f"UNV {self.name} Dubai",
                f"{self.name} price UAE",
                f"buy {self.name} Dubai",
                f"{self.name} Abu Dhabi",
                f"{self.name} Sharjah",
                "security camera UAE",
                "CCTV installation Dubai",
                "Uniview dealer UAE",
                "security systems Dubai",
                f"{self.category.name} price Dubai",
                f"best {self.category.name} UAE",
                "surveillance systems UAE",
                "security camera installation Dubai"
            ]

            # Add city-specific keywords
            uae_cities = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman", 
                         "Ras Al Khaimah", "Fujairah", "Umm Al Quwain", "Al Ain"]
            
            for city in uae_cities:
                base_keywords.extend([
                    f"Uniview {self.category.name} {city}",
                    f"security camera price {city}",
                    f"CCTV installation {city}",
                    f"security systems {city}"
                ])

            seo.keywords = ", ".join(base_keywords)

        # Calculate rating and review count
        reviews = self.reviews.all()
        if reviews.exists():
            seo.rating = sum(review.rating for review in reviews) / reviews.count()
            seo.review_count = reviews.count()

        seo.save()

    def __str__(self):
        return self.name  # Changed to 'name' instead of 'title'

    def get_absolute_url(self):
        # Assuming you have a URL pattern named 'product_detail' for products
        return reverse('products:product_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

# Inquiry Model


class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True,
                             default='No phone number provided')
    message = models.TextField(default='No message provided')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Add this model to your existing models.py


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Review by {self.name} for {self.product.name}'
