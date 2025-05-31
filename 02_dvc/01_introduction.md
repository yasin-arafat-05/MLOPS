## Topics:

- 01 Why we need DVC?
- 02 Why DVC Not git?
- 03 Working of  DVC along with  git

<br>

# `#01 Why we need DVC?`
<br>

### Scenario:
You are a data scientist working on a machine learning project to predict customer churn for a telecom company. Your pipeline includes the components mentioned in the transcription:
1. **Data Ingestion**: Fetch customer data (e.g., call logs, billing info) from an S3 bucket.
2. **Data Preprocessing**: Clean missing values and remove outliers.
3. **Feature Engineering**: Create features like average call duration or payment delays.
4. **Feature Selection**: Select the most predictive features using statistical tests.
5. **Model Training**: Train a classification model (e.g., random forest).
6. **Model Evaluation**: Evaluate metrics like precision, recall, and F1-score.

You’ve run **10 experiments** by tweaking preprocessing (e.g., Z-score vs. IQR for outliers), feature engineering (e.g., adding new features), and model parameters. Each experiment produces different artifacts (e.g., cleaned datasets, feature sets, models, and metrics). Your pipeline is dynamic, as the S3 data gets updated weekly by the engineering team, and you need to track these changes.

Your senior manager schedules a meeting and asks you to present the **best-performing model** and justify why it’s suitable for deployment. They also want to compare the current model’s performance (e.g., recall) with the previous experiment’s results to ensure improvements.

---

### Problem Faced by the Senior
During the meeting, the senior raises the following issues:
1. **Lack of Clarity on Experiments**:
   - You present the latest model’s recall (e.g., 0.85), but the senior asks, “What was the recall in the last experiment? How do I know this is better?”
   - You realize you didn’t systematically save or version the artifacts (e.g., metrics, datasets) from previous experiments, making it hard to retrieve past results.

2. **Inability to Reproduce Results**:
   - The senior asks you to reproduce the results of experiment #5, which had a promising F1-score. However, you can’t recall which dataset, features, or preprocessing steps were used.

3. **Dynamic Data Challenges**:
   - The S3 data was updated recently, and the senior is concerned that the new data might have impacted model performance. They ask, “Which version of the data was used for this model?”

4. **Business Decision Pressure**:
   - The senior needs to choose a model for deployment but wants to see a comparison of metrics (e.g., precision, recall) across all 10 experiments to ensure the best fit for the business (e.g., prioritizing recall to minimize missed churn predictions).

Without **data versioning** or a structured way to track experiments, you struggle to answer these questions confidently, risking delays in deployment and loss of trust from the senior.

<br>

# `#02 What DVC Why not git?`
<br>

- **Git Limitations** (as per the transcription):
  - **Storage Issue**: Git struggles with large files (e.g., 500 MB CSVs), causing repository bloat and slow operations.
  - **Inefficient for Data**: Git analyzes files line-by-line, which is inefficient for large binary or tabular data (e.g., millions of rows), increasing load and storage demands.
  - **Size Limits**: Git platforms (e.g., GitHub) impose file size limits (e.g., 100 MB), making it impractical for ML artifacts.
- **DVC Advantages**:
  - Handles large files by storing them in remote storage (e.g., S3) and tracking metadata in Git.
  - Efficiently versions data and artifacts without bloating the Git repository.
  - Integrates with Git to manage code and data versioning together.


<br>

# `#03 Working of  DVC along with  git`
<br>

#### **Temple Scenario Context**
- **Setting**: You’re responsible for managing items (phone, wallet, bag, shoes) for 20 people visiting a high-security temple. The temple has two counters:
  - **Counter 1**: Accepts phone, wallet, and bag (small, manageable items), issuing a token (ID1) for retrieval.
  - **Counter 2**: Accepts shoes (larger, separate items), issuing a unique token (ID2) for retrieval.
- **Rules**: Items are deposited with tokens, and upon return, the correct items are returned using these tokens to avoid mix-ups.
- **Challenge**: Without tokens, you’d struggle to match items to people, especially with frequent visitors and daily changes.

#### **Mapping to Git and DVC**
- **Git as Counter 1**:
  - **Role**: Git is like Counter 1, managing small, text-based items (code files like `.txt`, `.py`, `.gitignore`, libraries).
  - **Process**: When you make changes (e.g., add a line to a `.py` file), Git tracks these changes version by version (v1, v2, v3, v4). It commits the code efficiently, similar to depositing a phone or wallet.
  - **Limitation**: Git struggles with large files (e.g., 500 MB datasets), just as Counter 1 can’t handle shoes due to size and security constraints.

- **DVC as Counter 2**:
  - **Role**: DVC is like Counter 2, managing large datasets or artifacts (e.g., `data.csv`, `model.pkl`) that Git can’t handle.
  - **Process**: DVC assigns a unique token (e.g., ID1 for D1, ID2 for D2) to each data version, linking it to the corresponding code version in Git. For example:
    - Code version v1 is committed with data version D1 (token ID1).
    - Code version v2 is committed with data version D2 (token ID2), and so on.
  - **Storage**: DVC stores the actual large files in remote storage (e.g., S3), while Git tracks only the token (metadata), avoiding repository bloat.
### Chart: Temple Scenario Mapping Git and DVC Integration

```
+---------------------+
| Temple Visit (Theory) |
|                     |
|   +---------+       |
|   |  Git    |       |
|   |         |       |----> v1 -> D1  (Token ID1)
|   +---------+       |----> v2 -> D2  (Token ID2)
|    | Code   |       |----> v3 -> D3  (Token ID3)
|    | .txt   |       |----> v4 -> D4  (Token ID4)
|    | .gitignore|    |
|    | Library  |    |
+--------------------+
         |                  +---------+
         +----------------->|  DVC    |
                            |         |
                            |  Data   |
                            |  data2  |
                            +---------+
```

#### Chart Description:
- **Title**: "Temple Visit (Theory)" - Represents the overarching concept of managing items (code and data) with rules, similar to the temple’s security process.
- **Git Box**: 
  - Contains "Code", ".txt", ".gitignore", and "Library", symbolizing Git’s role in versioning small code files and configuration.
  - Git tracks versions of code (v1, v2, v3, v4) and commits changes, much like assigning a person’s items to Counter 1.
- **DVC Box**: 
  - Contains "Data" and "data2", representing DVC’s role in versioning large datasets or artifacts.
  - DVC links each code version (v1 to v4) to a corresponding data version (D1 to D4) using unique tokens (IDs), akin to Counter 2 managing shoes with tokens.
- **Arrows**: 
  - From Git to DVC, showing the flow where Git commits code versions, and DVC tracks associated data versions with unique identifiers.
  - From code elements to Git, indicating that Git manages these files.
  - From DVC to "data2", suggesting DVC handles multiple data versions or updates.

---

<br>

# `#Code Implementation:`

<br>

**1.** Create git repo and clone it in local.
**2.** Create mycode.py and add code to it. (It will save a csv file to a new data folder)
**3.** pip install dvc
**4.** "dvc init" (creates .dvcignore, .dvc)
**5.** mkdir S3
**6.** "dvc remote add -d myremote S3" (Like git, we need to tell remote repo, Here, we will use our local storage. Like git, we can add here remote storage).
**7.** "dvc add data/" (Track all the file that are present in data folder.We can also track a specific file.It will add the data folder into .gitignore file.And it will create data.dvc file. Where, It will track for which version of code which version of data is used). And(in .dvc/cache/files/md5 we will also see the id number)

**8.** "git status,git add ., git commit, git push"

**9.** "dvc status,dvc commit,dvc push"(After dvc push,there will add 2 files. One for data file another saved an unique token.)

**10.** After dvc push, let push S3 into git. 

---

**11.** Add new row in our data and check with dvc status.

**12.** 
- git log --oneline
- git checkout <code>  (go to data_version_1)
- dvc pull  (it will give the data_version_1 Data)

**come back to the letest branch:**
- git checkout main
- dvc pull















