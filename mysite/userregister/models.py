from django.db import models

class User(models.Model):
    """docstring for User"""
    name = models.CharField(max_length = 100)
    borndate = models.DateField()
    age = models.IntegerField()
    job = models.CharField(max_length = 60)
    created_at = models.DateTimeField(auto_now_add = True)

    def __unicode__(self):
        return u'%s\n\t%s\n\t%s\n\t%s\n\t%s' % (self.name, self.borndate, self.age, self.job, self.created_at)
        