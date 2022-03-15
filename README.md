
<a name="BackToTop"></a>


# Natural Language Processing Projects

**Contributors: Cameron Stewart**

>The projects in this repository are unrelated projects that use Natural Language Processing (NLP) to gather insight. The purpose of these projects was purely academic to explore tools to scrape data from websites and apply NLP analysis.

[Project 1](../main/Project%201/Project_1.ipynb)

[Project 2](../main/Project%202/Project_2.ipynb)

[Project 3](../main/Project%203/Project_3.ipynb)

[Project 4](../main/Project%204/Project_4.ipynb)

[Project 5](../main/Project%205/Project_5.ipynb)

[Project 6](../main/Project%206/Project_6.ipynb)

---

## Table of Contents
- [Project 1 - Analyze Books by Reading Level](#P1)
- [Project 2 - SVM and LR Modeling](#P2)
- [Project 3 - KNN, NB, and RF Modeling](#P3)
- [Project 4 - Clustering](#P4)
- [Project 5 - EDA](#P5)
- [Project 6 - SVM and LR Modeling](#P6)
- [References](#References)

---

<a name="P1"></a>

## Project 1 - Analyze Books by Reading Level

[Project 1](../main/Project%201/Project_1.ipynb)

description of project

[Back to Top](#BackToTop)

---

<a name="P2"></a>

## Part 2 - SVM and LR Modeling

[Part 2 - SVM and LR Modeling Report](../main/2_SVM_LR_Modeling/SVM_LR_Modeling_Final.ipynb)

The full step-by-step analysis is included in the detailed report. Using standardization and one-hot encoding, the team uses Logistic Regression and Support Vector Machines to classify Win and Show. The team used 80% of the data for training and 20% for testing. The team outputted the models in a confusion matrix (shown below for the top SVM model) and reported key metrics such as accuracy and AUC. The team began including precision in Part 3 which is the best metric for this specific use case.

<img width="634" alt="image" src="https://user-images.githubusercontent.com/37990637/158275271-6696fed0-1be6-47e8-b309-2c877173b624.png">

Next, the team looked at feature importance. Shown below, the team looked at the importance from the top logistic regression model. The feature is more significant as the value goes to -1 or 1. If the feature is close to 0 then it is insignificant. We can see win_odds is the most significant feature.

<img width="381" alt="image" src="https://user-images.githubusercontent.com/37990637/158275549-2901fdc3-4496-46c1-817c-c463a7d5aebb.png">

Support Vector Machines outperformed Logistic Regression in this classification.

[Back to Top](#BackToTop)

---

<a name="P3"></a>

## Part 3 - KNN, NB, and RF Modeling

[Part 3 - KNN, NB, and RF Modeling Report](../main/3_KNN_NB_RF_Modeling/KNN_NB_RF_Modeling_Final.ipynb)

The full step-by-step analysis is included in the detailed report. The team moved to a stratified 10-fold cross validation to better account for the imbalance in the data while training and testing. The team also shifted to precision as the highest importance measurement metric. Using standardization and one-hot encoding, the team optimized models for K-Nearest Neighbors, Naive Bayes, and Random Forest Models. For KNN, the team explored multiple distance calculations and number of neighbors. For Naive Bayes, the team explored the Gaussian and Complement methods while optimizing the smoother parameter. For Random Forest, the team tuned the number of trees and the depth of the model. The report reviews models created using manual feature selection vs recursive feature selection. An example of the recursive feature selection plot is shown below.

<img width="398" alt="image" src="https://user-images.githubusercontent.com/37990637/158277875-71919306-6ad2-4085-b6ee-c62b21a7155b.png">

The top model for predicting Win and Show were both by the Random Forest model. The Random Forest model also beat out the previous Support Vector Machine. The model results on the testing data were outputted into a confusion matrix with the key metrics as shown below:

RF Predicting Win:

<img width="630" alt="image" src="https://user-images.githubusercontent.com/37990637/158277331-4efbaf75-ea2b-4dc5-aa76-9f47af867ddc.png">

RF Predicting Show:

<img width="634" alt="image" src="https://user-images.githubusercontent.com/37990637/158278163-db8238a3-c774-4e89-bbe6-0817b7b42401.png">

Also, the report tests if the results of the models were statistically different using paired t-testing and shows the feature importance of the features in the models.

[Back to Top](#BackToTop)

---

<a name="P4"></a>

## Part 4 - Clustering

[Part 4 - Clustering Report](../main/4_Clustering/Clustering_Final.ipynb)

The full step-by-step analysis is included in the detailed report. The team continued to use a stratified 10-fold cross validation to better account for the imbalance in the data while training and testing. The team also continued to use precision as the highest importance measurement metric. Using standardization and one-hot encoding, the team prepared the data. The team clustered key features in the training data using K-Means, DBSCAN, and Spectral Clustering. The appropriate number of clusters was determined using Silhouette Score and Distance of the nth neighbor plot.

<img width="382" alt="image" src="https://user-images.githubusercontent.com/37990637/158279961-423eabe4-6aef-46f8-8db3-c7b76b8b378c.png">

<img width="382" alt="image" src="https://user-images.githubusercontent.com/37990637/158280030-987a288e-423c-4fbb-9197-5209c31b96db.png">

Using KNN, the team was able to impute the proper cluster to the test data points in order to create a new feature. Passing the new features into Random Forest, the team attempted to classify Win and Show.

Example output from K-Means Clustering:

<img width="380" alt="image" src="https://user-images.githubusercontent.com/37990637/158279765-550fc547-2873-4a8a-b190-1425740a6169.png">

The results of the classification using Random Forest showed no significant improvements from the Part 3. As an additional step, the team tried using the new and original features in AdaBoost.

AdaBoost to predict Win:

<img width="632" alt="image" src="https://user-images.githubusercontent.com/37990637/158280506-6a30b2d3-ca0a-4d95-af75-0ecb4b372885.png">

AdaBoost to predict Show:

<img width="626" alt="image" src="https://user-images.githubusercontent.com/37990637/158280536-75a1f5d4-4a60-4839-9a16-e8482052bd59.png">

AdaBoost was the best model and showed improvement over the second-best model Random Forest for classifying Win and Show.

[Back to Top](#BackToTop)

---

<a name="References"></a>

## References

[Kaggle Dataset](https://www.kaggle.com/gdaley/hkracing)

[Part 1 - EDA Report](../main/1_EDA/EDA_Final.ipynb)

[Part 2 - SVM and LR Modeling Report](../main/2_SVM_LR_Modeling/SVM_LR_Modeling_Final.ipynb)

[Part 3 - KNN, NB, and RF Modeling Report](../main/3_KNN_NB_RF_Modeling/KNN_NB_RF_Modeling_Final.ipynb)

[Part 4 - Clustering Report](../main/4_Clustering/Clustering_Final.ipynb)


##### Technologies
Jupyter Notebook 
Python 3.7.7

[Back to Top](#BackToTop)
