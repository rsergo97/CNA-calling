#!/bin/bash 

if [ "$#" -eq 0 ] || [ $1 = "-h" ]; then \
  echo "Usage: bash algorithm.sh normal.bam tumor.bam sample_ID hg19/hg38 outdir workdir"; exit
fi


# Arguments 
normal_bam=$1
tumor_bam=$2
sample_name=$3
hg=$4
outdir=$5
workdir=$6

echo "Start ..."

cd ${outdir}

samtools mpileup ${normal_bam} -o normal.mpileup

samtools mpileup ${tumor_bam} -o tumor.mpileup 

varscan somatic normal.mpileup tumor.mpileup ${sample_name}.varscan

echo "Pileup has beed calculated"

python ${workdir}/scripts/process_pileup.py -i ${sample_name}.varscan.snp -o ${sample_name}.to_call.txt 

echo "CNA calling"
# CNA calling by Facets script

Rscript ${workdir}/scripts/facets_call.R ${sample_name}.to_call.txt ${hg} ${outdir}

echo "Done! Segments and CNA plot are ready."


