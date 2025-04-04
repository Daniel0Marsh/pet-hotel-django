from django.db import models


class Branding(models.Model):
    """
    Model representing the Branding information for the website.

    This model stores essential details such as the company’s branding elements,
    contact information, meta tags, and media assets.
    """

    company_name = models.CharField(max_length=255, help_text="Enter the full name of the company.")
    company_email = models.EmailField(help_text="Enter the official company email address.")
    company_phone = models.CharField(max_length=20, help_text="Enter the company’s contact number (e.g., +1-234-567-8901).")
    company_address = models.CharField(max_length=255, help_text="Enter the full address of the company, including city and ZIP code.")

    logo = models.ImageField(upload_to="branding/", help_text="Upload the website logo.")
    favicon = models.ImageField(upload_to="branding/", help_text="Upload the favicon (ICO or PNG).")

    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Enter meta keywords for SEO (comma-separated).")
    meta_description = models.TextField(blank=True, help_text="Enter a meta description for SEO.")

    twitter_link = models.URLField(blank=True, help_text="Link to your Twitter profile.")
    facebook_link = models.URLField(blank=True, help_text="Link to your Facebook page.")
    instagram_link = models.URLField(blank=True, help_text="Link to your Instagram profile.")

    def __str__(self):
        return f"Branding Info for {self.company_name}"