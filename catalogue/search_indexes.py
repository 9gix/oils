from haystack import indexes

from . import models

class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return models.Book

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(instances__isnull=False)

