from django.contrib.syndication.views import Feed
from blog.models import Entry

class LatestPosts(Feed):
    title = "ED Blog"
    link = "/feed/"
    description = "Derniers Posts"

    def items(self):
        return Entry.objects.published()[:5]
