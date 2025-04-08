from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class HotelPage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='hotel/', null=True, blank=True, default=DEFAULT_IMAGE)
    our_facilities_image = models.ImageField(upload_to='hotel/', null=True, blank=True, default=DEFAULT_IMAGE)
    our_services_image = models.ImageField(upload_to='hotel/', null=True, blank=True, default=DEFAULT_IMAGE)
    our_prices_subheading = models.TextField(
        default="Our exclusive accommodations provide comfort and luxury for your pet, ensuring a relaxing stay. Choose the best option for your furry companion and experience the finest care."
    )

    # Translatable fields (no need to redefine `hero_title` here)
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=255, default="Your Pets Luxury Stay"),
        hero_subheading=models.TextField(default="Let Your Pet Experience ultimate comfort and sophistication in our luxurious hotel."),
        our_facilities_title=models.CharField(max_length=255, default=" Where Luxury Meets Love"),
        our_facilities_subheading=models.TextField(default="State-of-the-art amenities designed to make your pets stay seamless, with luxury and convenience at every turn."),
        our_services_title=models.CharField(max_length=255, default="Only The Best For Your Pets"),
        our_services_subheading=models.TextField(default="Exceptional service that goes above and beyond to cater to your pets every need."),
        our_prices_title=models.CharField(max_length=255, default="Our Room Prices"),
        luxury_title=models.CharField(max_length=255, default="Luxury Like No Other"),
        luxury_subheading=models.TextField(default="Let your pet indulge in the finest amenities, elegant decor, and personalized experiences.")
    )

    def __str__(self):
        return "Hotel Page Content"

    class Meta:
        verbose_name = "Hotel Page Content"
        verbose_name_plural = "Hotel Page Content"


class ServicePage(TranslatableModel):
    DEFAULT_IMAGE = 'default/placeholder.jpg'

    # Non-translatable fields
    hero_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_hotel_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_meal_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_training_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_grooming_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_watersports_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)
    our_transportation_image = models.ImageField(upload_to='services/', blank=True, null=True, default=DEFAULT_IMAGE)

    # Translations for all text fields
    translations = TranslatedFields(
        hero_title=models.CharField(max_length=200, default="Our Services"),
        hero_subheading=models.CharField(max_length=300, default="Providing the best care for your pets while you're away."),
        our_hotel_title=models.CharField(max_length=200, default="Our Pet Hotel"),
        our_hotel_subheading=models.TextField(default="Our pet hotel offers a safe and comfortable environment for your pets. With spacious rooms, loving staff, and 24/7 care, your pet will feel right at home."),
        our_meal_title=models.CharField(max_length=200, default="Healthy Meals for Your Pet"),
        our_meal_subheading=models.TextField(default="We offer a variety of nutritious meals tailored to your pet's needs, ensuring they stay healthy and energized during their stay with us."),
        our_training_title=models.CharField(max_length=200, default="Professional Pet Training"),
        our_training_subheading=models.TextField(default="Our professional trainers provide personalized training sessions to ensure your pet’s obedience and good behavior."),
        our_grooming_title=models.CharField(max_length=200, default="Grooming Services"),
        our_grooming_subheading=models.TextField(default="Pamper your pet with our grooming services, including baths, trims, and nail care, to keep them looking and feeling their best."),
        our_watersports_title=models.CharField(max_length=200, default="Exciting Water Sports"),
        our_watersports_subheading=models.TextField(default="Let your pet enjoy fun-filled water activities that are both stimulating and enjoyable, keeping them active and happy."),
        our_transportation_title=models.CharField(max_length=200, default="Safe and Comfortable Transportation"),
        our_transportation_subheading=models.TextField(default="We offer transportation services to pick up and drop off your pet, ensuring they travel safely and comfortably to and from our hotel."),
    )

    def __str__(self):
        return f"Services Page Content"

    class Meta:
        verbose_name = "All Services Page Content"
        verbose_name_plural = "All Services Page Content"
