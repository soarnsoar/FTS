LIST=($(ls Zombie__*.log))


for log in ${LIST[@]};do
    python ResubZombieUsingList.py $log
done
