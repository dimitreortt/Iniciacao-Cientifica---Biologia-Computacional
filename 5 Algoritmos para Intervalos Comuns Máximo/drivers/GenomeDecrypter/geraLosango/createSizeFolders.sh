mkdir tamanho$1
cp findAllMatchings.py runFindAllMatchings.sh collectGeneMatchings.py geraCodigoModeOne.py runGenGenomes.sh generateGenomes.py tamanho$1
python tamanho$1/geraCodigoModeOne.py $1
./tamanho$1/runGenGenomes.sh $1