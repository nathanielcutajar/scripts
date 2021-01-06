echo 'Getting everything up to date'

badCount=0
projectCount=0
manual_projects[badCount]="leave_empty"
badCount=$((badCount+1))

for project in */
do
	echo ''
	projectCount=$((projectCount+1))
	cd "$project"
	echo "$project"
	git fetch
	git checkout build | grep awudgawu
	if (! git pull); then
		manual_projects[$badCount]=$project
		badCount=$((badCount+1))
	fi
	cd ../
done

echo $badCount
if [ "$badCount" -gt 1 ]
then
	echo "$badCount out of $projectCount had an error"
	echo 'These projects were not pulled and require manual attention:'

	for project in $manual_projects;
	do
		echo "$project"
	done
else
	echo 'Everything is now up to date'
fi