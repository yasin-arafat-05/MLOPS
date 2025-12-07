import mlflow
import mlflow.sklearn
import seaborn as sns
from pprint import pprint
from mlflow import MlflowClient
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


#
# for traking artifact we need to track them like an url not file 
# if we give the tracking url then it will convert the file into url
#
mlflow.set_tracking_uri("http://127.0.0.1:5000")




# Load Wine dataset
wine = load_wine()
X = wine.data
y = wine.target



# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10, random_state=42)




# Define the params for RF model
max_depth = 10
n_estimators = 50



# Set the expriment name: 
mlflow.set_experiment('YT-MLOPS-Exp1')

with mlflow.start_run():
    rf = RandomForestClassifier(max_depth=max_depth, n_estimators=n_estimators, random_state=42)
    rf.fit(X_train, y_train)

    y_pred = rf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # ===== Which value we want to lock?? use this function to lock something =====
    mlflow.log_metric('accuracy', accuracy)
    
    # ============= log hyperparameter of model ==========
    mlflow.log_param('max_depth', max_depth)
    mlflow.log_param('n_estimators', n_estimators)

    # Creating a confusion matrix plot
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=wine.target_names, yticklabels=wine.target_names)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')

    # save plot
    plt.savefig("Confusion-matrix.png")

    # ======= log artifacts using mlflow / picture ========
    mlflow.log_artifact("Confusion-matrix.png")
    
    # log the file: file1.py 
    mlflow.log_artifact(__file__)

    # tags
    mlflow.set_tags({"Author": 'Yasin Arafat', "Project": "Wine Classification"})

    # =================== finally  Log the model ===================
    run_id = mlflow.active_run().info.run_id
    mlflow.sklearn.log_model(rf, "Random-Forest-Model")
    model_uri = f"runs:/{run_id}/Random-Forest-Model"
    register_model = mlflow.register_model(model_uri,"Wine-Classification-Model")
    
    client = MlflowClient()
    model_name = "Wine-Classification-Model"
    model_version = register_model.version
    
    # Adding tags
    client.set_model_version_tag(model_name,model_version,"Environment", "Development")
    client.set_model_version_tag(model_name,model_version,"Model", "Random-Forest")
    client.set_model_version_tag(model_name,model_version,"Notes", "Trained on Wine dataset with 10% test split")
    pprint(accuracy)
    
    
