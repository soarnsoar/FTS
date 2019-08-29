


import os

def SendMail(contents):
    HOSTNAME=os.getenv("HOSTNAME")
    USER=os.getenv("USER")
    os.system('echo -e "'+contents+'" | /bin/mailx -s "FINISHED JOB @'+HOSTNAME+'" '+USER+'@cern.ch')
