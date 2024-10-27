from django.contrib import admin
from .models import Position, Candidate, Status
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

admin.site.register(Position)

@admin.action(description="Reset candidate votes to 0")
def reset_votes(modeladmin, request, queryset):
    queryset.update(votes=0)

@admin.action(description="Send Email Report")
def send_report(modeladmin, request, queryset):
	subject = 'Election Candidate Report'
	body = ''
	candidate_json_data = {}
	users = User.objects.all()
	destination_emails = []
	for obj in queryset:
		candidate_json_data[obj.position.position] = []
	for obj2 in queryset:
		candidate_json_data[obj2.position.position].append({'student_name' : obj2.student_name, 'votes' : obj2.votes, 'house' : obj2.house})
	print(candidate_json_data)
	for user in users:
		destination_emails.append(user.email)
	for candidate_detail in candidate_json_data.items():
		body += f'\n\n\n|{candidate_detail[0]}|\n\n'
		for candidate_detail_st2 in candidate_detail[1]:
			body += f"NAME : {candidate_detail_st2['student_name']}  |  VOTES : {candidate_detail_st2['votes']}  |  HOUSE : {candidate_detail_st2['house']}\n\n "
		body += '_______________________________________'

	send_mail(subject, body, settings.EMAIL_HOST_USER, destination_emails)

class CandidateAdmin(admin.ModelAdmin):
	search_fields = ['student_name','house']
	list_display = ['student_name','house', 'position']
	list_filter = ['house', 'position']
	actions = [reset_votes,send_report]

admin.site.register(Candidate, CandidateAdmin)

class StatusAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Status.objects.exists():
            return False
        return super().has_add_permission(request)

admin.site.register(Status, StatusAdmin)
