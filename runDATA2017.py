from Transfer import *

dic={
    'Production':'Run2017_102X_nAODv4_Full2017v5',
    'Step':'DATAl1loose2017v5',
    'Samples':['SingleElectron_Run2017E','SingleElectron_Run2017F','SingleMuon'],

}



job=latinoTransfer()
job.Production=dic['Production']
job.Step=dic['Step']

for s in dic['Samples']:

    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
