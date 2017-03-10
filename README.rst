======================
Gender Detection
======================

This project is to test performance of different classification method on Gender Detection problem


Test tool usage
============
python GenderDetect.py [options] wave_file model_file
      where options may include:
      -m Model --determine which model you want to use, including GMM,MLP,KNN,DBN(currently, only GMM is available)
      -l window length --the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
      -s window step  -- the step between successive windows in seconds. Default is 0.01s (10 milliseconds)


Training document
============

Explanation for the process of training.

===================== =============================================
     Document         Description  
===================== =============================================
voxforgeDownload.sh   Download voxforge corpus from website
--------------------  ---------------------------------------------
Corpus_prep.ipynb    Pick and formalize the audios for further training
--------------------  ---------------------------------------------
MFCC_extract.ipynb   Extract AMFCC features from prepared corpus
--------------------  ---------------------------------------------
GMM_classify.ipynb   Train GMM models for gender detection
===================== =============================================

=============	===========
Document 		Description
=============	===========
signal			the audio signal from which to compute features. Should be an N*1 array
samplerate 		the samplerate of the signal we are working with.
winlen 			the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
winstep 		the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
numcep			the number of cepstrum to return, default 13
nfilt			the number of filters in the filterbank, default 26.
nfft			the FFT size. Default is 512
lowfreq			lowest band edge of mel filters. In Hz, default is 0
highfreq		highest band edge of mel filters. In Hz, default is samplerate/2
preemph			apply preemphasis filter with preemph as coefficient. 0 is no filter. Default is 0.97
ceplifter		apply a lifter to final cepstral coefficients. 0 is no lifter. Default is 22
appendEnergy	if this is true, the zeroth cepstral coefficient is replaced with the log of the total frame energy.
returns			A numpy array of size (NUMFRAMES by numcep) containing features. Each row holds 1 feature vector.
=============	===========