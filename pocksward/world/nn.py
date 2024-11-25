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

# Crossover function: combines the weights of two models
def crossover(model1, model2, solution1, solution2):
    # Extract model weights
    flat_weights1 = model_to_flat_array(model1)
    flat_weights2 = model_to_flat_array(model2)

    # Perform uniform crossover: combine the weights
    crossover_point = np.random.randint(0, len(flat_weights1))
    child1_weights = np.concatenate([flat_weights1[:crossover_point], flat_weights2[crossover_point:]])
    child2_weights = np.concatenate([flat_weights2[:crossover_point], flat_weights1[crossover_point:]])

    # Create child models
    child_model1 = SimpleNN(input_size=4, hidden_size=10, output_size=3)
    child_model2 = SimpleNN(input_size=4, hidden_size=10, output_size=3)

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
