#!/bin/bash

function Check1FileSize(){

    ##lxplus file
    FilePathFrom=$1
    #AddressFrom=gsiftp://eoscmsftp.cern.ch/
    #BasedirFrom=/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/

    ##Kisti File
    FilePathTo=$2
    #AddressTo=gsiftp://cms-se.sdfarm.kr/
    #BasedirTo=/xrootd/store/user/jhchoi/Latino/HWWNano/


    #echo "--Check FileSizeFrom--"
    FileSizeFrom=`gfal-ls -lH "${FilePathFrom}"|awk '{print $5}'`
    #echo "--Check FileSizeTo--"
    FileSizeTo=`gfal-ls -lH "${FilePathTo}"|awk '{print $5}'`

    #echo "FileSizeFrom=${FileSizeFrom}"
    #echo "FileSizeTo=${FileSizeTo}"
    if [ "$FileSizeFrom" != "$FileSizeTo" ]
    then
	echo False
    fi

}

##Test
#Check1FileSize gsiftp://eoscmsftp.cern.ch//eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5/nanoLatino_WpWmJJ_EWK_QCD_noHiggs__part5.root gsiftp://cms-se.sdfarm.kr//xrootd/store/user/jhchoi/Latino/HWWNano/Autumn18_102X_nAODv5_Full2018v5/MCl1loose2018v5/nanoLatino_WpWmJJ_EWK_QCD_noHiggs__part5.root





AddressFrom=gsiftp://eoscmsftp.cern.ch/                                                                                   
BasedirFrom=/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/                                                      

AddressTo=gsiftp://cms-se.sdfarm.kr/                                                                                      
BasedirTo=/xrootd/store/user/jhchoi/Latino/HWWNano/                                                                       




##--Make List--##
#keyword='QCD'
#step=MCl1loose2018v5
#production=Autumn18_102X_nAODv5_Full2018v5

keyword=$1
step=$2
production=$3

logfile_s=${production}__${step}__${keyword}__S.log
logfile_f=${production}__${step}__${keyword}__F.log


##--if running @ lxplus

#SearchPath="${BasedirFrom}"/"${production}"/"${step}"/"*${keyword}*.root"
#slist=($(ls ${SearchPath}))
pushd "${BasedirFrom}"/"${production}"/"${step}"/
slist=($(ls *${keyword}*.root))
popd


##--Check each file
echo "" > $logfile_s
echo "" > $logfile_f
for s in ${slist[@]};do

    echo "SAMPLENAME=""$s"
    FullPathFrom=${AddressFrom}/${BasedirFrom}/${production}/${step}/${s}
    echo $FullPathFrom
    FullPathTo=${AddressTo}/${BasedirTo}/${production}/${step}/${s}
    echo $FullPathTo
    Result=`Check1FileSize $FullPathFrom $FullPathTo`
    #echo $Result
    if [ -z $Result ]
    then
	echo ${s} >> $logfile_s
    else
	echo ${s} >> $logfile_f
    fi
done


