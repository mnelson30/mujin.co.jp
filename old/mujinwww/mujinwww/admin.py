from django.contrib import admin
from models import NewsEntry, UserProfile, TranslatedNewsEntry
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class NewsEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(NewsEntry, NewsEntryAdmin)

class TranslatedNewsEntryAdmin(admin.ModelAdmin):
    pass
admin.site.register(TranslatedNewsEntry, TranslatedNewsEntryAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [UserProfileInline]

# unregister old user admin
admin.site.unregister(User)

# register new user admin
admin.site.register(User, UserAdmin)
