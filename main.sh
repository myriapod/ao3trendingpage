#export AO3TIMESTAMP=$(date '+%F %T')
# timestamp="2024-01-17 15:21:46" # fixed timestamp if needed to restart
#python3 dataextraction.py $AO3TIMESTAMP
#echo "Done with data extraction"
#python3 dataanalysis.py $AO3TIMESTAMP
#echo "Done with data analysis"
python3 datavizualisation.py $AO3TIMESTAMP
echo "Done with data vizualisation"