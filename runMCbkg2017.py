from Transfer import *

dic={
    'Production':'Fall2017_102X_nAODv4_Full2017v5',
    'Step':'MCl1loose2017v5',
    'Samples':[
        'WW-LO',
        'WZ',
        'ZZ',
        'TTToSemiLeptonic',
        '_WpWmJJ_',
        '_WpWpJJ_',
        'ST_t',
        'TTW',
        'TTZ',
        'WJetsToLN',
        'DYJets',
        'QCD',

    ],
}



job=latinoTransfer()
job.Production=dic['Production']
job.Step=dic['Step']

for s in dic['Samples']:

    this_list=job.MakeList(Sample=s)
    job.Run(this_list)


from SendMail import *
SendMail(GetScriptName())
