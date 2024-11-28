# MSTIP-

## Spam Email Classification Project 📧
This project focuses on developing an efficient and reliable spam email classification system. The dataset underwent rigorous cleaning, exploration, preprocessing, and model evaluation to ensure optimal performance.

### Key Steps and Findings
#### 1. Data Cleaning
1. Removed unnecessary columns and renamed the remaining ones to Target and Email.
2. Checked for missing values (none found) and identified 409 duplicate rows, which were removed.
3. Ensured the dataset was clean and ready for further analysis.

Outcome: A consistent and well-structured dataset served as the foundation for this project.

#### 2. EDA(Exploratory Data Analysis)
##### Spam vs. Ham Distribution:
* Ham (Non-Spam): 87.46%
* Spam: 12.54%
Noted a clear class imbalance.
###### Text Analysis:
* Spam emails are typically longer in terms of sentences, words, and characters.
###### Correlation findings:
* Strong relationships: num_char ↔ num_words and num_words ↔ num_sentence.
* Multicollinearity between num_char & num_words led to focusing on the num_char feature during modeling.
###### Visualizations:
* Pairplots revealed outliers and highlighted feature patterns.

Outcome: Extracted actionable insights that guided feature selection and improved model design.

#### 3. Data Preprocessing
Implemented a comprehensive text preprocessing function that:
* Lowercased all text.
* Tokenized words.
* Removed special characters, punctuation, and stop words.
* Applied stemming for word normalization.
* Created word clouds to visualize frequently used words in spam and ham emails.
* Identified the top 30 words in both categories.

Outcome: Transformed raw text into numerical data suitable for machine learning models.

#### 4. Model Building
##### Feature Extraction:
* Explored both Bag of Words and TF-IDF vectorizers for text representation.
##### Models Evaluated:
* Multinomial Naive Bayes (MNB): High precision and simplicity.
* K-Nearest Neighbors (KNN): Reliable but computationally expensive.
* Random Forest & Extra Trees Classifiers: Achieved high accuracy and precision.
##### Results Comparison:
* Using TF-IDF with max_features=5000:
* Multinomial Naive Bayes achieved 97% accuracy and a precision score of 1.0.
*Using TF-IDF with max_features=4000:
*Extra Trees Classifier excelled with the highest accuracy and precision.
##### Model Selection:
* While Extra Trees Classifier demonstrated marginally higher accuracy, Multinomial Naive Bayes was chosen for its:
* Precision (1.0), computational efficiency, and simplicity.
  
Outcome: Delivered a high-performing spam email classifier ready for real-world applications.

#### 5. Further Enhancements
* Ensemble Techniques: Explore advanced models like voting classifiers and stacking for further optimization.
* Scalability Testing: Evaluate performance on larger, more diverse datasets.
* Real-Time Application: Deploy the model for live spam detection systems.
