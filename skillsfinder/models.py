from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class VersionedModel(models.Model):
    created = models.DateTimeField(blank=True, auto_now_add=True)
    last_modified = models.DateTimeField(blank=True, auto_now=True)

    class Meta:
        abstract = True


class Organisation(VersionedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkillCategory(VersionedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Skill(VersionedModel):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class Profile(VersionedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name="staff")

    title = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    skills = models.ManyToManyField(Skill, through='SkillRecord')

    class Meta:
        ordering = ('user__first_name', 'user__last_name', )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class SkillRecord(VersionedModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
