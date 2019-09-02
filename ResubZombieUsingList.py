

from Transfer import *
import sys

INPUT_FILE=sys.argv[1]



f=open(INPUT_FILE)



job=latinoTransfer()
job.Production=INPUT_FILE.split('__')[1]
job.Step=INPUT_FILE.split('__')[2]

lines=f.readlines()



for s in lines:
    s=s.split('/')[-1]
    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
