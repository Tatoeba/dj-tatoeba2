# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

# Datetime conversion back and forth from MySQL to Python fails when datetime
# is zero. MySQL allows datetime to be zero, while Python doesn't. When Python
# is unable to interpret a datetime, it replaces it by None (see MySQLdb.times,
# def DateTime_or_None), which stands for NULL to MySQL, whereas the column
# can't be NULL, so MySQL complains.
class ZeroedDateTimeField(models.DateTimeField):
    def get_db_prep_value(self, value, connection, prepared=False):
        value = super(ZeroedDateTimeField, self).get_db_prep_value(value, connection, prepared)
        if value is None:
            return '0000-00-00 00:00:00'
        else:
            return value

class Audios(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    class Meta:
        db_table = 'audios'

class Contributions(models.Model):
    sentence_id = models.IntegerField()
    sentence_lang = models.CharField(max_length=4, blank=True)
    translation_id = models.IntegerField(blank=True, null=True)
    translation_lang = models.CharField(max_length=4, blank=True)
    script = models.CharField(max_length=4, blank=True)
    text = models.CharField(max_length=1500)
    action = models.CharField(max_length=6)
    user_id = models.IntegerField(blank=True, null=True)
    datetime = ZeroedDateTimeField()
    type = models.CharField(max_length=8)
    id = models.AutoField(primary_key=True, unique=True)
    class Meta:
        db_table = 'contributions'

class ContributionsStats(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    date = models.DateField(blank=True, null=True)
    lang = models.CharField(max_length=4, blank=True)
    sentences = models.IntegerField(blank=True, null=True)
    action = models.CharField(max_length=6)
    type = models.CharField(max_length=8)

    class Meta:
        db_table = 'contributions_stats'

class DisabledAudios(models.Model):
    id = models.IntegerField(primary_key=True)
    sentence_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    external = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    class Meta:
        db_table = 'disabled_audios'

class FavoritesUsers(models.Model):
    id = models.AutoField(primary_key=True)
    favorite_id = models.IntegerField()
    user_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'favorites_users'
        unique_together = ('favorite_id', 'user_id')

class Languages(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(unique=True, max_length=4, blank=True)
    sentences = models.IntegerField()
    audio = models.IntegerField()
    group_1 = models.IntegerField()
    group_2 = models.IntegerField()
    group_3 = models.IntegerField()
    group_4 = models.IntegerField()
    level_0 = models.IntegerField()
    level_1 = models.IntegerField()
    level_2 = models.IntegerField()
    level_3 = models.IntegerField()
    level_4 = models.IntegerField()
    level_5 = models.IntegerField()
    level_unknown = models.IntegerField()

    class Meta:
        db_table = 'languages'

class LastContributions(models.Model):
    sentence_id = models.IntegerField()
    sentence_lang = models.CharField(max_length=4, blank=True)
    translation_id = models.IntegerField(blank=True, null=True)
    translation_lang = models.CharField(max_length=4, blank=True)
    script = models.CharField(max_length=4, blank=True)
    text = models.CharField(max_length=1500)
    action = models.CharField(max_length=6)
    user_id = models.IntegerField(blank=True, null=True)
    datetime = models.DateTimeField()
    type = models.CharField(max_length=8)
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'last_contributions'

class PrivateMessages(models.Model):
    id = models.AutoField(primary_key=True)
    recpt = models.IntegerField()
    sender = models.IntegerField()
    user_id = models.IntegerField()
    date = models.DateTimeField()
    folder = models.CharField(max_length=6)
    title = models.CharField(max_length=255)
    content = models.TextField()
    isnonread = models.IntegerField()
    draft_recpts = models.CharField(max_length=255)
    sent = models.IntegerField()
    class Meta:
        db_table = 'private_messages'

class ReindexFlags(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    lang = models.CharField(max_length=4, blank=True)
    indexed = models.IntegerField()
    type = models.CharField(max_length=7)

    class Meta:
        db_table = 'reindex_flags'

class SentenceAnnotations(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    meaning_id = models.IntegerField()
    text = models.CharField(max_length=2000)
    modified = models.DateTimeField()
    user_id = models.IntegerField()
    class Meta:
        db_table = 'sentence_annotations'

class SentenceComments(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    lang = models.CharField(max_length=4, blank=True)
    text = models.TextField()
    user_id = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    hidden = models.IntegerField()
    class Meta:
        db_table = 'sentence_comments'

class Sentences(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=4, blank=True)
    text = models.CharField(max_length=1500)
    correctness = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    script = models.CharField(max_length=4, blank=True)
    class Meta:
        db_table = 'sentences'

    def __str__(self):
        return '<Sentence: id={}>'.format(str(self.id))

class SentencesLists(models.Model):
    id = models.AutoField(primary_key=True)
    is_public = models.IntegerField()
    name = models.CharField(max_length=450)
    user_id = models.IntegerField(blank=True, null=True)
    numberofsentences = models.IntegerField(db_column='numberOfSentences') # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    visibility = models.CharField(max_length=8)
    editable_by = models.CharField(max_length=7)

    class Meta:
        db_table = 'sentences_lists'

class SentencesSentencesLists(models.Model):
    id = models.AutoField(primary_key=True)
    sentences_list_id = models.IntegerField()
    sentence_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'sentences_sentences_lists'
        unique_together = ('sentences_list_id', 'sentence_id')

class SentencesTranslations(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    translation_id = models.IntegerField()
    sentence_lang = models.CharField(max_length=4, blank=True)
    translation_lang = models.CharField(max_length=4, blank=True)
    distance = models.IntegerField()
    class Meta:
        db_table = 'sentences_translations'
        unique_together = ('sentence_id', 'translation_id')

class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    internal_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True)
    user_id = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    nbrofsentences = models.IntegerField(db_column='nbrOfSentences') # Field name made lowercase.
    class Meta:
        db_table = 'tags'

class TagsSentences(models.Model):
    id = models.AutoField(primary_key=True)
    tag_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    sentence_id = models.IntegerField(blank=True, null=True)
    added_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'tags_sentences'

class Transcriptions(models.Model):
    id = models.AutoField(primary_key=True)
    sentence_id = models.IntegerField()
    script = models.CharField(max_length=4)
    text = models.CharField(max_length=10000)
    user_id = models.IntegerField(blank=True, null=True)
    needsreview = models.IntegerField(db_column='needsReview')  # Field name made lowercase.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        db_table = 'transcriptions'
        unique_together = ('sentence_id', 'script')

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    since = models.DateTimeField()
    last_time_active = models.IntegerField()
    level = models.IntegerField()
    role = models.CharField(max_length=20)
    send_notifications = models.IntegerField()
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    settings = models.TextField()
    homepage = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    country_id = models.CharField(max_length=2, blank=True)
    audio_license = models.CharField(max_length=50, blank=True)
    audio_attribution_url = models.CharField(max_length=255, blank=True)
    class Meta:
        db_table = 'users'

class UsersLanguages(models.Model):
    id = models.AutoField(primary_key=True)
    of_user_id = models.IntegerField()
    by_user_id = models.IntegerField()
    language_code = models.CharField(max_length=4)
    level = models.IntegerField(blank=True, null=True)
    level_approval_status = models.CharField(max_length=10)
    details = models.TextField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'users_languages'
        unique_together = ('of_user_id', 'by_user_id', 'language_code')

class UsersVocabulary(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    vocabulary_id = models.IntegerField()
    class Meta:
        db_table = 'users_vocabulary'

class Visitors(models.Model):
    ip = models.CharField(primary_key=True, unique=True, max_length=15)
    timestamp = models.IntegerField()
    class Meta:
        db_table = 'visitors'

class Vocabulary(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=4, blank=True)
    text = models.CharField(max_length=1500)
    numsentences = models.IntegerField(db_column='numSentences', blank=True, null=True)  # Field name made lowercase.
    numadded = models.IntegerField(db_column='numAdded', blank=True, null=True)  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'vocabulary'

class Wall(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)
    hidden = models.IntegerField()
    modified = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'wall'

class WallThreadsLastMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    last_message_date = models.DateTimeField()
    class Meta:
        db_table = 'wall_threads_last_message'

class UsersSentences(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    sentence_id = models.IntegerField()
    correctness = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    dirty = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'users_sentences'
        unique_together = ('user_id', 'sentence_id')

from django.conf import settings

if not settings.MANAGE_DB:
    import sys
    import inspect

    mmbrs = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    tbls = [m[1] for m in mmbrs]
    for tbl in tbls:
        if hasattr(tbl, '_meta'): tbl._meta.managed = False
