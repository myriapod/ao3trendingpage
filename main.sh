timestamp=$(date '+%F %T')
# timestamp="2024-01-17 15:21:46" # fixed timestamp if needed to restart
python3 dataextraction.py $timestamp
echo "Done with data extraction"
python3 dataanalysis.py $timestamp
echo "Done with data analysis"
python3 datavizualisation.py $timestamp
echo "Done with data vizualisation"