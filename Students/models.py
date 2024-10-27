from django.db import models
from import_export import resources

class Student_List(models.Model):
    admission_number = models.IntegerField(default=0)
    student_name = models.CharField(max_length=100, default='')
    # GRADES = [('XII', 'XII'), ('XI', 'XI'), ('X', 'X'), ('IX', 'IX'), ('VIII', 'VIII'), ('VII', 'VII'), ('VI', 'VI'), ('V', 'V'), ('IV', 'IV'), ('III', 'III'), ('II', 'II'), ('I', 'I')]
    # grade = models.CharField(max_length=4, choices=GRADES, default=None)
    # DIVISION = [(chr(i), chr(i)) for i in range(ord('A'), ord('Z') + 1)]
    # division = models.CharField(max_length=1, choices=DIVISION, default=None)
    HOUSES = [("RED", "RED"),("YELLOW", "YELLOW"),("BLUE", "BLUE"),("GREEN", "GREEN")]
    house = models.CharField(max_length=10, choices=HOUSES, default=None)
    voted = models.BooleanField(default=False)
    class Meta:
    	verbose_name_plural = 'Student List'
    def __str__(self):
        return f"{self.student_name}" 

