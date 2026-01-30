# Question_Answering_Bot_With_Provided_Context

### Extractive Question Answering System
!

#### Overview
This project demonstrates a complete Machine Learning lifecycle: fine-tuning a BERT-based model for Question Answering, tracking the training process with MLflow, and deploying the final model as a web application and REST API via Hugging Face Spaces.  

#### Project Components
QA_Model_FineTuning.ipynb: The core notebook containing data preprocessing (SQuAD dataset), model training logic, and MLflow integration.  

app.py: A Gradio-based application script used for local testing and cloud deployment.  

requirements.txt: Dependency list for environment reproducibility.  

api_call_check.py: To test the api of the model.  

#### Key Implementations
1. Experiment Tracking (MLflow)  
Training was conducted on Kaggle with real-time logging. We tracked:  

Loss Metrics: Monitoring test loss.   

Artifacts: Automatically saving the best model weights for deployment.  

2. Deployment & API Access  
The model is hosted on Hugging Face Spaces. While it provides a user-friendly Gradio interface, it also functions as a REST API.  

#### To call the API programmatically:  

#### Python  
from gradio_client import Client  

client = Client("Adrita03/QnA_with_context")  
result = client.predict(  
    question="What is the name of the dog?",  
    context="Alice is a software engineer. She lives in Seattle. Alice has a dog named Buddy. In her free time, she likes to bake chocolate cakes.",  
    api_name="/get_answer"   
)  
print(result) # Output: Buddy   
#### 🚧 Training Constraints & Model Performance
Due to time and computational scarcity, the model was trained on a subset of the dataset for 500 batches.  

Observation: Because the model has not reached full convergence, it may display Label Bias.  

Known Issue: In complex contexts, the model tends to latch onto "Strong Tokens" like years (e.g., "2015" or "1887") rather than semantic answers.  

Conclusion: This version serves as a Proof of Concept (PoC). Future iterations would involve full-dataset training (3-5 epochs) to improve entity recognition and semantic accuracy.  

#### Getting Started  
Local Execution:  

Bash  
pip install -r requirements.txt  
python app.py  
Notebook: Open QA_Model_FineTuning.ipynb to view the training logs and data preparation steps.  
