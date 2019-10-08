


import sys

INPUT_FILE=sys.argv[1]
sys.path.append("../")


from Transfer import *

f=open(INPUT_FILE)


#Summer16_102X_nAODv4_Full2016v5__MCl1loose2016v5__WJetsToLN__S.log
job=latinoTransfer()
job.Production=INPUT_FILE.split('__')[0]
job.Step=INPUT_FILE.split('__')[1]

lines=f.readlines()



for s in lines:
    if len(s)==0: continue
    if s=="": continue
    s=s.split('/')[-1]
    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
