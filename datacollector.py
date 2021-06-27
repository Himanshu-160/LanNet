import numpy as np
import h5py as h5
import librosa
import os
import json


"""
Datafolder should be in the following format :

DataFolder
    |--->Language_1
            |--->audio_file_0
            |--->audio_file_1
            |--->audio_file_2
            |
            |
            |--->audio_file_n
    |--->Language_2(folder)
    |
    |
    |
    |
    |--->Language_N(folder)    


"""

class FeatureExtractor():
    def __init__(self, DataFolder, HdfDataFile, DataConfigFile, sampling_rate=22500, n=20):
        self.DataFolder=DataFolder
        self.HdfDatafile=HdfDatafile
        self.DataConfigFile=DataConfigFile
        self.sampling_rate=sampling_rate
        self.n=n
        self.__makefile()
        self.Configs=self.__get_congif()
        
    def __get_config():
        with open(self.DataConfigFile,'r') as f:
            return json.load(f)
    
    def __create_H5():
        with open(self.HdfDataFile, 'w') as f:
            pass
        
    def __create_json():
        with open(self.DataConfigFile,'w') as h:
            pass
        
    def __makefiles():
        if(not os.path.isfile(self.DataConfigFile)):
            print("Data Configuration file do not exist at the given location.")
            print("New Dataset will also be created")
            print("If you would like to create a new one then enter YES else NO")
            if(input()=="YES"):
                self.__create_DataConfigFile()
                self.__create_H5()
                print("Files created")
                
    def get_last_index():
        try:
            end_indices=[]
            for i in self.Configs:
                end_indices+=i["end"]
            return max(end_indices)+1
        except(json.decoder.JSONDecodeError):
            return 0
        
    def get_last_label():
        try:
            labels=[]
            for i in self.Configs:
                labels.append(i["label"])
            return max(labels)+1
        except(json.decoder.JSONencodeError):
            return 0
    def __MFCC(audio):
        return librosa.feature.mfcc(np.array(audio),sr=self.sampling_rate,n_mfcc=self.n)
        
    def add_language(Language):
        if(Language in self.Configs.keys()):
            print("{} is already present in the dataset".format(Language))
            print("If you want to add the files present in the folder enter update")
            cmd=input()
            if(cmd="update"):
                update_langauge(Language)
                return
            if(cmd="renew"):
                renew_langauge(Language)
                return 
   
        last_index_h5=self.get_last_index()
        label=self.get_last_label()
        audio_files=os.listdir(os.path.join(Datafolder,Language))
        self.Configs[Language]={"label":label,"start":[last_index],"end":[]}
                  
        with h5.File(HdfDataFile,'a') as f:
            path=os.join(Datafolder,Language)
            for i in range(len(audio_files):
                  audio,sr=librosa.load(os.path.join(audio_files[i]))
                  dset=f.create_dataset(str(last_index),data=self._MFCC(audio))
                  dset.attrs["class"]=label
                  last_index+=1
                           
        self.Configs[Langauge]["end"].append(last_index)
                           
        with open(DataConfigFile,'w') as k:
            json.dump(self.Configs,k,indent=4)
                  
    def update_language(Language):
                           
        if(Language not in self.Config.keys()):
            print("Language not already present in the dataset")
            print("Kindly first add it")
            return
                           
        last_index_h5=self.get_last_index()
        label=self.Config[Language]["label"]
        audio_files=os.listdir(os.path.join(Datafolder,Language))
        self.Configs[Langauge]["start"].append(last_index)
                           
        with h5.File(HdfDataFile,'a') as f:
            path=os.join(Datafolder,Langauge)
            for i in range(len(audio_files)):
                audio,sr=librosa.load(os.path.join(audio_files[i]))
                dset=f.create_dataset(str(last_index),data=self._MFCC(audio))
                dset.attrs["class"]=label
                           
         self.Configs[Language]["end"].append(last_index)
                           
         with open(DataConfigFile,'w') as k:
             json.dump(self.Configs,k,indent=4)
             
    def get_language_data():
        for i in list(self.Configs.keys()):
        	print("Language : ", i)
        	print("Label : ",i["label"])
        	
        	
        	
                           
                           
        
        
