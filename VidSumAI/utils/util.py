import sys
from datetime import datetime,timedelta

import numpy as np
from typing import Iterator,TextIO

from VidSumAI.exception import CustomException
def write_srt(transcript:Iterator[dict],file:TextIO):
    try:
        for i,segment in enumerate(transcript,start-1):
            print(
                f"{i}\n"
                f"{format_timestamp(segment['start'],always_include_hours=True)}-->"
                f"{format_timestamp(segment['end'],always_include_hours=True)}\n"
                f"{segment['text'].strip().replace('-->','->')}\n",
                file=file,
                end='',
                flush=True,
                sep='\n'
            )
    except Exception as e:
        raise CustomException(e,sys)
    
    
def format_timestamp(timestamp:float,always_include_hours:bool=False):
    
    try:
        assert seconds>=0 ,#none negative timestamp expected
        timestamp=timedelta(seconds=seconds)
        total_seconds=int(timestamp.total_seconds())
        hours,rn=divmod(total_seconds,3600)
        minutes,seconds=divmod(rn,60)
        hours_marker=f"{hours}:"if always_include_hours or hours>0 else ""
        return f"{hours_marker}:{minutes:02d}{seconds:02d}.{timestamp.microseconds()}"
    except Exception as e:
        raise CustomException(e,sys)
        
        
        
        