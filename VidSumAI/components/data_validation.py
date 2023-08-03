import os
import sys
from VidSumAI.logger import logger
from VidSumAI.exception import CustomException

class DataValidation:
    def __init__(self, dataset_folder):
        self.dataset_folder = dataset_folder
        
    def check_dataset(self):
        try:
            train_folder = os.path.join(self.dataset_folder, 'train')
            test_folder = os.path.join(self.dataset_folder, 'test')
            
            # Check if train and test folders exist
            if not os.path.exists(train_folder) or not os.path.exists(test_folder):
                raise ValueError("Train and/or test folders do not exist in the dataset folder.")
            
            # Check if train and test folders are not empty
            if not os.listdir(train_folder) or not os.listdir(test_folder):
                raise ValueError("Train and/or test folders are empty.")
            
            # Check for required metadata file existence
            # required_metadata_files = ['metadata.json']  # Update with actual required filenames
            # for file in required_metadata_files:
            #     if not os.path.exists(os.path.join(self.dataset_folder, file)):
            #         raise ValueError(f"Required metadata file {file} does not exist.")
            
            # Check for specific files in train folder (you can add more checks as needed)
            required_train_files = ['data-00000-of-00001.arrow']  # Update with actual required filenames for train
            for file in required_train_files:
                if not os.path.exists(os.path.join(train_folder, file)):
                    raise ValueError(f"Required train file {file} does not exist in train folder.")
            
            # Check for specific files in test folder (you can add more checks as needed)
            required_test_files = ['data-00000-of-00001.arrow']  # Update with actual required filenames for test
            for file in required_test_files:
                if not os.path.exists(os.path.join(test_folder, file)):
                    raise ValueError(f"Required test file {file} does not exist in test folder.")
            
            logger.info("Dataset validation successful.")
            return True
        
        except Exception as e:
            logger.info(f"Error during dataset validation: {e}")
            raise CustomException(e, sys)

    