"""Admin settings"""
from django.contrib import admin

from social_auth.utils import setting
from social_auth.models import Nonce, Association


if setting('SOCIAL_AUTH_CREATE_MODEL', True):
    from social_auth.models import UserSocialAuth
    
    class UserSocialAuthOption(admin.ModelAdmin):
        """Social Auth user options"""
        list_display = ('id', 'user', 'provider', 'uid')
        search_fields = ('user__first_name', 'user__last_name', 'user__email')
        list_filter = ('provider',)
        raw_id_fields = ('user',)
        list_select_related = True

    admin.site.register(UserSocialAuth, UserSocialAuthOption)

class NonceOption(admin.ModelAdmin):
    """Nonce options"""
    list_display = ('id', 'server_url', 'timestamp', 'salt')
    search_fields = ('server_url',)


class AssociationOption(admin.ModelAdmin):
    """Association options"""
    list_display = ('id', 'server_url', 'assoc_type')
    list_filter = ('assoc_type',)
    search_fields = ('server_url',)


admin.site.register(Nonce, NonceOption)
admin.site.register(Association, AssociationOption)
