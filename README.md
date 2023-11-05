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

Programming language: python 3.7.7
This repository contains:

1. Open source nuclear extraction
	This open source nuclear extraction protocol corresponds to part of our open_source nuclear data extraction pipeline, carried out in Cellprofiler

2. Training Datasts
- Contains the training datasets of the treated and control (DMSO) groups. All data derive from .TIF files.The acquired images had the following characteristics: width and length of 663.005 μm (2040 pixels), at a 3.0769 pixels per μm resolution.The following parameters were extracted to assess nuclear morphology: Area (in micron2), form factor (object roundness), elongation (object short axis / object long axis), compactness (average radius of the object), chord ratio (object min. chord ratio / object max. chord length), gyration radius (average radius of the shape), displacement (distance between the nucleus centre of gravity and the cell centre of gravity, normalised by the gyration radius of the nucleus). 

Importantly, CT and RF training sets were randomized from the same datasets, which are linked in this repository (redirected to Google Drive).

3. Classificaton Tree
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
HERFM - SK-HEP-1 Etposide Random Forest Model
MERFM - SK-MEL-103 Etoposide Random Forest Model


5. In Vivo Classifier

- Contains the in vivo classifier for QuPath processed files. The input requires Xlsx files containing the following columns containing nuclear data:
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
