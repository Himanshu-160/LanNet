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
        self.HdfDataFile=HdfDataFile
        self.DataConfigFile=DataConfigFile
        self.sampling_rate=sampling_rate
        self.n=n
        self.__makefiles()
        self.Configs=self.__get_config()
        
    def __get_config(self):
        try:
            with open(self.DataConfigFile,'r') as f:
                return json.load(f)
        except:
            return {}
    
    def __create_H5(self):
        with open(self.HdfDataFile, 'w') as f:
            pass
        
    def __create_json(self):
        with open(self.DataConfigFile,'w') as h:
            pass
        
    def __makefiles(self):
        if(not os.path.isfile(self.DataConfigFile)):
            print("Data Configuration file do not exist at the given location.")
            print("New Dataset will also be created")
            print("If you would like to create a new one then enter Y else N")
            if(input()=="Y"):
                self.__create_json()
                self.__create_H5()
                print("Files created")
                
    def get_last_index(self):
        try:
            end_indices=[]
            for i in list(self.Configs.keys()):
                end_indices+=self.Configs[i]["end"]
            return max(end_indices)+1
        except:
            return 0
        
    def get_last_label(self):
        try:
            labels=[]
            for i in list(self.Configs.keys()):
                labels.append(self.Configs[i]["label"])
            return max(labels)+1
        except:
            return 0
    def __MFCC(self,audio):
        return librosa.feature.mfcc(np.array(audio),sr=self.sampling_rate,n_mfcc=self.n)
    
    def add_language(self,Language):
        if(Language in self.Configs.keys()):
            print("{} Language is already present in the dataset".format(Language))
            print("If you want to add the files present in the folder enter U")
            cmd=input()
            if(cmd=="U"):
                self.update_language(Language)
                return
            else:
                return
                
 
        print("Adding ", Language)
        last_index_h5=self.get_last_index()
        print(last_index_h5,"last_index")
        label=self.get_last_label()
        print(label,"label")
        audio_files=os.listdir(os.path.join(self.DataFolder,Language))
        self.Configs[Language]={"label":label,"start":[last_index_h5],"end":[]}
                  
        with h5.File(self.HdfDataFile,'a') as f:
            pth=os.path.join(self.DataFolder,Language)
            for i in range(len(audio_files)):
                audio,sr=librosa.load(os.path.join(pth,audio_files[i]))
                dset=f.create_dataset(str(last_index_h5),data=self.__MFCC(audio))
                dset.attrs["class"]=label
                last_index_h5+=1
                print(i)
            
        self.Configs[Language]["end"].append(last_index_h5-1)
                           
        with open(self.DataConfigFile,'w') as k:
            json.dump(self.Configs,k,indent=4)
        print("Added",German)
        
        
    def update_language(self,Language):
                           
        if(Language not in self.Configs.keys()):
            print("Language not already present in the dataset")
            print("Kindly first add it")
            return
                           
        last_index_h5=self.get_last_index()
        label=self.Configs[Language]["label"]
        audio_files=os.listdir(os.path.join(self.DataFolder,Language))
        self.Configs[Language]["start"].append(last_index_h5)
                           
        with h5.File(self.HdfDataFile,'a') as f:
            pth=os.path.join(self.DataFolder,Language)
            for i in range(len(audio_files)):
                audio,sr=librosa.load(os.path.join(pth,audio_files[i]))
                dset=f.create_dataset(str(last_index_h5),data=self.__MFCC(audio))
                dset.attrs["class"]=label
                last_index_h5+=1
                           
        self.Configs[Language]["end"].append(last_index_h5-1)
                           
        with open(self.DataConfigFile,'w') as k:
             json.dump(self.Configs,k,indent=4)
        
        
    def get_language_data(self):
        for i in list(self.Configs.keys()):
        	print("Language : ", i)
        	print("Label : ",self.Configs[i]["label"])
        return
        	
        	
        	
                           
                           
        
        
