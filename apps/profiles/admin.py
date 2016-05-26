from django.contrib import admin

from apps.profiles.models import Profile, Rating, Bonus


class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'points']
    search_fields = ['user', 'user__username']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['user__username']


class BonusAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'code', 'points']
    search_fields = ['name', 'code', 'user__username']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Bonus, BonusAdmin)
