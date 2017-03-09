DATA_SRC="http://www.repository.voxforge1.org/downloads/SpeechCorpus/Trunk/Audio/Main/16kHz_16bit"
DATA_ROOT="/home/ubuntu/voxforge"
DATA_TGZ=${DATA_ROOT}/tgz
DATA_EXTRACT=${DATA_ROOT}/audio
mkdir ${DATA_EXTRACT}

wget -P ${DATA_TGZ} -l 1 -N -nd -c -e robots=off -A tgz -r -np ${DATA_SRC}

for a in ${DATA_TGZ}/*.tgz; do
  tar -C ${DATA_EXTRACT} -xf $a
done
