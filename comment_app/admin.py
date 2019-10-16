from django.contrib import admin
from .models import Post,Category,Comment


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name' , 'slug')
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Category,CategoryAdmin)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','published','status')
	list_filter = ('status','created','published','author')
	list_display = ('title','content')
	prepopulated_fields = {'slug':('title',)}


admin.site.register(Post,PostAdmin)

#---------------------------------------------------------------------------comment wala part
class CommentAdmin(admin.ModelAdmin):
 	list_display = ('user','email','approved')
 	
admin.site.register(Comment,CommentAdmin)	