import sys
import os
from transformers import AutoModelForSeq2SegLM, AutoTokenizer
import requests
from VidSumAI.exception import CustomException
from VidSumAI.logger import logger

class Summarizer:
    def load_model(self):
        try:
            logger.info("Loading Tokenizer and Summarizer Model--------------------------------")
            try:
                self.tokenizer=AutoTokenizer.from_pretrained("best_model")
                
                self.model = AutoModelForSeq2SegLM.from_pretrained("best_model")
                logger.info("Tokenizer and Model loaded")
            except:
                try:
                    logger.error(f"Model not availabe in best model dir of huggingface--.loading from artifacts--")
                    self.tokenizer=AutoTokenizer.from_pretrained("artifacts/model_trainer")
                    self.model=AutoModelForSeq2SegLM.from_pretrained("artifacts/model_trainer")
                    logger.info("Model loaded from arifacts/")
                except:
                    logger.info("Model not loaded from arifacts--loading from huggingface.")
                    self.tokenizer=AutoTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')
                    self.model=AutoModelForSeq2SegLM.from_pretrained('sshleifer/distilbart-cnn-12-6')
                    
                    logger.info("Model loaded from huggingface model hub")
        except Exception as e:
            logger.info("Could not load model")
            raise CustomException(e,sys)
        
        
    def summarize_text(self,transcript):
        
        try:
            logger.info("Summarizre starting...")
            inputs=self.tokenizer(transcript, max_length=1024, truncation=True, return_tensors='pt')
            
            summary_ids=self.model.generate(inputs["input_ids"],min_length=50,max_length=1024,length_penalty=2.0, num_beams=4, early_stopping=True)
            
            summary = self.tokenizer.batch_decode(summary_ids, skip_special_tokens=True,clean_up_tokenization_spaces=False)[0]

            return summary
        except Exception as e:
            logger.info(f"Error summarizing text check your best model: {e}")
            raise CustomException(e,sys)
