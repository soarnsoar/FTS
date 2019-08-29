

from Transfer import *

dic={
    'Production':'Run2016_102X_nAODv4_Full2016v5',
    'Step':'DATAl1loose2016v5',
    'Samples':['SingleElectron_Run2016G','SingleElectron_Run2016H','SingleMuon'],
}



job=latinoTransfer()
job.Production=dic['Production']
job.Step=dic['Step']

for s in dic['Samples']:

    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
