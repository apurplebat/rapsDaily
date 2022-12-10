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



class ContestAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name',
        'submitted'
    )
    # Make these fields read-only in the admin
    readonly_fields = (
        'first_name',
        'last_name',
        'email',
        'photo',
        'submitted'
    )

    search_fields = (
		'first_name',
		'last_name',
		'email',
		'submitted',
	)

    list_filter = (
		'first_name',
		'last_name',
		'email',
		'submitted',
	)

# Register your models here.
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Topic, TopicAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Contest, ContestAdmin)