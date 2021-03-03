from django.contrib import admin

# Register your models here.
from skillsfinder.models import Skill, SkillCategory, Profile, Organisation

admin.site.register(Organisation)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(SkillCategory)
