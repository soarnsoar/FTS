import ROOT
import glob

MC2018v5={
'Production':'Autumn18_102X_nAODv5_Full2018v5',
'Step':'MCl1loose2018v5'
}

DATA2018v5={
'Production':'Run2018_102X_nAODv5_Full2018v5',
'Step':'DATAl1loose2018v5'
}

MC2017v4v5={
'Production':'Fall2017_102X_nAODv4_Full2017v5',
'Step':'MCl1loose2017v5'
}

DATA2017v4v5={
'Production':'Run2017_102X_nAODv4_Full2017v5',
'Step':'DATAl1loose2017v5'
}

MC2016v4v5={
'Production':'Summer16_102X_nAODv4_Full2016v5',
'Step':'MCl1loose2016v5'
}

DATA2016v4v5={
'Production':'Run2016_102X_nAODv4_Full2016v5',
'Step':'DATAl1loose2016v5'
}







##---Main---##
CheckList=[
MC2018v5,
DATA2018v5,
MC2017v4v5,
DATA2017v4v5,
MC2016v4v5,
DATA2016v4v5
]

BASEDIR='/xrootd/store/user/jhchoi/Latino/HWWNano/'

for dic in CheckList:
    SAMPLEDIR=BASEDIR+'/'+dic['Production']+'/'+dic['Step']
    filelist=glob.glob(SAMPLEDIR+'/*.root')

    print "=====",SAMPLEDIR,"====="
    

    for f in filelist:
        if not ROOT.TFile.Open(f):
            print '[FAIL]',f
        
