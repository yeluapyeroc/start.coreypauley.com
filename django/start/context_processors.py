from django.contrib.sites.models import Site

def site_info(request):
    """
    Adds the current site's info
    """

    return {
            'domain': Site.objects.get_current().domain
            }
