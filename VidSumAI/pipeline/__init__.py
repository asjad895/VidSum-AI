import os
import sys
from VidSumAI import logger
from VidSumAI.exception import CustomException
from VidSumAI.components.data_ingestion import DataIngestion
from VidSumAI.components.data_validation import DataValidation
from dataclasses import dataclass

@dataclass
class TrainingPipelineConfig:
    artifacts_folder='artifacts'
    data_ingestion_artifacts=os.path.join(artifacts_folder,"data_ingestion")
    
def create_directory(config=TrainingPipelineConfig):
    if not os.path.exists(config.artifacts_folder):
        os.makedirs(config.artifacts_folder)
    if not os.path.exists(config.data_ingestion_artifacts):
        os.makedirs(config.data_ingestion_artifacts)
        
def run_training_pipeline(config=TrainingPipelineConfig):
    create_directory(config)
    data_ingestion=DataIngestion(dataset_name='lighteval/summarization',subset='xsum',save_folder=config.data_ingestion_artifacts)
    data_ingestion.download_datasets()
    data_validation=DataValidation(dataset_folder=config.data_ingestion_artifacts)
    data_validation.check_dataset()
