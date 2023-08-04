import os
import sys
from VidSumAI.logger import logger
from VidSumAI.exception import CustomException
from VidSumAI.components.data_ingestion import DataIngestion
from VidSumAI.components.data_validation import DataValidation
from VidSumAI.components.data_preprocessing import DataProcessingConfig
from VidSumAI.components.data_preprocessing import DataProcessing
from VidSumAI.components.model_trainer import ModelTrainer
from dataclasses import dataclass

@dataclass
class TrainingPipelineConfig:
    artifacts_folder='artifacts'
    data_ingestion_artifacts=os.path.join(artifacts_folder,"data_ingestion")
    data_processing_artifacts = os.path.join(artifacts_folder, "data_processing")
    model_trainer_artifacts = os.path.join(artifacts_folder, "model_trainer")

    
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
    
    # create an instance of the config dataclass for data processing component
    data_processing_config = DataProcessingConfig(max_input_length=128, max_target_length=64, dataset_folder=config.data_ingestion_artifacts, artifacts_folder=config.data_processing_artifacts)
    # create an instance of the 'DataProcessing' class and assigns variable as 'processor'.
    processor = DataProcessing(data_processing_config)
    processor.process_data()

    # # create an instance of the `ModelTrainer` class with the specified parameters.
    trainer = ModelTrainer(model_checkpoint='facebook/bart-base', 
                           processed_dataset_folder=config.data_processing_artifacts, 
                           trainer_artifact_dir=config.model_trainer_artifacts)
    trainer.train()