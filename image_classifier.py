from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from torchvision import models, transforms
from PIL import Image
import torch
import numpy as np

# Load the pre-trained ResNet18 model
model = models.resnet18(weights='DEFAULT')
model.eval()  # Set the model to evaluation mode

# Define image transformations
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Create FastAPI instance
app = FastAPI()

@app.post("/classify/")
async def classify_image(file: UploadFile = File(...)):
    # Open the uploaded image file
    image = Image.open(file.file).convert("RGB")
    
    # Apply transformations to the image
    image_tensor = transform(image).unsqueeze(0)  # Add batch dimension
    
    # Make predictions
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        top_prob, top_class = torch.topk(probabilities, k=1)  # Get top prediction

    # Mapping the predicted index to the labels we defined
    cat_dog_labels = ['cat', 'dog']
    
    # Find the class with the highest probability
    predicted_label = "unknown"
    predicted_index = top_class.item()

    if predicted_index < len(cat_dog_labels):
        predicted_label = cat_dog_labels[predicted_index]
    
    return JSONResponse(content={"label": predicted_label})

