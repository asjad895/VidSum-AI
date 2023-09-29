import os
import sys
import tempfile
import warnings
from typing import List, Dict
import ffmpeg
import whisper
from dataclasses import dataclass
from VidSumAI.logger import logger
from VidSumAI.utils.util import write_srt

@dataclass
class video2usbConfig:
    output_dir: str = 'srt'
    audio_codec: str = 'pcm_s16le'
    audio_sample_rate: str = '16k'
    audio_channels: int = 1

class SubtitleGenerator:
    def __init__(self, config: video2usbConfig):
        self.output_dir = config.output_dir
        self.audio_codec = config.audio_codec
        self.audio_sample_rate = config.audio_sample_rate
        self.audio_channels = config.audio_channels

    def extract_audio_from_video(self, video_paths: List[str]) -> Dict[str, str]:
        """Extract audio from a video using ffmpeg"""

        tempdir = tempfile.gettempdir()
        audio_paths = {}

        for video_path in video_paths:
            filename = os.path.basename(video_path).split('.')[0]
            output_path = os.path.join(tempdir, f"{filename}.wav")

            logger.info(f'Extracting audio from {video_path}')
            try:
                (
                    ffmpeg.input(video_path)
                    .output(
                        output_path,
                        acodec='pcm_s16le',
                        ar=self.audio_sample_rate,
                        ac=self.audio_channels
                    )
                    .run(quiet=False, overwrite_output=True, capture_stdout=True, capture_stderr=True)
                )
            except ffmpeg.Error as e:
                logger.error(e.stdout.decode('utf-8'))
                logger.error(e.stderr.decode('utf-8'))
                raise e

            audio_paths[video_path] = output_path

        return audio_paths

    def subtitle_from_audio(self, audio_paths: Dict[str, str], transcribe_fn=callable) -> Dict[str, str]:
        subtitles_paths = {}

        for video_path, audio_path in audio_paths.items():
            try:
                logger.info(f'Transcribing audio from {audio_path}')

                subtitle_path = os.path.join(self.output_dir, f"{os.path.basename(video_path).split('.')[0]}.srt")
                warnings.filterwarnings("ignore")
                transcript = transcribe_fn(audio_path)
                warnings.filterwarnings('default')
                with open(subtitle_path,'w',encoding='utf-8') as srt_file:
                    write_srt(transcript)

                subtitles_paths[video_path] = subtitle_path
                logger.info(f'Subtitle generated: {subtitle_path}')
            except ffmpeg._run.Error as e:
                logger.info(f'Error generating subtitle for {os.path.basename(audio_path)}: {e}')

        return subtitles_paths,transcript
    
    
    def get_subtitle(self,video_paths:list[str],model_path:str,task:str,verbose=False)->Dict[str,str]:
        """Generate subtitles from a video using a trained model"""
        os.makedirs(self.output_dir,exist_ok=True)
        if model_path.endswith('.en'):
            print(f"{model_path} is an english model")
        try:
            logger.info(f'Loading model from {model_path}')
            model = whisper.load_model(model_path)
            audio_paths=self.extract_audio_from_video(video_paths)
            subtitles_paths=self.subtitle_from_audio(
                audio_paths,
                lambda audio_path: model.transcribe(audio_path,verbose=verbose)
            )
    
        except Exception as e:
            logger.info(f'Error loading model: {e}')
            raise e
        
        return subtitles_paths,audio_paths