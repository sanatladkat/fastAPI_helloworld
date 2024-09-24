# FastAPI AI Model Serving with PyTorch
### Medium [article](http://127.0.0.1:8000/docs) : 

This repository contains a FastAPI application that serves multiple pre-trained PyTorch models for image classification and sentiment analysis. The application demonstrates how to create a lightweight REST API that can handle various AI tasks effectively.

## Features

- **FastAPI Framework**: Built with FastAPI for high-performance API development, featuring automatic documentation generation for easy exploration.
- **Image Classification**: Classifies images of cats and dogs using a pre-trained ResNet18 model.
- **Sentiment Analysis**: Analyzes sentiment from text inputs using a sentiment analysis model from Hugging Face's Transformers library.
- **Image Upload Support**: Users can upload images directly to the API for classification.
- **Text Input Support**: Users can submit text to receive sentiment labels (e.g., positive or negative) with associated confidence scores.

## Getting Started

### Prerequisites

Make sure you have Python 3.7 or higher installed. You can check your version with:

```bash
python --version
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sanatladkat/fastAPI_helloworld.git
    ```

2. Navigate to the project directory:

    ```bash
    cd YOUR_REPOSITORY
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To start the FastAPI application, run:

Hello World App:
```bash
uvicorn main:app --reload
```

Sentiment Analysis app:
```bash
uvicorn sentiment_analysis:app --reload
```

Image Classification App:
```bash
uvicorn image_classifier:app --reload
```

Access the API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints

### Image Classification

- **Endpoint**: `POST /classify/`
- **Usage**: Upload an image to classify it as either a cat or dog.

### Sentiment Analysis

- **Endpoint**: `POST /predict/`
- **Usage**: Send a JSON object with a text field to receive sentiment analysis results.

## Example Usage

### Image Classification

You can test the image classification endpoint using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/classify/" -F "file=@path_to_your_image.jpg"
```

### Sentiment Analysis

You can test the sentiment analysis endpoint using `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/predict/" -H "Content-Type: application/json" -d '{"text": "I love using FastAPI!"}'
```

## Contributions

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit issues or pull requests.