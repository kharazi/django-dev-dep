from django.contrib import admin
from users.models import Users
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # fields = ('first_name', 'last_name', 'username')
    list_display = ('first_name', 'last_name', 'username', 'password', 'number_of_friends', 'token')
    search_fields = ('first_name', 'last_name', 'username')

admin.site.register(Users, UserAdmin)