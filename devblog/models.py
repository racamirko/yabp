from django.db import models
import loremipsum as LI
import random as rnd

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Tag: "+self.name


class Story(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return "Story: "+self.title


def __auto_populate(num_of_stories=10, num_of_tags=10):
    # generate tags
    for i in xrange(num_of_tags):
        t = Tag(name=LI.get_sentence().split()[0])
        t.save()
    tags = Tag.objects.all()
    for i in xrange(num_of_stories):
        s = Story(title=LI.get_sentence(), body=LI.get_paragraph())
        s.save()
        for j in xrange(rnd.randint(1, 4)):
            tag_idx = rnd.randint(0, len(tags)-1)
            s.tag.add(tags[tag_idx])
        s.save()
