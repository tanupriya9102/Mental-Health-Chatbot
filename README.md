Mental Health Chatbot for Employee Mental Health System
OBJECTIVES:
The objectives of this project are as follows:


PHASE I(Completed):
Data Collection: Gather comprehensive historical data on employees, including demographic information, work-related factors (e.g., workload, job role, work hours), and mental health-related indicators (e.g., self-reported stress levels, absenteeism).
Data Preprocessing: Clean and preprocess the collected data, addressing issues such as missing values and duplicate values. This ensures the data is suitable for modelling.
Model Development: Build a BERT based model capable of predicting the likelihood of an employee experiencing mental health issues based on the selected features.
Classification: Classify the employee as suffering from Depression, Anxiety, Frustration or Stress.


PHASE II:
Incorporating a simple conversational agent using natural language processing techniques.
Song Recommendation based on the user's mood.
Integration of chatbot and the prediction model in a user friendly application for easy usage.


Part 1:Mental Health Chatbot
Intent Recognition and Text Processing:
A pre-trained neural network model analyzes the user's input and predicts the most likely intent based on patterns learned during training.
The input is tokenized into individual words, and each word is lemmatized to its base form. This processed input is then used to create a "bag of words" representation.
The "bag of words" is a binary vector indicating the presence or absence of specific words in the user's input. This representation allows the model to make predictions based on word patterns.

Model Prediction:
Utilizes a pre-trained neural network to predict the intent class associated with the user's input. The bag of words is fed into the neural network model ('chatbot_model.h5'), which outputs a probability distribution over the possible intent classes. The model selects the intent with the highest probability as the predicted intent.
Response Generation:
Provides contextually relevant responses based on the recognized intent. The chatbot selects a random response from a set of predefined responses associated with the predicted intent in the 'intents.json' file. This randomness adds variability to the bot's replies.
Part 2: Music Suggestion based on mood
Apply nlp algorithms for sentiment analysis on user responses and based on the mood detected suggest songs based on genres corresponding to user’s mood.



DATASET DESCRIPTION:

This dataset contains a collection of conversations related to mental health. It covers various conversational styles, such as casual chats, common questions about mental health, discussions on traditional therapy, and general advice for people dealing with depression or anxiety. The main purpose of the dataset is to train a chatbot model to simulate a therapist, providing empathetic and supportive responses to those seeking emotional assistance.
To train the model effectively, the dataset includes the concept of "intents," representing the core purpose behind a user's message. For instance, if a user expresses sadness, the corresponding intent would be labeled as "sad." Each intent is accompanied by sample messages (patterns) that align with that specific intent, along with corresponding responses that the chatbot should generate. By defining multiple intents, patterns, and responses, the model learns to recognize user intentions and generate appropriate and compassionate replies.

Key: "intents"
Value: This is an array containing a list of intents.
Each intent:
Key: "tag"
Value: This defines the intent category, such as “greeting” or “fact”.
Key: "patterns"
Value: This is an array containing user phrases that trigger the intent, for example, greetings like "Hi" or "Good morning".
Key: "responses"
Value: This is an array containing potential responses the chatbot can give depending on the user's specific phrase within the intent.
