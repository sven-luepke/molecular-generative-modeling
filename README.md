# Generative Modeling for Inverse Molecular Design | [Project Report](report.pdf)

Code for the interdisciplinary project "Generative Modeling for Molecules"

## Setup
```
conda env create -f environment.yml
conda activate idp
```

## Training

The following commands can be used to train all models from scratch:
##### Graph Variational Autoencoder
```
cd source
./train_graph_vae_models
```
##### Mixture Model
```
cd source
./train_mixture_models
```

## Pretrained Models
Pretrained models can be downloaded [here](https://drive.google.com/drive/folders/1AevYhNYIih6OiZ-97LklmQzSvTbatCuO). To replicate the results from the report, place the `.pt` file in `source/checkpoints` and run the notebooks in `source`.
