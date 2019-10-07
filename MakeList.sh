#From

#PRODUCTION=Run2016_102X_nAODv4_Full2016v5
#STEP=DATAl1loose2016v5

#SAMPLES=(
#SingleElectron_Run2016E
#SingleElectron_Run2016F
#SingleElectron_Run2016G
#SingleElectron_Run2016H
#SingleMuon
#)

#InputList=()
#for s in ${SAMPLES[@]};do
#    thislist=($(ls /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/${PRODUCTION}/${STEP}/*${s}*.root))
#    for this_sample in ${thislist[@]};do
	
#	InputList+=($this_sample)
#    done
#done

#for a in ${InputList[@]};do
#    echo "======"
#    echo $a
#done

function MakeList(){
PRODUCTION=$1
STEP=$2

s=$3

thislist=($(ls /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/${PRODUCTION}/${STEP}/*${s}*.root))




}
