from torch.utils.data import Dataset
import numpy as np
import json


class MFCC_Dataset(Dataset):
    def __init__(self, h5_file="/home/himanshu/Desktop/Semester_6/ML/project/dataset/MFCC.hdf5",indices):
        self.count=len(indices)
        self.X=np.zeros((self.count,1,40,431))
        self.y=np.zeros((self.count,))
        with h5py.File(h5_file,"r") as f:
            for j,i in enumerate(indices):
                dset=f[str(i)]
                self.y[j]=dset.attrs["class"]
                self.X[j]=np.reshape(np.array(dset),(1,40,431))
                print(i)
        
    def __getitem__(self, index):
        mfcc = torch.as_tensor(self.X[index])
        label = int(self.y[index])
        return (mfcc, label)

    def __len__(self):
        return self.count

    
def trainble_dataset(HdfDataFile="",DataConfig="",train_ratio=0.7):
    
    config={}
    with open(DataConfig,'r') as f:
        config=json.load(f)
    end_indices=[]
    for i in list(configs.keys()):
        end_indices+=configs[i]["end"]
    index=max(end_indices)+1
    
    indices=np.random.shuffle(np.array([i for i in range(index)]))
    l=int(len(indices)*0.7)
    
    train_ind=indices[:l]
    val_ind=indices[l:]
    
    train_set=MFCC_Dataset(HdfDataFile,train_ind)
    val_set=MFCC_Dataset(HdfDataFile,val_ind)
    
    return train_set,val_set 
    
    
    
    
    
    
    
    