import numpy as np
import pygad
import torch
import torch.nn as nn
import torch.optim as optim

#generating NNs
class NN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x


# Function to extract model weights into a flat array
def model_to_flat_array(model):
    flat_weights = []
    for param in model.parameters():
        flat_weights.append(param.detach().cpu().numpy().flatten())
    return np.concatenate(flat_weights)

# Function to set model weights from a flat array
def flat_array_to_model(flat_weights, model):
    idx = 0
    for param in model.parameters():
        numel = param.numel()
        param.data = torch.tensor(flat_weights[idx:idx+numel].reshape(param.shape)).float()
        idx += numel

# Crossover function: combines the weights of two models DAMIT THIS CODE IS CHATGPT and is wrong?
def crossover(models, coefs):
    # Extract model weights to numpy array
    flat_models = model_to_flat_array(models)
    
    print(flat_models)
    #do weighted average of values

    # Perform uniform crossover: combine the weights
    
    # Create child models
    child_model1 = NN(input_size=4, hidden_size=10, output_size=3)
    child_model2 = NN(input_size=4, hidden_size=10, output_size=3)

    flat_array_to_model(child1_weights, child_model1)
    flat_array_to_model(child2_weights, child_model2)

    return child_model1, child_model2

# Mutation function: randomly modify weights
def mutate(model, mutation_rate=0.1):
    flat_weights = model_to_flat_array(model)
    mutation_mask = np.random.rand(len(flat_weights)) < mutation_rate
    flat_weights[mutation_mask] += np.random.randn(np.sum(mutation_mask)) * 0.1  # Add random noise to mutated genes
    flat_array_to_model(flat_weights, model)
    return model
