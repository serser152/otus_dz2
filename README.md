# Python Web App

Last changes:
- changed Dockerfile
    - docker rebuild speedup when changes source files only

- changed src
    - train.py - trains model
    - model.save - model
    - main.py - process GET localhost/ with parametes

Quick test:
    
    - http://localhost/?age=61&sex=1&cp=0&trestbps=134&chol=234&fbs=0&restecg=0&thalach=145&exang=0&oldpeak=2.6&slope=1&ca=2&thal=0
    Result: {condition: 1}
    
    - http://localhost/?age=65&sex=1&cp=0&trestbps=138&chol=282&fbs=1&restecg=2&thalach=174&exang=0&oldpeak=1.4&slope=1&ca=1&thal=0
    Result: {condition: 0}
