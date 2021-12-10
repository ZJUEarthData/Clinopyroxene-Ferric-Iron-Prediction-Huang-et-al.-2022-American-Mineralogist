# PYRO_PROCESSOR

This project provides three functions for pyroxene's instances:
+ **calculator**: convert oxide weight percentages data into molar ion concentrations;
+ **predictor**: predict Fe3+/Fetot value with the given data set by trained ML models respectively;
+ **classifier**: classify every entry into a specific kind of pyroxene according to the classification criteria of *Commission on New Minerals and Mineral Names*.(Morimoto, N. (1988). Nomenclature of pyroxenes. Mineralogy and Petrology, 39(1), 55–76) 

## APPLICATION
See **Manual_for_Mac** or **Manual_for_Windows** for application details.The manual would tell:
+ configuration  
+ data format 
+ package details
+ operation steps

## MAIN DIRECTORY
+ **model_training_code** : this directory contains the codes to train the merchine learning model with designated hyperparameters   and data sets used for train
+ **Fe3_calculation_program** : this directory contains the codes packaged in 【**pyroxene_processor**】to provide three functions mentioned above and other related dependencies

## CONTRIBUTORS
+ Can He (Sany)  
Email : hecan@mail2.sysu.edu.cn
+ Weihua Huang  
Email : 21938003@zju.edu.cn

## REFERENCE
+ Huang W-H, Lyv Y, Du M-H, He C, Gao S-D, Xu R-J, Xia Q-K, and ZhangZhou J\* (2022) [Estimation of ferriciron contents in clinopyroxene by machine learning models](https://www.researchgate.net/publication/354803339_Title_Estimation_of_ferric_iron_contents_in_clinopyroxene_by_machine_learning_models). American Mineralogist (in press,doi:https://doi.org/11.2139/am-2022-8189)
