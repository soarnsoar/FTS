StartTime=$(date +%s)
#CheckFiles.sh keyword step production

step=MCl1loose2017v5
production=Fall2017_102X_nAODv4_Full2017v5

ARR_Keyword=()
ARR_Keyword=(
WW-LO
WZ
ZZ
TTToSemiLeptonic
_WpWmJJ_
_WpWpJJ_
ST_t
TTW
TTZ
WJetsToLN
DYJets
QCD
GluGluHToWWToLNuQQ
VBFHToWWToLNuQQ
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
