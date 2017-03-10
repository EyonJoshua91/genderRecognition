""" Command-line usage:
      python GenderDetect.py [options] wave_file model_file
      where options may include:
      -m Model --determine which model you want to use, including GMM,MLP,KNN,DBN(currently, only GMM is available)
      -l window length --the length of the analysis window in seconds. Default is 0.025s (25 milliseconds)
      -s window step  -- the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
	You can also import this file as a module and use the functions directly.
"""

import pickle
import sys
import sklearn.mixture
import getopt
import os 
import scipy.io.wavfile as  wav
import numpy as np
from base import GenderPredict,mfcc_d_dd

def getopt2(name, opts, default = None) :
    value = [v for n,v in opts if n==name]
    if len(value) == 0 :
        return default
    return value[0]

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "r:s:e:", ["model="])
        # get the three mandatory arguments
        if len(args) != 2 :
            raise ValueError("Specify wavefile modelfile!")
        wavfile,modelfile= args
        if not os.path.exists(wavfile):
            raise ValueError("wavefile doesn't exist!")
        if not os.path.exists(modelfile):
            raise ValueError("modelfile doesn't exist!")        
        mode = getopt2("-m", opts, 'GMM')
        winlen=getopt2("-l", opts, 0.025)
        winstep=getopt2("-s", opts, 0.01)
    except :
        print __doc__
        (type, value, traceback) = sys.exc_info()
        print value
        sys.exit(0)
    if mode=='GMM':
        (rate,sig) = wav.read(wavfile)
        feats=mfcc_d_dd(sig,rate,winlen=winlen,winstep=winstep,numcep=13)
        f=open(modelfile,'rb')
        male_model,female_model=pickle.load(f)
        f.close()
        print('Done')
        gender=GenderPredict(feats,male_model,female_model,mode='score')
        if gender==1:
            print('Gender is Male')
        else:
            print('Gender is Female')
    else:
        print('Other models are not available now')