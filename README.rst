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

====================  =============================================
Document.             Description  
====================  ==============================================
voxforgeDownload.sh   Download voxforge corpus from website
--------------------  ---------------------------------------------
Corpus_prep.ipynb     Pick and formalize the audios for further training
--------------------  ---------------------------------------------
MFCC_extract.ipynb    Extract AMFCC features from prepared corpus
--------------------  ---------------------------------------------
GMM_classify.ipynb    Train GMM models for gender detection
===================== =============================================


+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | Cells may span columns.          |
+------------------------+------------+---------------------+
| body row 3             | Cells may  | - Table cells       |
+------------------------+ span rows. | - contain           |
| body row 4             |            | - body elements.    |
+------------------------+------------+---------------------+