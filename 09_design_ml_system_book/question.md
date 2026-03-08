
# **Chapter 1: Overview of Machine Learning Systems**

**1. The "Google Translate" Leap:** * **Question:** In 2016, Google Translate saw more improvement in one year than in the previous 10 years combined. What changed in their system design? 

* **Answer:** They switched from phrase-based translation (rules) to **Multilingual Neural Machine Translation**. This moved the system from a rule-heavy architecture to an end-to-end ML architecture. 



**2. Defining Software 2.0:**

* 
**Question:** How does Andrej Karpathy's "Software 2.0" concept differ from traditional Software 1.0? 


* **Answer:** Software 1.0 is code written by humans (if-else, loops). Software 2.0 is defined by data; the "code" (parameters) is learned by the system through optimization (gradient descent). 



**3. When NOT to use ML:**

* 
**Question:** Give an example of a problem where ML is unnecessary (Over-engineering). 


* **Answer:** If the relationship is a simple lookup. Example: Mapping Zip Codes to States (like Airbnb does). A simple lookup table is faster and cheaper than a model. 



**4. Research vs. Production (Latency):**

* 
**Question:** Why is a model with 99% accuracy in research sometimes useless in production? 


* **Answer:** Because production cares about **Latency**. If a 99% accurate model takes 5 seconds to respond, users will leave. Production requires a trade-off between accuracy and speed. 



**5. Data-Dependent Complexity:**

* 
**Question:** Why are ML systems more "unique" compared to traditional software? 


* **Answer:** Because they are **data-dependent**. Two companies (e.g., Netflix and Amazon) can have the same goal (recommender system) but vastly different systems because their data and user behavior differ. 



**6. ML in Health Care (Interpretability):**

* **Question:** Discuss Geoffrey Hinton’s "Black Box AI Surgeon" scenario. Why is interpretability a requirement in industry? 


* **Answer:** Trust and Debugging. Even if an AI surgeon has a higher cure rate, users and doctors need to know *why* a decision was made to ensure safety and prevent bias. 



**7. Bias at Scale:**

* 
**Question:** Why is ML bias more dangerous than human bias? 


* **Answer:** Scale. A biased human affects a few people; a biased ML model (like the Berkeley credit score study) can discriminate against millions in milliseconds. 



**8. Real-world Example (Netflix/Uber):**

* 
**Question:** How does infrastructure play a role in ML? 


* 
**Answer:** Companies like Netflix and Uber spend more time on "ML Platforms" (Feature stores, Model stores) than on the algorithms themselves to ensure reliability at scale. 



**9. Learning from Data:**

* 
**Question:** What are the 5 core elements of an ML solution's capacity? 


* 
**Answer:** (1) Learn (2) complex patterns from (3) existing data to make (4) predictions on (5) unseen data. 



**10. [Programming] Latency Monitoring:**

* **Task:** Write a Python snippet to measure the latency of a model's prediction.
* **Answer:**
```python
import time
start_time = time.time()
prediction = model.predict(input_data)
latency = time.time() - start_time
print(f"Latency: {latency} seconds")

```


<br>
<br>

---

<br>
<br>

# **Chapter 2: Introduction to ML Systems Design**

**11. The Iterative Nature:**

* 
**Question:** Why is ML development called a "cycle" rather than a linear process? 


* 
**Answer:** Because evaluation often reveals data issues (like label noise or stale data), forcing you to go back to data collection or feature engineering. 



**12. Business Objective vs. ML Metric:**

* **Question:** Your model has high Precision/Recall, but the company is losing revenue. What is the issue? 


* **Answer:** A mismatch between the **ML Metric** and the **Business Objective**. The model might be recommending items people click on but don't buy. 



**13. Reliability in ML:**

* 
**Question:** What does "Reliability" mean for an ML system specifically? 


* 
**Answer:** The system should continue to work correctly even when faced with "hardware/software faults" or "human error" (like bad data input). 



**14. Scalability (Amazon Prime Day Example):**

* 
**Question:** What happened during Amazon's Prime Day failure regarding autoscaling? 


* 
**Answer:** Their autoscaling feature failed to handle the massive growth in requests, leading to a crash that cost $72M-$99M in just one hour. 



**15. Maintainability & Stakeholders:**

* 
**Question:** Who are the different stakeholders in an ML system, and why does that affect maintainability? 


* **Answer:** Data Scientists, ML Engineers, and DevOps/SREs. Maintainability ensures that even if the original author leaves, others can reproduce and update the model. 



**16. Adaptability (Data Shift):**

* 
**Question:** Why must an ML system be "Adaptable"? 


* **Answer:** To handle **Data Distribution Shifts**. The world changes (e.g., consumer trends), and the model must evolve without service interruption. 



**17. The "Startup" Growth Pattern:**

* 
**Question:** How does artifact management change when moving from 1 model to 8,000 models? 


* **Answer:** You can't monitor 8,000 models manually. You need **automated monitoring and retraining** pipelines. 



**18. Case Study: Ad Click Prediction:**

* 
**Question:** In the book's 13-step example of ad prediction, what happens if 99.99% of your data has negative labels? 


* **Answer:** The model will always predict "No Ad." You must collect more positive samples or use sampling techniques to fix the class imbalance. 



**19. Deciding to Build vs. Buy:**

* 
**Question:** Why do founders advise startups to avoid "Integration Hell"? 


* **Answer:** Selling to big tech with custom infrastructure is hard. Startups should focus on standard, clean infrastructure to move faster. 



**20. Resource Scaling (Vertical vs. Horizontal):**

* 
**Question:** What is the difference between Up-scaling and Down-scaling in ML? 


* 
**Answer:** Up-scaling increases resources (like 100 GPUs) for peaks (e.g., Black Friday), and Down-scaling reduces them to save costs when traffic is low. 



**21. Model Iteration (Stale Data):**

* 
**Question:** Why might a model perform well on 2-month-old test data but poorly on yesterday's data? 


* **Answer:** The model is **stale**. The underlying data patterns have changed, requiring a retrain on recent data. 



**22. Monica Rogati’s Hierarchy:**

* 
**Question:** Why is "Data Collection" at the bottom of the Data Science Hierarchy of Needs? 


* 
**Answer:** Without stable data collection and storage, you cannot build features, let alone train Deep Learning models. 



**23. Baseline Importance:**

* 
**Question:** Why should you always start with a "Simple Baseline"? 


* **Answer:** To prove that a complex ML model is actually adding value. If a simple heuristic (e.g., "always predict the most frequent class") performs similarly, you don't need a complex model. 



**24. [Programming] Baseline with Scikit-learn:**

* **Task:** Create a "Most Frequent" baseline classifier.
* **Answer:**
```python
from sklearn.dummy import DummyClassifier
# Create baseline
baseline = DummyClassifier(strategy='most_frequent')
baseline.fit(X_train, y_train)
print(f"Baseline Score: {baseline.score(X_test, y_test)}")

```



**25. Model Artifacts:**

* 
**Question:** What are the 4 main components of a "Model" in production? 


* 
**Answer:** (1) Model Definition (Code), (2) Parameters (Weights), (3) Hyperparameters, and (4) Dependencies (Python version, etc.). 

<br>

---
---

<br>
<br>
