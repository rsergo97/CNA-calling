#!/usr/bin/env python
# coding: utf-8


from __future__ import print_function
import sys
import pandas as pd
import argparse
import warnings

def get_zygousity(ref_c, alt_c):
    if ref_c / (ref_c + alt_c + 1) * 100 in range(25, 75+1):
        return "heterozygous"
    else:
        return "homozygous"
    
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Create pileup file for CNA calling')
    parser.add_argument('-i', '--input_pileup', type=str, help='Path to varscan file', required=True)
    parser.add_argument('-o', '--output_pileup', type=str, help='Path to output file for CNA calling', required=True)
    

    args = parser.parse_args()

    input_pileup, output_pileup = args.input_pileup, args.output_pileup
    


    snp = pd.read_csv(input_pileup, sep="\t")

    snp = snp[['chrom', 'position', 'ref', 'var', 'normal_reads1', 'normal_reads2', 
               'tumor_reads1', 'tumor_reads2']].rename(columns={"chrom":"Chromosome", "position":"Position",
                                                               "ref":"Ref", "var":"Alt", "normal_reads1":"File1R", 
                                                               "normal_reads2":"File1A", "tumor_reads1":"File2R",
                                                               "tumor_reads2":"File2A"})

    snp["File1D"], snp["File1E"], snp["File2D"], snp["File2E"] = 0, 0, 0, 0

    snp = snp[['Chromosome', 'Position', 'Ref', 'Alt', 'File1R', 'File1A',
               'File1E', 'File1D', 'File2R', 'File2A', 'File2E', 'File2D']]
    snp["Zygousity"] = snp.apply(lambda x: get_zygousity(x.File1R, x.File1A), axis=1)

    snp["Chromosome"] = snp["Chromosome"].apply(lambda x: "chr" + str(x) if not "chr" in str(x) else x)

    snp.to_csv(output_pileup, sep=",", index=False)