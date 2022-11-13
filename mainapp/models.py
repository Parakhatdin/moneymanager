from django.db import models

class Member(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "members"

class MemberAuthdata(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length = 150)
    member_id = models.ForeignKey(Member, on_delete = models.CASCADE)
    class Meta:
        db_table = "member_authdatas"

class Family(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "families"

class FamilyMember(models.Model):
    member_id = models.BigIntegerField()
    family_id = models.BigIntegerField()
    class Meta:
        db_table = "family_members"
        unique_together = (('member_id', 'family_id'))

class Envelope(models.Model):
    name = models.CharField(max_length = 150)
    member_id = models.ForeignKey(Member, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "envelopes"

class Category(models.Model):
    name = models.CharField(max_length = 150)
    is_income = models.BooleanField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    amount = models.BigIntegerField()
    envelope_id = models.ForeignKey(Envelope, on_delete = models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete = models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.amount)
