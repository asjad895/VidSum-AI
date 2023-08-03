import os
import sys
import datasets
from VidSumAI.logger import logger
from VidSumAI.exception import CustomException

class DataIngestion:
    def __init__(self, dataset_name, subset, save_folder):
        self.dataset_name = dataset_name
        self.subset = subset
        self.save_folder = save_folder
        
    def download_datasets(self):
        try:
            # Check if save_folder exists, create if needed
            if not os.path.exists(self.save_folder):
                os.makedirs(self.save_folder)
            
            # Download the dataset using the datasets library
            dataset = datasets.load_dataset(self.dataset_name,self.subset)
            
            # Split the dataset into train and test subsets
            train_dataset = dataset['train'].train_test_split(test_size=0.2, seed=42)
            
            # Save train and test data to respective folders
            train_folder = os.path.join(self.save_folder, 'train')
            test_folder = os.path.join(self.save_folder, 'test')
            
            os.makedirs(train_folder, exist_ok=True)
            os.makedirs(test_folder, exist_ok=True)
            train_dataset['train'].save_to_disk('train')
            train_dataset['test'].save_to_disk('test')
            
            logger.info(f'Dataset{self.dataset_name} downloaded and saved to {self.save_folder}')
            
        
        except Exception as e:
            logger.error(f"Error downloading datasets: {e}")
            raise CustomException(e,sys)
