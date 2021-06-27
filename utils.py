import torch.optim as optim
from torch.autograd import Variable
import torch
import json

def train(device="cpu",criterian, optimizer, model, data_loader,val_loader):
    model = model.to(device)
    trainig_loss = 0.0
    val_loss = 0.0
    
##Training of one epoch

    model.train()
    for data in train_loader:
        
        imgs, labels  = data
        batch_size = imgs.shape[0]
        
        imgs = Variable(imgs.to(device))
        labels = Variable(labels.to(device))
 
        optimizer.zero_grad()
        outputs = model(imgs.double())
        loss = criterion(outputs, labels)
 
        loss.backward()
        optimizer.step()
                      
        training_loss += loss.data * batch_size
    
## Validation     
    model.eval()
    with torch.no_grad():
        for data in val_loader:
            
            imgs, labels  = data
            batch_size = imgs.shape[0]
 
            imgs = Variable(imgs.to(device))
            labels = Variable(labels.to(device))
        
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            val_loss += loss.data * batch_size
            
    return (training_loss,val_loss)

## Testing
def test(device="cpu", model, data_path=None, result_path=None,sampling_rate=22500,n=40):
    model.eval()
    audio_files=os.listdir(data_path)
    prediction={}
    with torch.no_grad():
        for data in audio_files:
  
            ad,sr=librosa.load(os.path.join(data_path,data))
            mfcc=librosa.feature.mfcc(np.array(ad),sr=sampling_rate,n_mfcc=self.n)
            
            img=torch.DoubleTensor(np.reshape(mfcc,(1,mfcc.shape[0],mfcc.shape[1])))
            
            output= model(imgs)
            prediction[data]=output
    with open(result_path,'w') as j:
        json.dump(prediction,j,indent=4)
 
        
            
        
            