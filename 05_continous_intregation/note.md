<br>
<br>

# `# CI-Continous Intregration:`

<br>
<br>

**For making CI 1st make a folder like ".github/workflows/ci.yaml"**

```yaml

name: CI

# when the ci will be trigged when push and pull request came:
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main


jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'

      - name: Install dependencies
        run: pip install --no-cache-dir -r requirements.txt

      - name: Run tests
        run: pytest _test.py
```

---

# CI (Continuous Integration)

## What is CI?

**Continuous Integration (CI)** is a software practice where **code changes are automatically built and tested** every time a developer **pushes code or creates a pull request**.

👉 Goal:

* Catch bugs early
* Ensure new code doesn’t break existing code
* Maintain code quality automatically


## Popular CI Platforms / Services

These platforms run your tests automatically in the cloud:

* **GitHub Actions** → CI for GitHub repositories
* **GitLab CI/CD** → Built-in CI for GitLab
* **Jenkins** → Self-hosted, highly customizable CI tool
* **CircleCI** → Cloud-based CI service
* **Travis CI** → Older but still used CI service


## Types of Testing in CI

Common testing layers used in CI pipelines:

1. **Unit Testing**

   * Tests individual functions or small components
   * Fast and easy to run
   * Example: testing a function like `square(n)`

2. **Integration Testing**

   * Tests how multiple modules work together
   * Example: model + preprocessing pipeline

3. **System / End-to-End Testing**

   * Tests the full application flow
   * Example: API → model → response

4. **Regression Testing**

   * Ensures old features still work after new changes


## Testing Priority for ML Projects (Important ⭐)

For **Machine Learning projects**, the **first priority** should be:

### ✅ Unit Tests (Highest Priority)

Test:

* Data preprocessing functions
* Feature engineering logic
* Utility functions
* Model input/output shapes
* Loss function behavior

Example:

```python
def test_normalization():
    assert normalize([0, 10])[1] == 1.0
```


### 🔄 Integration Tests (Second Priority)

Test:

* Dataset → preprocessing → model pipeline
* Model loading & inference
* Training script execution (small dummy data)


### 🧪 Model Validation Tests (Optional in CI)

* Accuracy threshold checks
* Shape consistency checks
* NaN / Inf detection in outputs

⚠️ Full training is usually **NOT recommended** in CI (too slow).


## Why CI is Important for ML

* Prevents broken pipelines
* Ensures reproducible experiments
* Makes collaboration safer
* Detects data & code bugs early

## Summary

* CI = automatic build + test on every push/PR
* GitHub Actions is the most common CI tool today
* Unit tests are the **top priority** in ML CI
* CI keeps ML projects reliable and production-ready



