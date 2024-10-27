from django.shortcuts import render, redirect
from django.db.models import F
from Students.models import Student_List 
from Campaign.models import Candidate, Position, Status

def election_page(request, student_code):
	student_details = Student_List.objects.get(admission_number=student_code)
	candidates = Candidate.objects.all()
	positions = Position.objects.all()
	candidate_details = {}
	print(request.method)
	if request.method == 'POST':
		positions = Position.objects.all()
		for each_position in positions:
			if each_position.position.strip().lower() in ['house captain', 'house vice captain']:
				each_position = f'{each_position.position.upper()} ({student_details.house})'
			selected_candidate = request.POST.get(f'options-outlined-{each_position}')
			add_vote = Candidate.objects.get(student_name=selected_candidate)
			add_vote.votes = F('votes') + 1
			add_vote.save()
		student_details.voted = True
		student_details.save()
		return render(request,'thankyou.html', {'student_details' : student_details})
	else:
		for each_position in positions:
			if each_position.position.strip().lower() in ['house captain', 'house vice captain']:
				each_position.position = f'{each_position.position.upper()} ({student_details.house})'
			candidate_details[each_position.position.upper()] = []
		for candidate in candidates:
			if candidate.position.position.strip().lower() in ['house captain', 'house vice captain']:
				if candidate.house == student_details.house:
					candidate_details[candidate.position.position.upper() + f" ({candidate.house})"].append(candidate)
			else:
				candidate_details[candidate.position.position.upper()].append(candidate)
	if student_details.house == 'RED':
		button_color = 'danger'
	elif student_details.house == 'YELLOW':
		button_color = 'warning'
	elif student_details.house == 'GREEN':
		button_color = 'success'
	else:
		button_color = 'primary'

	return render(request, 'election.html', {'candidate_details' : candidate_details, 'student_details' : student_details, 'button_color' : button_color})

def admission_number(request):
	status_in_model = Status.objects.get(election_status_name='Election Campaign Status')
	if status_in_model.status == 'ON':
		if request.method == 'POST':
			student_code = request.POST.get('student-code')
			student_code = student_code.strip()
			if len(Student_List.objects.filter(admission_number=student_code)) != 0:
				if Student_List.objects.get(admission_number=student_code).voted == True:
					return render(request, 'admission-code.html', {'message' : f'{student_code} has already voted!'})
				else:
					return redirect('voting-page', student_code=int(student_code))
			else:
				return render(request, 'admission-code.html', {'message' : f'{student_code} does not exist. Please double check and try again!'})
		return render(request, 'admission-code.html')
	else:
		return render(request, '404.html')

