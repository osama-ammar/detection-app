# Project : Kidney Stones detection 
> Getting a working template pipeline for detection
> with many features in training and reporting

## Description
- This project is designed to train a model for Kidney Stones detection  , where:  
    - input ---> is a 2D CT coronal slice .
    - output ---> is a bbox around stones
- The used model is YOLO-8

## Usage
- link [https://osama-ammar-detection-app-streamlit-app-kuziji.streamlit.app/]

## Configuration
The project can be configured by editing `model_config.yaml` file . The available configuration options are as follows:
```
- `input_size`: The size of input images (default: ...).
- `in_channels`: The number of input channels (default: 1).
- `out_channels`: The number of output channels (default: 2).
- `epochs`: The number of training epochs (default: 300).
- `batch_size`: The batch size for training (default: 16).
- `learning_rate`: The learning rate for optimization (default: 1e-3).
- `log_period`: The interval for printing training logs (default: 1).
- `criterion` : The Loss function used (default:....).
- `optimizer`: The optimizer (default:AdamW).
- `mode`: The mode of operation (train/test/export).
- `weights_path`: The path to load the checkpoint for testing or exporting .
- `dataset_path`: The path to the dataset directory .
- `results_path`: The path to save the result files .
```

## Dataset
The dataset used for training and testing should be placed in the specified `dataset_path` directory. The dataset  .......
- data set Balance :

## Training
To train the model, set the `mode` argument to `train`. The training progress, including loss and accuracy, will be displayed during training.

## Testing
To test the trained model, set the `mode` argument to `test`. The model will be loaded from the `checkpoint_path`, and the test results will be displayed.

## Exporting
To export the trained model, set the `mode` argument to `export`. The model will be loaded from the `checkpoint_path`, and the exported model will be saved in the `model_path`.

## Results
The results, including trained models and logs, will be saved in the specified `model_path` and `result_path` directories, respectively. Each run of the program will create a subdirectory in the `result_path` directory named with the model type and the current date and time.

---------------------------------------------------------------------------------------------------------------------
### Model performance
- Generally , accuracy = .......................
- Accuracy in bad Cases = .........................

----------------------------------------------------------------------------------------------------------------------

## TODO 
- [ ] General steps
    - [ ] select a problem (simple one)
    - [ ] prepare data and make analysis to it , track it 
    - [ ] select a model and train , fine tune or use it directly if applicable
    - [ ] view results in MLFlow or weight and bias 
    - [ ] deploy it in a gui or AWS service 
    - [ ] make a report with images and links 

- [x] Editing hyperparams in only ony file
- [ ] model versioning
- [x] Applicability of different dataset
- [ ] Augmentations scripts
    - [ ] image classification
    - [ ] bboxes detection
    - [ ] segmentation
    - [ ] overall example
- [ ] automatic experiementation
- [ ] early stopping
- [ ] CI/CD
- [ ] making readme template ...including (images , tables , videos , emojies ...)
- [ ] Cleaning and organizing
- [ ] Feature engineering 
- [ ] Error analysis
- [ ] Using weight and biases
- [x] apply DVC
- [/] use MLFlow
    - [x] log params
    - [x] log models
    - [ ] log dataset

- [x] making one file -scv- for tracking experiments , each expriement and its parameters and metrics
    - generating this file automatically  or generating it after making experiemnts (replaced by MLFlow)
    
- [ ] include training time and computer resources in trial summary
- [ ] apply some performance optimization mentioned in [https://pytorch.org/tutorials/recipes/recipes/tuning_guide.html]

---------------------------------------
![Example Image](loss.png)


### Credits
-
-
