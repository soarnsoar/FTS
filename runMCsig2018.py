from Transfer import *

dic={
    'Production':'Autumn18_102X_nAODv5_Full2018v5',
    'Step':'MCl1loose2018v5',
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
