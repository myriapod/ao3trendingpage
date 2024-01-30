#!/bin/bash

export AO3TIMESTAMP=$(date '+%F %T')
python3 `pwd`/packages/dataextraction.py $AO3TIMESTAMP
echo $AO3TIMESTAMP - Done with data extraction
python3 `pwd`/packages/dataanalysis.py $AO3TIMESTAMP
echo $AO3TIMESTAMP - Done with data analysis
python3 `pwd`/packages/datavizualisation.py $AO3TIMESTAMP
echo $AO3TIMESTAMP - Done with data vizualisation

sudo systemctl daemon-reload
sudo systemctl restart ao3trendingpage
sudo systemctl restart nginx