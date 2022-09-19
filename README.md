# CNA-calling


This is beta version of CNA caller. It temporary uses the facets algorithm for CNA detection. My personal calling algorithm is in development stage. It will be ready soon and will replace current method.

This tool is created for easy copynumber alterations calling and visualization based on tumor/normal samples ratio. 

Installation 
=====================
To create the enviroment with all dependencies run:
```
$ conda env create -f config.yml
$ conda activate CiaNAs
```
Calling
=====================
Then run by typing:
```
$ bash algorithm.sh --normal NORMAL_BAM --tumor $TUMOR_BAM --sample_id $NAME --hg hg38/hg19 --outdir $OUTDIR --workdir $WORKDIR
```


## Literature Resources

Shen R, Seshan VE. FACETS: allele-specific copy number and clonal heterogeneity analysis tool for high-throughput DNA sequencing. Nucleic Acids Res. 2016 Sep 19;44(16):e131. doi: 10.1093/nar/gkw520. Epub 2016 Jun 7. PMID: 27270079; PMCID: PMC5027494.

Koboldt DC, Chen K, Wylie T, Larson DE, McLellan MD, Mardis ER, Weinstock GM, Wilson RK, Ding L. VarScan: variant detection in massively parallel sequencing of individual and pooled samples. Bioinformatics. 2009 Sep 1;25(17):2283-5. doi: 10.1093/bioinformatics/btp373. Epub 2009 Jun 19. PMID: 19542151; PMCID: PMC2734323.

