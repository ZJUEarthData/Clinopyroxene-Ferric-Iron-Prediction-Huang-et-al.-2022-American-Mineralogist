# Setup 
See 【Manual_for_Mac】 or 【Manual_for_Windows】 for application details.The manual would tell:

+ configuration
+ data format
+ package details
+ operation steps

The following introduction will be included in 【Manual_for_Mac】or【Manual_for_Windows】also. In the manual, there are more specific details.

# Structure
+ **pyroxene_processor**: a python package, created on our own, provides a python function *process*, which performs as the combination of calculator, predictor and classifier.

+ **dataset**: this directory stores the data, which can be replaced by your own data, to process. Please name your own data sheet as "cpx_data.xlsx" if it is cpx data or name the sheet as "spl_data.xlsx" if it is spl data. The package 'pyroxene_processor' will import the data in the form of excel sheet automatically.

+ **results**: this directory will be created automatically as soon as you run the command, such as ```>>>process(cpx_data="cpx_data.xlsx", spl_data="spl_data.xlsx", pattern=3)```. It will store the calculation results, prediction results and classification results.

+ **requirments.txt**: it’s a text where all the dependencies we used when creating the package are listed. It is used for configuration. You can ignore it if you run *setup.sh* in the command line. Or you can run ```pip install -r requirements.txt``` in the command line.

+ **setup.sh**: on Mac, a bash script, which can be executed directly in the command line, contains the code to download all the dependencies automatically we'll use when importing the package.

+ **setup.bat**: on Windows, a batch script, which can be executed directly in the command line, contains the code to download all the dependencies automatically we'll when importing the package.
 
+ **vir_env_mac**: on Mac a python’s virtual environment with all the dependencies we use when creating the package. You can run the commands and *execution.py* when activating this virtual environment without running *setup.sh*.

+ **vir_env_windows**: on Windows a python’s virtual environment with all the dependencies we use when creating the package. You can run the commands and *execution.py* when activating this virtual environment without running *setup.bat*. 

+ **excecution.py**: it’s a python scripts used to run the commands for processing the given data once you execute it in the command line. It is editable according to the routine we mentioned in Processing part of 【Manual_for_Mac】or 【Manual_for_Windows】.

# Data Process Steps
This package *pyroxene_processor* will provide you with a function to use. The presence of ```>>>``` before a command indicates that the command is a python script, which means that it should be excuted by a python interpreter. More detail, please check the corresponding manual.
Please import it in this way in command line:
Activate Python interpreter in Terminal(Mac) or Dos(Windows).
```
python
```
Import the package *pyroxene_processor*.
```
>>> from pyroxene_processor.processor import process
```
When you want to use pattern I to process, *cpx_data.xlsx* is needed.
```
>>> process(cpx_data="cpx_data.xlsx", pattern=1)
```
When you want to use pattern II to process, *cpx_data.xlsx* is needed.
```
>>> process(cpx_data="cpx_data.xlsx", pattern=2)
```
When you want to use pattern III to process, *cpx_data.xlsx* and *spl_data.xlsx*  are needed.
```
>>> process(cpx_data="cpx_data.xlsx", spl_data="spl_data.xlsx",  pattern=3)
```



