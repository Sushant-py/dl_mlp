import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

# Define the classical MLP Architecture
class IntrusionDetectionMLP(nn.Module):
    def __init__(self, input_size, num_classes):
        super(IntrusionDetectionMLP, self).__init__()
        # Feedforward layers with standard ReLU and Dropout
        self.network = nn.Sequential(
            nn.Linear(input_size, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )

    def forward(self, x):
        return self.network(x)

def train_model():
    print("Loading CSE-CIC-IDS2018 data...")
    # TODO: Load dataset using pd.read_csv('data/your_dataset.csv')
    # TODO: Preprocess features and encode the legitimate + attack labels
    
    # Dataset specs based on CICFlowMeter output
    input_features = 80 
    num_classes = 7 
    
    # Initialize model, loss function, and optimizer
    model = IntrusionDetectionMLP(input_size=input_features, num_classes=num_classes)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    print("Model initialized. Ready to begin training.")
    # TODO: Build the training loop (epochs, forward pass, loss backward)
    # Target: macro-F1 > 0.90 for classes with >= 1000 instances

if __name__ == "__main__":
    train_model()