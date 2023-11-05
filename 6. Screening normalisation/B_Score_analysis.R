library(cellHTS2)
BiocManager::install("cellHTS2")
setwd("/directory")
getwd()

# Define the path to your experiment directory
experimentName <- "Experiment_name"

dataPath <- system.file(experimentName, package="cellHTS2")
rev(dir(dataPath))


platelistx <- readPlateList("Platename.txt", name=experimentName, path=dataPath)

platelistx

templateDescriptionFile(filename="Description.txt", dataPath, force=FALSE)

x <- configure(x,
               descripFile="Description.txt",
               confFile="Plateconf.txt", "Screenlog.txt",
               path=dataPath)

configurationAsScreenPlot(x)

xn <- normalizePlates(x,
                        scale="additive",
                        log=FALSE,
                        method="Bscore",
                        varianceAdjust="byPlate")
 compare2cellHTS(x, xn)
 
 xsc <- scoreReplicates(xn, sign="-", method="zscore")
 xsc <- summarizeReplicates(xsc, summary="mean")
 scores <- Data(xsc)
 ylim <- quantile(scores, c(0.001, 0.999), na.rm=TRUE)
 boxplot(scores ~ wellAnno(x), col="lightblue", outline=FALSE,
         ylim=ylim)
xsc <- annotate(xsc, geneIDFile="GeneID.txt",
 path=dataPath)
xsc
save(xsc, file=paste(experimentName, ".rda", sep=""))

setSettings(list(plateList=list(reproducibility=list(include=TRUE, map=TRUE),
 intensities=list(include=TRUE, map=TRUE)),
 screenSummary=list(scores=list(range=c(-4, 8), map=TRUE))))
 out <- writeReport(raw=x, normalized=xn, scored=xsc,
 force=T,outdir=dataPath)
 if (interactive()) browseURL(out)
writeTab(xsc, file="Scores.txt")
