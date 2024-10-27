from django.db import models

class Status(models.Model):
	election_status_name = models.CharField(default='Election Campaign Status', max_length=100, editable=False)
	STATUS = [('ON', 'ON'), ('OFF', 'OFF')]
	status = models.CharField(choices=STATUS, max_length=3, default='OFF')
	class Meta:
		verbose_name_plural = 'Status (ON/OFF)'
	def __str__(self):
		return self.election_status_name

class Position(models.Model):
	position = models.CharField(max_length=100, default='')
	def __str__(self):
		return self.position

class Candidate(models.Model):
    student_name = models.CharField(max_length=100, default='')
    HOUSES = [("RED", "RED"),("YELLOW", "YELLOW"),("BLUE", "BLUE"),("GREEN", "GREEN")]
    house = models.CharField(max_length=10, choices=HOUSES, default=None)
    position = models.ForeignKey(Position, default=None, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.student_name}" 

