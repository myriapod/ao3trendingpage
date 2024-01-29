export AO3TIMESTAMP=$(date '+%F %T')
python3 packages/dataextraction.py $AO3TIMESTAMP
echo "Done with data extraction"
python3 packages/dataanalysis.py $AO3TIMESTAMP
echo "Done with data analysis"
python3 packages/datavizualisation.py $AO3TIMESTAMP
echo "Done with data vizualisation"