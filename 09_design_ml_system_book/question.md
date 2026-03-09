
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


#### **Part 1: Data Communication & Protocols (REST, gRPC, & Formats)**

**1. What is the fundamental difference between REST and gRPC for ML service communication?**

* **REST (Representational State Transfer):** Primarily uses **JSON** over **HTTP 1.1**. It is text-based, making it easy for humans to read but "heavy" for machines because field names are repeated in every message. It follows a strict request-response pattern where the client must wait for a response before sending the next request.
* **gRPC (Google Remote Procedure Call):** Uses **Protocol Buffers (Protobuf)** over **HTTP 2.0**. Protobuf is a binary format, which is much smaller and faster to serialize/deserialize than JSON. HTTP 2.0 allows **multiplexing** (multiple requests over one connection) and **streaming**, which is ideal for sending large feature vectors in real-time.

**2. Why are Protocol Buffers (Protobuf) preferred over JSON for high-scale ML?**

* **Efficiency:** Because Protobuf is binary, it consumes significantly less bandwidth.
* **Strict Schema:** You must define a `.proto` file (schema) beforehand. This ensures that the client and server always agree on the data types, preventing runtime crashes due to "missing fields" or "wrong types" common in JSON.

**3. When should you use a Row-based format (CSV, Avro) versus a Column-oriented format (Parquet)?**

* **Row-based (Avro/CSV):** Best for **Write-intensive** tasks or when you need to access every column of a single record (e.g., logging a single transaction).
* 
**Column-oriented (Parquet):** Essential for **Read-intensive** ML training. It allows "Projection Pushdown," where the system only reads the specific columns (features) your model needs, saving massive I/O and time.



---

#### **Part 2: Data Movement & Architectures (Request vs. Event)**

**4. Explain Request-Driven vs. Event-Driven Architecture in ML Systems.**

* **Request-Driven (Synchronous):** A client (e.g., a web app) asks the model for a prediction and *waits* for the answer. If the model is slow, the app freezes. This creates **tight coupling**.
* **Event-Driven (Asynchronous):** Services communicate via a **Message Broker** (like Kafka). A service publishes an event (e.g., "UserUploadedImage"), and multiple ML models can "subscribe" and process that image whenever they are ready. This is **decoupled** and handles traffic spikes much better.

**5. What is "Integration Hell" in ML infrastructure?**

* This happens when a company builds too much custom, non-standard infrastructure. It becomes nearly impossible to integrate new third-party tools or models because everything is "hard-wired" for a specific environment. Using standard protocols like REST/gRPC and brokers like Kafka helps avoid this.



**6. What is the role of a Message Broker like Apache Kafka in an ML pipeline?**

* Kafka acts as a high-throughput, fault-tolerant buffer. It allows for **stream processing**, where data is consumed as it arrives. It also enables "Repayability," allowing you to re-run your model on old data if you find a bug.

---

#### **Part 3: Databases & Normalization (The Deep Dive)**

**7. Define Database Normalization (1NF, 2NF, 3NF).**

* **1NF (First Normal Form):** Each column contains atomic (indivisible) values, and there are no repeating groups.
* **2NF/3NF:** These forms remove partial and transitive dependencies, ensuring that every non-key column is strictly dependent on the primary key. This eliminates **data redundancy**.

**8. Why is Normalization good for Apps but potentially bad for ML?**

* Normalization is great for **Data Integrity** in apps (e.g., changing a user's address in one place updates it everywhere). However, for ML training, it requires expensive **SQL JOINs** between many tables, which can be extremely slow.



**9. What is "Denormalization" and when is it used?**

* Denormalization is the process of pre-joining tables into one large, "flat" table. We do this for ML to ensure **fast read performance** during training and real-time inference, sacrificing storage space for speed.

**10. What are the ACID properties in transactional databases?**

* **Atomicity:** All parts of a transaction succeed, or none do.
* **Consistency:** Data stays valid according to rules.
* **Isolation:** Transactions don't interfere with each other.
* **Durability:** Once committed, data is permanent even if the system crashes.

---

#### **Part 4: Storage Systems (OLTP vs. OLAP)**

**11. Detailed Difference: OLTP vs. OLAP.**

* **OLTP (Online Transaction Processing):** Optimized for many fast, small transactions (e.g., inserting a new order). Usually **Row-oriented** (Postgres, MySQL).
* **OLAP (Online Analytical Processing):** Optimized for complex, long-running queries over massive datasets (e.g., calculating the average user spend over 5 years). Usually **Column-oriented** (Snowflake, BigQuery).

**12. Why should you never train an ML model directly on a production OLTP database?**

* Running a heavy ML query (scanning millions of rows) can "lock" the database, preventing actual users from making purchases or logging in. Always use a read-replica or an OLAP warehouse for training.

**13. What is a "Data Warehouse" versus a "Data Lake"?**

* **Data Warehouse:** Stores highly structured, cleaned data for business analysis (OLAP).
* **Data Lake:** Stores raw, unstructured data (logs, images, JSON) in its original format. ML Engineers often use Data Lakes for "unstructured" deep learning data.

---

#### **Part 5: Data Processing Pipelines (ETL vs. ELT)**

**14. Compare ETL and ELT. Which one is better for modern ML?**

* **ETL (Extract, Transform, Load):** Data is cleaned *before* it reaches the database. It’s older and less flexible.
* **ELT (Extract, Load, Transform):** Data is loaded raw into the warehouse and transformed *using* the warehouse’s compute power. **ELT is better for ML** because it keeps raw data available for researchers to experiment with different "transformations" later.

**15. What is the "Online-Offline Feature Skew"?**

* This occurs when the code used to calculate a feature during training (e.g., in SQL) is different from the code used during real-time inference (e.g., in Java/Python). Even small differences in math can cause the model to fail in production.

**16. How does a "Feature Store" solve the Skew problem?**

* A Feature Store (like Tecton or Feast) acts as a single source of truth. It ensures that the same logic and data are used for both training (offline) and serving (online).

---

#### **Part 6: Data Quality & Performance**

**17. What is "Schema Enforcement"?**

* It is the process of rejecting data that doesn't match the expected format (e.g., receiving a string when you expect an integer). This prevents downstream model failures.

**18. What is "Data Poisoning"?**

* A security threat where an attacker injects malicious or biased data into the training set to "trick" the model into learning the wrong behavior.



**19. Why did Peter Norvig say, "We just have more data"?**

* He emphasized that for many problems (like Search or Translation), a large volume of high-quality data is more effective than a slightly better algorithm. This is the core of the **Data-Centric AI** movement.



**20. What is "Lambda Architecture"?**

* A design that handles massive data by combining a **Batch layer** (for historical accuracy) and a **Speed layer** (for real-time streaming), merging them at the **Serving layer**.

---

#### **Part 7: Advanced Practical Concepts**

**21. What are "Static" vs. "Dynamic" features?**

* **Static:** Rarely change (e.g., user's birthdate).
* **Dynamic:** Change constantly (e.g., user's current location or items in a shopping cart). Dynamic features usually require **stream processing**.

**22. How do you handle data that is too large for a single machine's RAM?**

* You use **sharding** (splitting the dataset) and **distributed training** (Data Parallelism), where multiple GPUs/machines train on different parts of the data simultaneously.



**23. Why is "Data Versioning" (DVC) critical?**

* Unlike code (Git), data is huge and changes often. DVC allows you to "tag" exactly which version of the dataset produced which model, ensuring your experiments are **reproducible**.

**24. What is the "Data Science Hierarchy of Needs"?**

* Proposed by Monica Rogati, it argues that you cannot do AI/ML until you have stable **Data Collection**, **Storage**, and **Cleaning** at the bottom of the pyramid.



**25. [Technical Scenario] How would you handle a sudden spike in traffic for a real-time model?**

* 
**Answer:** I would use an **Event-driven** system with a message broker (Kafka) to queue incoming requests so they don't overwhelm the model, and I would enable **Autoscaling** to spin up more model instances in the cloud.

<br>

---
---

<br>
<br>


