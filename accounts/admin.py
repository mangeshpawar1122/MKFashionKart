from django.contrib import admin
from .models import Account,UserProfile
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
# Register your models here.

class AccountAdmin(UserAdmin):

    list_display = ('email',  'first_name', 'last_name','username', 'date_joined', 'last_login','is_active')
    list_display_links = ('email', 'first_name','last_name')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

#class UserProfileAdmin(admin.ModelAdmin):
#    def thumbnail(self,object):
 #       return format_html('<img src="{}" width="30" style="border-redius:50%">'.format(object.profile_picture.url))
  #  thumbnail.short_description='Profile Picture'
   # list_display=('thumbnail','user','city','state','country')

#pufrom django.contrib import admin
#from django.utils.html import format_html
#from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('thumbnail', 'user', 'city', 'state', 'country')

    def thumbnail(self, obj):
        if obj.profile_picture and obj.profile_picture.name:
            return format_html(
                '<img src="{}" width="30" height="30" style="border-radius:50%;" />',
                obj.profile_picture.url
            )
        return "—"

    thumbnail.short_description = 'Profile Picture'

admin.site.register(Account, AccountAdmin)
#admin.site.register(UserProfile,UserProfileAdmin)