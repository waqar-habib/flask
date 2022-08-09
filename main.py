#import function from auth_app folder
from auth_app import create_app

app = create_app()

#if this file is run, execute this line and run webserver
if __name__=='__main__':
    #anytime a change is made, rerun the app automatically
    app.run(debug=True)
