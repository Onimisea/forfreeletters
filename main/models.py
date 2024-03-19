from django.db import models


# Create your models here.
class GenericTemplate(models.Model):
    CATEGORY_CHOICES = [
        ('cv', 'CV'),
        ('cover-letters', 'Cover Letters'),
        ('business-letters', 'Business Letters'),
        ('recommendation-letters', 'Recommendation Letters'),
        ('statement-of-purpose', 'Statement of Purpose'),
        ('biography', 'Biography'),
    ]

    SUBCATEGORY_CHOICES = [
        ('academic-&-education', 'Academic & Education'),
        ('art-design-&-fashion', 'Art, Design & Fashion'),
        ('hospitality-&-entertainment', 'Hospitality & Entertainment'),
        ('management-&-business', 'Management & Business'),
        ('healthcare-&-wellness', 'Healthcare & Wellness'),
        ('information-technology-it', 'Information Technology (IT)'),
        ('marketing-&-digital-marketing', 'Marketing & Digital Marketing'),
        ('legal-&-criminal-justice', 'Legal & Criminal Justice'),
        ('sales-&-customer-service', 'Sales & Customer Service'),
        ('human-resources-&-recruitment', 'Human Resources & Recruitment'),
        ('logistics-&-supply-chain', 'Logistics & Supply Chain'),
        ('communications-&-public-relations', 'Communications & Public Relations'),
        ('creative-arts-&-media-production', 'Creative Arts & Media Production'),
        ('government-&-diplomacy', 'Government & Diplomacy'),
        ('financial-services-&-consulting', 'Financial Services & Consulting'),
        ('miscellaneous', 'Miscellaneous'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='cv')
    subcategory = models.CharField(max_length=100, choices=SUBCATEGORY_CHOICES, default='academic-and-education')
    name = models.CharField(max_length=255, default='')
    file_upload = models.FileField(upload_to='media/generic_templates/', default='')
    image_preview = models.ImageField(upload_to='media/generic_templates/previews/', default='')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.subcategory}, {self.category})"
    
    class Meta:
        verbose_name = 'Generic Template'
        verbose_name_plural = 'Generic Templates'




