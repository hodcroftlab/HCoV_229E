# HCoV 229E Ingest and Analysis Pipeline

This repository provides a complete ingest and analysis pipeline for Human coronavirus 229E (HCoV 229E), built using Snakemake and based on the [Nextstrain](https://nextstrain.org/) framework.

It includes tools to download and process sequences and metadata, generate Nextstrain-compatible inputs, and perform genomic analysis and visualization.

The data for this analysis is available from [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/). Instructions for downloading sequences are provided under [Sequences](#sequences).

## Prerequisites
Ensure the following are installed:
- Python=3.8 or higher
- Micromamba or Conda
- Snakemake=7
- Nextstrain CLI

## Installation

Install the Nextstrain environment by following [these instructions](https://docs.nextstrain.org/en/latest/guides/install/local-installation.html).

## Sequences

You can download HCoV 229E sequences:

Manually from [NCBI Virus](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/)

Automatically using the `ingest` pipeline. Please refer to the [README](ingest/README.md) in the `ingest` folder.

## Configuration Files

Found in `config` and `data` subdirectories:

config.yaml: Pipeline configuration

geo_regions.tsv, lat_longs.tsv: Geographical mappings

colors.tsv: Color palette for Nextstrain builds

clades_genome.tsv: For manually labeling clades

dropped_strains.txt: List of strains to exclude

auspice_config.json: Required for visualization

reference_sequence.gb: Reference file for 229E (from GenBank: AF304460)

## Nextstrain Analysis 
You can perform either a whole-genome or protein-specific build of 229E using Nextstrain.

### Usage Examples

#### Activate your environment:

```bash
micromamba activate nextstrain
```

#### Run a full build:

```bash
snakemake --cores 9 all
``` 

#### Run specific builds:

```bash
snakemake auspice/HCoV_229E_genexy.json --cores 9
snakemake auspice/HCoV_229E_whole_genome.json --cores 9
```

#### Visualizing the Build

```bash
auspice view --datasetDir auspice
```

To run two visualizations simultaneously, you may need to set the port:

```bash
export PORT=4001
```

## 🙏 Acknowledgments
- [Nextstrain](https://nextstrain.org/)
- [Auspice](https://auspice.us/)
- [Hodcroftlab](https://github.com/hodcroftlab/template_nextstrain/tree/master) 
- [Snakemake](https://snakemake.readthedocs.io/en/stable/)
