StartTime=$(date +%s)
#CheckFiles.sh keyword step production

step=DATAl1loose2016v5
production=Run2016_102X_nAODv4_Full2016v5

ARR_Keyword=()
ARR_Keyword=(
SingleElectron
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
