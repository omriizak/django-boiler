import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hello_django.settings')

import django
# Import settings
django.setup()

from main_app.models import Employed, NotEmployed


def populate(current_employees):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in current_employees:

        # Create new User Entry
        employee = Employed.objects.get_or_create(first_name=entry.split(',')[0],
                                          last_name=entry.split(',')[1],
                                          position=entry.split(',')[2],
                                          image=entry.split(',')[3].lower().strip() + '.jpeg')[0]

    non_employee = NotEmployed.objects.get_or_create(
        first_name="Omri Izak",
        last_name="Jacobsz",
        position="Data Engineer | Web Engineer | Cloud Engineer",
        image="omri.png"
    )


if __name__ == '__main__':
    
    print("Read CSV")
    with open('employees.csv') as f:
        current_employees = f.readlines()
    print("Populating the databases...Please Wait")
    populate(current_employees)
    print('Populating Complete')
