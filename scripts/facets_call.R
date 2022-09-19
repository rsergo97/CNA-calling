#!/usr/bin/Rscript

library(facets)

args = commandArgs(trailingOnly=TRUE)

pileup_file=args[1]
hg=args[2]
outdir=args[3]

sample_matrix <- readSnpMatrix(pileup_file)
pre_sample <- preProcSample(sample_matrix, gbuild = hg)
pre_sample$jointseg <- na.omit(pre_sample$jointseg)
sample <- procSample(pre_sample,cval=150)
facets_res <- emcncf(sample)

png(paste0(outdir, "cna.png"))
plotSample(x=sample, emfit=facets_res)
dev.off()

write.table(facets_res$cncf, paste0(outdir, "segments.txt"), row.names = F, quote = F, sep = "\t")

write.table(facets_result$ploidy, paste0(outdir, 'ploidy.txt', row.names = F, quote = F))

