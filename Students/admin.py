from django.contrib import admin
from .models import Student_List
from import_export.admin import ImportExportModelAdmin
from import_export import resources


@admin.action(description="Unvote students")
def unvote_students(modeladmin, request, queryset):
    queryset.update(voted=0)

@admin.action(description="Delete selected students")
def delete_selected_students(modeladmin, request, queryset):
    queryset.delete()


class StudentListResource(resources.ModelResource):
    class Meta:
        model = Student_List
        fields = ('admission_number', 'student_name', 'house')
        import_id_fields = ['admission_number']
        skip_unchanged = True
        report_skipped = True

class Student_ListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	resource_class = StudentListResource
	search_fields = ['student_name','house', 'admission_number']
	list_display = ['student_name','house', 'admission_number']
	list_filter = ['house', 'voted']
	actions = [unvote_students, delete_selected_students]
	def get_actions(self, request):
		actions = super().get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

admin.site.register(Student_List, Student_ListAdmin)


