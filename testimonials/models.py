from django.db import models
from django.utils.translation import ugettext_lazy as _

class ClientTestimonies (models.Model):
    """
    the client testimonies goes here and the functions as well 
    """

    client_full_name = models.CharField(
        max_length=120,
        verbose_name=_("Client Full Name"),
        null = True,
        help_text=_("The legal full name of the client.")
    )

    client_comment = models.TextField(
        verbose_name=_("Client Comment"),
        null = True,
        help_text=_("The Client Comment.")
    )

    client_position = models.CharField(
        verbose_name=_("Client Position"),
        max_length=50,
        null = True,
        help_text=_("The Client Position.")
    )

    client_image = models.ImageField(
        verbose_name=_("Client Image"),
        null = True,
        upload_to = 'client_image/',
        default = 'image.png',
        help_text=_("The Client Image.")
    )


    class Meta :
        verbose_name = _("Client Feedback")
        verbose_name_plural = _("Client Feedback")

    def __str__(self):
        return str(self.client_full_name)






class FAQ (models.Model):

    questions  = models.CharField(
        verbose_name = _("Customers Questions"),
        max_length=500,
        null = True, 
        help_text=_("client FAQ questions and answers.")
        )

    answers = models.TextField(
        verbose_name = _("Customers Answers"),
        null = True, 
        help_text=_("Customers Answers.")
    )

    #Metadata
    class Meta :
        # 
        verbose_name = _("FAQ questions and answers")
        verbose_name_plural = _("FAQ questions and answers")

    #Methods
    # def get_absolute_url(self):
    #     return reverse('url', args=[args])

    def __str__(self):
        return self.questions


