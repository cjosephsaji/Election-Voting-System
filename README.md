# Election-Voting-System
`This program is created to simplify election voting in schools`


## Installing Required Packages
```
pip3 install django django-import-export
```

## Create Database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

## Upload Student List to Database
Ensure to label the first row as follows:

```
admission_number
student_name
house
```

![image](https://github.com/user-attachments/assets/69ca792f-ca64-4e8e-bed7-dfbd0a23c1bd)

Head to the `Students_List` model and click on `Import`


## Turn Voting System ON/OFF
Navigate to the `Status (ON/OFF)` model and change the option to `ON` to activate the voting system and vice versa
