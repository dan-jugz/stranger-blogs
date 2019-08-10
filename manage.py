from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

#create app instance
app = create_app('development')
manager=Manager(app)
migrate=Migrate(app,db)

#create manager instance
manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)


@manager.shell
def make_shell_context():
    return dict (app=app,db=db)

if __name__=='__main__':
    manager.run()