from django.contrib import admin
from .models import EmergencyAlert, UserProfile
from django.utils.html import format_html
from django.contrib import admin

#
class EmergencyAlertAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'video_file_link', 'video_file_player', 'timestamp', 'description')
    search_fields = ('user__username', 'location', 'description')
    list_filter = ('timestamp',)

    def video_file_link(self, obj):
        if obj.video_file:
            return format_html('<a href="{}" target="_blank">video.mp4</a>', obj.video_file.url)
        return '-'
    video_file_link.short_description = 'Video File'

    def video_file_player(self, obj):
        if obj.video_file:
            return format_html('<video width="320" height="240" controls><source src="{}" type="video/mp4"></video>', obj.video_file.url)
        return 'No video'
    video_file_player.short_description = 'Video Preview'

    exclude = ('timestamp',)
    fields = ('user', 'location', 'video_file', 'description')

class UserProfileAdmin(admin.ModelAdmin):
    # Display relevant fields in the list view for user profiles
    list_display = ('user', 'phone_number', 'address', 'last_login_time')
    search_fields = ('user__username',)  # Allows search by username

    # Adding last login time as a custom field in the admin
    def last_login_time(self, obj):
        return obj.user.last_login
    last_login_time.short_description = 'Last Login Time'

# Register models with their custom admin configurations
admin.site.register(EmergencyAlert, EmergencyAlertAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
