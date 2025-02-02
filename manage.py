#from flask_script import Manager, prompt_bool, Shell, Server
from termcolor import colored

from app import app, db, models


#manager = Manager(app)


def make_shell_context():
    return dict(app=app)



def initdb():
    ''' Create the SQL database. '''
    db.create_all()
    print(colored('The SQL database has been created', 'green'))



def dropdb():
    ''' Delete the SQL database. '''
    if prompt_bool('Are you sure you want to lose all your SQL data?'):
        db.drop_all()
        print(colored('The SQL database has been deleted', 'green'))

#manager.add_command('runserver', Server())
#manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    #manager.run()
    pass
