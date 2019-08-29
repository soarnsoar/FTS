from Transfer import *

dic={
    'Production':'Run2018_102X_nAODv5_Full2018v5',
    'Step':'DATAl1loose2018v5',
    'Samples':['EGamma_Run2018B','EGamma_Run2018C','EGamma_Run2018D','SingleMuon'],

}



job=latinoTransfer()
job.Production=dic['Production']
job.Step=dic['Step']

for s in dic['Samples']:

    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
