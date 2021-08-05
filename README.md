# microarray-ml

All the code for my reseach paper: [Machine Learning Models and Neural Networks for Hepatocellular carcinoma Microarray Diagnosis](https://github.com/raymondytian/microarray-ml/blob/master/research-paper/Machine_Learning_Models_and_Neural_Networks_for_Hepatocellular_carcinoma_Microarray_Diagnosis.pdf)

## Instructions

1. Download [dataset](https://drive.google.com/file/d/1L_WTo8lmGNH96zP0VKKsY1sMycS7QXR3/view?usp=sharing) and save it as ~/microarray-ml/db/Liver_GSE14520_U133A.csv

2. Install [dependencies](#Dependencies)

3. Run main.ipynb

## Files

* **gene_optimizer.py** - program to determine genes with the best accuracy and exports the results to **genes.txt**
* **genes.txt** - file containing genes in order of accuracy
* **main.ipynb** - main file to run (contains comments for ease of experimentation and explanations)

## Dependencies
* [python3.8](https://www.python.org/downloads/release/python-3810/)
* [numpy](https://numpy.org/install/)
* [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
* [matplotlib](https://matplotlib.org/stable/users/installing.html)
* [seaborn](https://seaborn.pydata.org/installing.html)
* [scikit-learn](https://scikit-learn.org/stable/install.html)
* [pytorch](https://pytorch.org/)

## Abstract
This paper examines the effectiveness of using machine learning  algorithms including a neural network on a hepatocellular carcinoma (HCC) microarray dataset. The dataset contained 358 samples and over 22,000 features (genes) and was pre-processed for ML applications. This dataset had been extensively used to compare the accuracy of various ML classification models. This paper proposes a new method; the utilization of ML models and neural networks could contribute to more affordable HCC diagnosis and could also be applied to other types of cancer. The discovery of a direct relationship between the best-performing genes and HCC demonstrated that machine learning could be a powerful tool for HCC diagnosis. The exceptional results produced by the neural network proved that neural networks could be the future for HCC diagnosis.
