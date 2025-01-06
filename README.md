# Applied Machine Learning Tasks

These are some applications of machine learning tasks using libraries such as Pandas, PySpark, Scikit-learn, PyTorch and TensorFlow. The tasks cover the major aspects of machine learning workflows, like data preprocessing, feature engineering, model building/training/evaluation, neural networks and dimensionality reduction.

--- 
## Repository Structure
Here is a description of folders and their files in repository:
1. `DataPrep-EDA/` <br>

Contains scripts for exploratory data analysis (EDA) and data preprocessing workflows. Also, Focuses on understanding datasets, handling missing values, and visualizing data distributions..

2. `FeatureEngineering/` <br>

Includes feature engineering scripts such as encoding categorical variables, scaling numerical features, and creating new features. Also, Demonstrates methods for preparing data for machine learning models.

3. `ModelTrainPandas/` <br>

Scripts for training machine learning models using Pandas and Scikit-learn. Covers tasks like logistic regression, random forests, and support vector machines.

4. `ModelTrainPySpark/` - download the dataset from <br>

Demonstrates building and training models using PySpark for distributed data processing. Suitable for handling large-scale datasets.


5. `SonarNN_Classifier/` <br>

Implements fully connected feed-forward neural networks to classify sonar signals as bouncing off metal cylinders or rocks. Includes multiple experiments with architectures, hyperparameters, and optimization algorithms.

6. `MnistCNN_Digits/` <br>

Contains code for training convolutional neural networks (CNNs) on the MNIST handwritten digits dataset.
Includes model architecture, hyperparameter tuning, and evaluation.


## Setup Instructions

To set up the repository and its dependencies, follow one of these methods:

### Using `requirements.txt` with `pip`

1. Create a virtual environment:
```
python -m venv ml_assignments_env
source ml_assignments_env/bin/activate  # Linux/Mac
.\ml_assignments_env\Scripts\activate   # Windows
```

2. Install dependencies
```
pip install -r requirements.txt
```

### Using `environment.yml` with `Conda`:

1. Create a Conda environment:
```
conda env create -f environment.yml
conda activate ml_assignments_env
```

<br>
You're welcome to contriibute to the repo. Whether it’s adding new tasks, improving code, or suggesting features, feel free to open an issue or submit a pull request!



