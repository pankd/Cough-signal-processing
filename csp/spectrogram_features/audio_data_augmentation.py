# inspired from Qishen Ha code

import cv2
import os
import numpy as np
import pandas as pd 
import librosa
import matplotlib.pyplot as plt
from .core_features import Spectrogram_features as sp

class Audio_augmentation(object):
    
    
    @staticmethod
    def time_shifting(signal_spectrogram):
        
        start = int(np.random.uniform(-4800,4800))
        signal = signal_spectrogram
        
        EPS = 1e-8


        if start >= 0:
            signal_time_shift = np.r_[signal[start:], np.random.uniform(-0.001,0.001, start)]
        else:
            signal_time_shift = np.r_[np.random.uniform(-0.001,0.001, -start), signal[:start]]
        
        
        
        log_spectrogram  = np.log(sp.get_spectrogram(signal_time_shift)['magnitude'] + EPS)
        plt.imshow(log_spectrogram, aspect='auto', origin='lower',)
        plt.title('time shifted audio spectrogram')
            
    
        return{
                'time_shift'       : signal_time_shift,
                'log_spectrogram'  : log_spectrogram,
                'plt'              : plt
               }
    
    
    
    @staticmethod
    def speed_tuning(signal_spectrogram):
        
        EPS = 1e-8
        
        speed_rate = np.random.uniform(0.7,1.3)
        wav_speed_tune = cv2.resize(signal_spectrogram, (1, int(len(signal_spectrogram) * speed_rate))).squeeze()
        
        if len(wav_speed_tune) < 16000:
            pad_len = 16000 - len(wav_speed_tune)
            wav_speed_tune = np.r_[np.random.uniform(-0.001,0.001,int(pad_len/2)),
                                   wav_speed_tune,
                                   np.random.uniform(-0.001,0.001,int(np.ceil(pad_len/2)))]
        else: 
            cut_len = len(wav_speed_tune) - 16000
            wav_speed_tune = wav_speed_tune[int(cut_len/2):int(cut_len/2)+16000]


        log_spectrogram = np.log(sp.get_spectrogram(wav_speed_tune)['magnitude'] + EPS)
        plt.imshow(log_spectrogram, aspect='auto', origin='lower',)
        plt.title('speed tuned audio spectrogram')


        return {'speed_tune' : wav_speed_tune, 
                'wav length' :  wav_speed_tune.shape[0], 
                'plt'        : plt
               }


    @staticmethod
    def background_noise(signal_spectrogram):
        
        pass
    