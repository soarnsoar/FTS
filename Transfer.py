#From
import os
import glob


import inspect

def GetScriptName():
    return inspect.getfile(inspect.currentframe())

class latinoTransfer:

    def __init__(self):
        self.BASEDIR_From='/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
        self.BASEDIR_To='/xrootd/store/user/jhchoi/Latino/HWWNano/'
        
        self.ADDRESS_From='gsiftp://eoscmsftp.cern.ch/'
        self.ADDRESS_To='gsiftp://cms-se.sdfarm.kr/'

        self.Production=''
        self.Step=''
        

    def Run(self,mylist):
        for this_sample in mylist:

            os.system('gfal-copy -K ADLER32 '+self.ADDRESS_From+'/'+this_sample+' '+self.ADDRESS_To+'/'+self.BASEDIR_To+'/'+self.Production+'/'+self.Step+'/')

    def MakeList(self,Sample):

        print'"===Make List of ',Sample,'==='

        #PRODUCTION=Run2018_102X_nAODv5_Full2018v5
        #STEP=DATAl1loose2018v5
        BASEDIR=self.BASEDIR_From
        #'/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'
        
        Production=self.Production
        Step=self.Step

        thispath=BASEDIR+'/'+Production+'/'+Step+'/*'+Sample+'*.root'
        print thispath
        mylist=glob.glob(thispath)
        print "--TRANSFER LIST--"
        print thispath
        print "--TRANSFER LIST[END]--"

        return mylist







DATA2016nAODv4_v5={
    'Production':'Run2016_102X_nAODv4_Full2016v5',
    'Step':'DATAl1loose2016v5',
    'Samples':['SingleElectron_Run2016G','SingleElectron_Run2016H','SingleMuon'],
}



job=latinoTransfer()
job.Production='Run2018_102X_nAODv5_Full2018v5'
job.Step='DATAl1loose2018v5'
this_list=job.MakeList(Sample='nanoLatino_SingleMuon_Run2018D-Nano1June2019_ver2-v1__part9')
job.Run(this_list)



