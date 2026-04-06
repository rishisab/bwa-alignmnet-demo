# bwa-alignmnet-demo
#OVERVIEW
This project demonstrates how to:

Generate synthetic sequencing reads
Introduce mutations
Align reads to a reference genome using BWA
Understand why some reads fail to align

#KEY LEARNING
BWA uses a seed-based alignment algorithm.
For short reference sequences, even a single mutation can:

Break seed matching
Cause reads to be unmapped (FLAG 4)

#PIPELINE SETUP
1. Generate Reads
Extracts a 30 bp read from reference
Introduces mutations at different positions
Saves output in FASTQ format
2. Index Reference
bwa index data/ref.fasta
3. Align Reads
bwa mem -k 5 data/ref.fasta data/reads.fastq > results/out.sam

-k 5 reduces seed length → improves alignment for short sequences

#KEY INSIGHT
Perfect reads always align
Mutated reads may fail in small references
BWA is optimized for large genomes (e.g., human genome)
Seed length plays a crucial role in alignment
