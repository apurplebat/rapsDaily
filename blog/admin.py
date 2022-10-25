from django.contrib import admin
from . import models



class CommentInline(admin.StackedInline):
    model = models.Comment
    extra = 0
    readonly_fields = (
    	'name',
    	'text',
    	'email',
	)

class PostAdmin(admin.ModelAdmin):
	list_display = (
		'title',
		'author',
		'status',
		'created',
		'updated',
	)

	search_fields = (
		'title',
		'author__username',
		'author__first_name',
		'author__last_name',
	)


	inlines = [
		CommentInline,
	]

	list_filter = (
		'status',
		'topics',
	)

	prepopulated_fields = {'slug': ('title',)}


class TopicAdmin(admin.ModelAdmin):
	list_display = (
		'name',
		'slug',
	)

	prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = (
    	'name',
    	'email',
    	'text',
    	'approved',
    	'created',
    	'updated',

    )

    search_fields = (
		'name',
		'text',
		'email',
	)

    list_filter = (
    	'approved',
    )

    moderate = ['moderate_comments']

    def moderate_comments(self, request, queryset):
        queryset.update(approved=True)



# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment, CommentAdmin)