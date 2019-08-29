from Transfer import *

dic={
    'Production':'Summer16_102X_nAODv4_Full2016v5',
    'Step':'MCl1loose2016v5',
    'Samples':['GluGluHToWWToLNuQQ','VBFHToWWToLNuQQ'],
}



job=latinoTransfer()
job.Production=dic['Production']
job.Step=dic['Step']

for s in dic['Samples']:

    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
