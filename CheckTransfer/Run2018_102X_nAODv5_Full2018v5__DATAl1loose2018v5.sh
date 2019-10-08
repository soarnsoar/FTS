StartTime=$(date +%s)
#CheckFiles.sh keyword step production

step=DATAl1loose2018v5
production=Run2018_102X_nAODv5_Full2018v5

ARR_Keyword=()
ARR_Keyword=(
EGamma
SingleMuon
)

for keyword in ${ARR_Keyword[@]};do

    ./CheckFiles.sh ${keyword} $step $production

done
EndTime=$(date +%s)
echo $EndTime
echo "runtime : $(($EndTime - $StartTime)) sec"
echo -e "JOBDIR:${PWD}
args=$@
runtime=$(($EndTime - $StartTime))
ScriptName=$BASH_SOURCE" | /bin/mailx -s "FINISHED JOB @ $HOSTNAME" $USER@cern.ch
