# Senescence_nuclear_features
Repository for senescence nuclear feature classifiers and associated data
# Senescence_Data

MRC London Institute of Medical Sciences, London, UK. 2Institute of Clinical Sciences, Faculty of Medicine, Imperial College London, London, UK
MRC London Institute of Medical Sciences, Du Cane Rd, London W12 0NN

Senescence Group
Principal Investigator:     Prof. Jesus Gil
Authors:                     Imanol Duran, Joaquim Pombo, Bin Sun, Suchira Gallage, Hiromi Kudo, Domhnall McHugh, Laurą Bousset, Jose Efren Barragan Avila,
			  Roberta Forlano, Pinelopi Manousou, Mathias Heikenwalder, Domonic J. Withers, Santiago Vernia, Robert D. Goldin, Jesus Gil.

Repository for nuclear feature-based senescence prediction


1. System requirements 
Programming language: python 3.7.7 (3.7 or higher required).
For CellProfiler data extraction: v 4.2.1 
For InCarta data extraction (Cytiva): v 1.14 (1.14 or higher required).
For QuaPath data extraction: v 0.30 (0.30 or higher required).

The present code have been tested on macOS Ventura (13.6.1). There is no required non-standard hardware requirements. It only requires a standard computer with enough RAM to support the in-memory operations.

Python dependencies:
Numpy
Script
Scikit-learn
Pandas
Seaborg
Matplotlib
Graphviz


2. Installation guide
Python and required dependencies can be installed via https://www.python.org/downloads/. Cellprofiler data can be installed via https://cellprofiler.org/releases.  QuPath data extraction can be installed via https://qupath.github.io. InCarta is not open source software and requires third party purchase. Typical install time for the above packages may vary according to the user hardware.

For information on instructions of use, expected output, runtime and other instructions follow the inventory of the repository mentioned below.

This repository contains:

1. Open source nuclear extraction
	This open source nuclear extraction protocol corresponds to part of our open_source nuclear data extraction pipeline, carried out in Cellprofiler

2. Training Datasets
- Contains the training datasets of the treated and control (DMSO) groups. All data derive from .TIF files.The acquired images had the following characteristics: width and length of 663.005 μm (2040 pixels), at a 3.0769 pixels per μm resolution.The following parameters were extracted to assess nuclear morphology: Area (in micron2), form factor (object roundness), elongation (object short axis / object long axis), compactness (average radius of the object), chord ratio (object min. chord ratio / object max. chord length), gyration radius (average radius of the shape), displacement (distance between the nucleus centre of gravity and the cell centre of gravity, normalised by the gyration radius of the nucleus). 

Importantly, CT and RF training sets were randomised from the same datasets, which are linked in this repository.

3. Classification Tree
- Contains the classification tree training model for the development of all the CT classifiers, including:

AEM - A549 Etoposide Model
GM - General Model (constructed merging all datasets)
HEM - SK-HEP-1 Etoposide Model
IEM - IMR90 Etoposide Model
MEM - SK-MEL-103 Etoposide Model

VCA is a democratic majority vote based on the previous 8 algorithms.

3. Random Forest
- Contains the Random Forest training model for the development of all the RF classifiers, including:

AERFM - A549 Etoposide Random Forest Model
HERFM - SK-HEP-1 Etoposide Random Forest Model
MERFM - SK-MEL-103 Etoposide Random Forest Model

For both Classification Tree and Random Tree models, the output will consist on AP, AUC and test data on the input based on the developed classifiers, and it will yield a classification tree where specified. The expected run time for a normal desktop computer on a randomised sample of 10.000 cells per condition should not take more than a few minutes. Increasing the output data size will increase the output run time.

5. In Vivo Classifier

- Contains the in vivo classifier for QuPath processed files. The input requires .xlsx files containing the following columns containing nuclear data:
Centroid X
Centroid Y
Area
Perimeter
Circularity
Maxcaliper
Mincaliper
Eccentricity

It will yield two files:
- Data.txt (containing single cell values)
- Parameter.txt (containing different AUC thresolds)

6. Screening normalisation
It contains the R script for Score data normalisation carried out for the selective drug screening.



