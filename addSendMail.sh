scripts=($(ls run*.py))



for s in ${scripts[@]};do

    echo 'from SendMail import *' >> $s
    echo 'SendMail(GetScriptName())' >> $s

done
