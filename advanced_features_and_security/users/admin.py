from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, UserProfile

class UserProfileInline(admin.StackedInline):
    """Inline admin for UserProfile to show within CustomUser admin"""
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('role',)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Custom admin for CustomUser model"""
    
    # Include the UserProfile inline
    inlines = (UserProfileInline,)
    
    # Add our custom fields to the existing UserAdmin fieldsets
    fieldsets = UserAdmin.fieldsets + (
        (_('Additional Information'), {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Add custom fields to the add user form
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_('Additional Information'), {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Include custom fields in list display
    list_display = UserAdmin.list_display + ('date_of_birth', 'get_user_role')
    
    # Add filters for better user management
    list_filter = UserAdmin.list_filter + ('date_of_birth', 'userprofile__role')
    
    # Add search functionality
    search_fields = UserAdmin.search_fields + ('userprofile__role',)
    
    def get_user_role(self, obj):
        """Display user role in the list view"""
        try:
            return obj.userprofile.role
        except UserProfile.DoesNotExist:
            return 'No Profile'
    get_user_role.short_description = 'Role'
    get_user_role.admin_order_field = 'userprofile__role'

# Optional: Register UserProfile separately if you want to manage it independently
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """Admin for UserProfile model"""
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    raw_id_fields = ('user',)