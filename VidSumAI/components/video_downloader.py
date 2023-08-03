import sys
import os
from pytube import YouTube
import requests
from VidSumAI.exception import CustomException
from VidSumAI.logger import logger

class VideoDownloader:
    def __init__(self, url: str, save_path: str):
        self.url = url
        self.save_path = save_path
    
    def download(self) -> None:
        try:
            if 'youtube' in self.url:
                return self._download_youtube()
            return self._download_other()
        
        except Exception as e:
            logger.error(e)
            raise CustomException(e)
    
    def _download_youtube(self):
        try:
            yt = YouTube(self.url)
            video = yt.streams.first()
            video.download(self.save_path)
            logger.info(f"YOUTUBE VIDEO DOWNLOADEED TO{ os.path.join(self.save_path,video.default_filename)}")
            return os.path.join(self.save_path,video.default_filename)
        except Exception as e:
            logger.error(e)
            raise CustomException(e,sys)
    
    
    def _download_other(self):
        try:
            response = requests.get(self.url, stream=True)
            filename = self.url.split('/')[-1]
            with open(os.path.join(self.save_path, filename), "wb") as f:
                for chunk in response.iter_content(chunk_size=4096):
                    f.write(chunk)
            
            logger.info(f"OTHER VIDEO DOWNLOADED TO {os.path.join(self.save_path, filename)}")
            return os.path.join(self.save_path, filename)
            
        except Exception as e:
            raise CustomException(e, sys)
        
    