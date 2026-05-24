<div align="center">
  <h1>📊 Teleco Customer Churn Prediction</h1>
  <p><strong>AI-Powered Customer Retention Intelligence | Predict customer churn with 78% accuracy</strong></p>
  
  <p>
    <img src="https://img.shields.io/badge/Python-3.x-blue?style=flat-square">
    <img src="https://img.shields.io/badge/Flask-Framework-green?style=flat-square">
    <img src="https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat-square">
    <img src="https://img.shields.io/badge/XGBoost-Boosting-red?style=flat-square">
    <img src="https://img.shields.io/badge/SMOTE-Balancing-purple?style=flat-square">
  </p>
</div>

<hr>

<h2>📌 Project Overview</h2>
<p>This project develops a machine learning web application that predicts whether a telecommunications customer will churn (leave the service). The application analyzes customer account details, demographics, subscribed services, and payment history to provide real-time churn predictions.</p>

<hr>

<h2>📈 Project Statistics</h2>
<table>
  <tr>
    <th>Metric</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>🤖 ML Models Evaluated</td>
    <td>9</td>
  </tr>
  <tr>
    <td>🎯 Best Model Accuracy</td>
    <td>78.14%</td>
  </tr>
  <tr>
    <td>👥 Customer Records</td>
    <td>7,043</td>
  </tr>
  <tr>
    <td>⚡ Prediction Time</td>
    <td>&lt; 2 seconds</td>
  </tr>
</table>

<hr>

<h2>✨ Key Features</h2>
<table>
  <tr>
    <td>✅ SIM Card Selection (Jio, Airtel, Vi, BSNL)</td>
    <td>✅ Real-time Churn Predictions</td>
  </tr>
  <tr>
    <td>✅ 29 Input Features Analysis</td>
    <td>✅ Live Deployment on Render</td>
  </tr>
  <tr>
    <td>✅ Comprehensive Data Preprocessing Pipeline</td>
    <td>✅ 9 ML Models Comparison</td>
  </tr>
  <tr>
    <td>✅ ROC-AUC Visualization</td>
    <td>✅ Responsive Web Interface</td>
  </tr>
</table>

<hr>

<h2>📊 Dataset Description</h2>
<table>
  <tr>
    <th>Attribute</th>
    <th>Value</th>
  </tr>
  <tr>
    <td>Total Records</td>
    <td>7,043 customers</td>
  </tr>
  <tr>
    <td>Features</td>
    <td>21 columns</td>
  </tr>
  <tr>
    <td>Target Variable</td>
    <td>Churn (Yes/No)</td>
  </tr>
  <tr>
    <td>Source</td>
    <td>IBM / Kaggle</td>
  </tr>
</table>

<h3>Feature Categories</h3>

<h4>👤 Demographics</h4>
<ul>
  <li>gender</li>
  <li>SeniorCitizen</li>
  <li>Partner</li>
  <li>Dependents</li>
</ul>

<h4>💳 Account Information</h4>
<ul>
  <li>tenure</li>
  <li>Contract</li>
  <li>PaperlessBilling</li>
  <li>PaymentMethod</li>
  <li>MonthlyCharges</li>
  <li>TotalCharges</li>
</ul>

<h4>🌐 Services</h4>
<ul>
  <li>PhoneService</li>
  <li>MultipleLines</li>
  <li>InternetService</li>
  <li>OnlineSecurity</li>
  <li>OnlineBackup</li>
  <li>DeviceProtection</li>
  <li>TechSupport</li>
  <li>StreamingTV</li>
  <li>StreamingMovies</li>
</ul>

<h4>📱 Partner/Circle</h4>
<ul>
  <li>Teleco_Partner (BSNL, Reliance Jio, Vodafone, Airtel)</li>
</ul>

<hr>

<h2>🛠️ Technology Stack</h2>
<table>
  <tr>
    <th>Backend</th>
    <th>Frontend & Deployment</th>
  </tr>
  <tr>
    <td>Python 3.x</td>
    <td>HTML5 / CSS3</td>
  </tr>
  <tr>
    <td>Flask</td>
    <td>JavaScript</td>
  </tr>
  <tr>
    <td>Scikit-learn</td>
    <td>Render.com</td>
  </tr>
  <tr>
    <td>XGBoost</td>
    <td>Gunicorn</td>
  </tr>
  <tr>
    <td>Pandas &amp; NumPy</td>
    <td>Git &amp; GitHub</td>
  </tr>
  <tr>
    <td>Imbalanced-learn (SMOTE)</td>
    <td>Font Awesome</td>
  </tr>
</table>

<hr>

<h2>🔄 Data Preprocessing Pipeline</h2>

<h4>1️⃣ Missing Values</h4>
<p>Linear interpolation for <code>TotalCharges</code></p>

<h4>2️⃣ Data Transformation</h4>
<ul>
  <li>Yeo-Johnson Transformation (tenure)</li>
  <li>Quantile Transformation (charges)</li>
</ul>

<h4>3️⃣ Outlier Handling</h4>
<p>IQR capping (1.5× rule)</p>

<h4>4️⃣ Encoding</h4>
<ul>
  <li>One-Hot Encoding</li>
  <li>Ordinal Encoding</li>
</ul>

<h4>5️⃣ Feature Selection</h4>
<ul>
  <li>Variance Threshold</li>
  <li>P-value filtering (<code>p &lt; 0.05</code>)</li>
</ul>

<h4>6️⃣ Class Balancing</h4>
<p>SMOTE balancing (<code>4,118 samples per class</code>)</p>

<h4>7️⃣ Scaling</h4>
<p>StandardScaler (z-score normalization)</p>

<hr>

<h2>🤖 Model Performance Comparison</h2>
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Accuracy</th>
      <th>Precision (Churn)</th>
      <th>Recall (Churn)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>KNN</td><td>69.6%</td><td>44%</td><td>71%</td></tr>
    <tr><td>Naive Bayes</td><td>66.9%</td><td>42%</td><td>88%</td></tr>
    <tr><td>Logistic Regression</td><td>76.0%</td><td>51%</td><td>81%</td></tr>
    <tr><td>Decision Tree</td><td>73.4%</td><td>47%</td><td>51%</td></tr>
    <tr><td>Random Forest</td><td>78.0%</td><td>56%</td><td>60%</td></tr>
    <tr style="background:#f0f0f0;"><td><strong>AdaBoost (Selected)</strong></td><td><strong>74.1%</strong></td><td><strong>49%</strong></td><td><strong>83%</strong></td></tr>
    <tr><td>Gradient Boosting</td><td>74.5%</td><td>49%</td><td>80%</td></tr>
    <tr><td><strong>XGBoost</strong></td><td><strong>78.1%</strong></td><td><strong>55%</strong></td><td><strong>75%</strong></td></tr>
    <tr><td>SVM</td><td>77.3%</td><td>53%</td><td>76%</td></tr>
  </tbody>
</table>

<hr>

<h2>🏆 Final Model Selection</h2>

<pre><code>from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import AdaBoostClassifier

lr = LogisticRegression(max_iter=1000)

model = AdaBoostClassifier(
    estimator=lr,
    n_estimators=5
)

model.fit(x_train_scaled, y_train)
</code></pre>

<h3>📉 Confusion Matrix</h3>
<pre>
                 Predicted
              No Churn  Churn

Actual No Churn    752    304
Actual Churn        61    292
</pre>

<h3>✅ Why AdaBoost?</h3>
<ul>
  <li>Excellent recall for churn prediction (83%)</li>
  <li>Good balance of precision and recall</li>
  <li>Effective with imbalanced data</li>
  <li>Interpretable results</li>
</ul>

<hr>

<h2>⚙️ Installation &amp; Setup</h2>

<pre><code># Clone the repository
git clone https://github.com/yourusername/teleco-churn-prediction.git

# Move into project directory
cd teleco-churn-prediction

# Create virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
</code></pre>

<h3>🌐 Access Application</h3>
<pre>http://localhost:5000</pre>

<hr>

<h2>📦 requirements.txt</h2>
<pre><code>flask==2.3.0
numpy==1.24.3
pandas==2.0.1
scikit-learn==1.2.2
xgboost==1.7.6
imbalanced-learn==0.10.1
gunicorn==20.1.0
</code></pre>

<hr>

<h2>🚀 Deployment on Render</h2>

<h4>Build Command</h4>
<pre><code>pip install -r requirements.txt</code></pre>

<h4>Start Command</h4>
<pre><code>gunicorn app:app</code></pre>

<h3>📁 Required Files</h3>
<ul>
  <li><code>app.py</code> → Flask application</li>
  <li><code>model.pkl</code> → Trained model</li>
  <li><code>standar_Scaler.pkl</code> → Fitted scaler</li>
  <li><code>columns.pkl</code> → Feature names</li>
  <li><code>requirements.txt</code> → Dependencies</li>
  <li><code>Procfile</code> → Start command</li>
  <li><code>templates/</code> → HTML templates</li>
  <li><code>static/</code> → CSS and images</li>
</ul>

<hr>

<h2>🔌 API Documentation</h2>

<h4>POST <code>/api/predict</code></h4>

<p><strong>Request Body:</strong></p>
<pre><code>{
  "tenure": 24.5,
  "monthly_charges": 89.50,
  "total_charges": 2148.00,
  "senior_citizen": 0,
  "partner": "Yes",
  "dependents": "No",
  "contract": "Month-to-month"
}
</code></pre>

<p><strong>Response:</strong></p>
<pre><code>{
  "success": true,
  "prediction": 1,
  "churn": true,
  "confidence": 0.83,
  "message": "Customer will churn"
}
</code></pre>

<hr>

<h2>⚠️ Challenges &amp; Solutions</h2>
<table>
  <tr>
    <th>Challenge</th>
    <th>Solution</th>
  </tr>
  <tr>
    <td>Missing Values</td>
    <td>Linear interpolation</td>
  </tr>
  <tr>
    <td>Class Imbalance (73/27)</td>
    <td>SMOTE balancing</td>
  </tr>
  <tr>
    <td>Non-normal Distributions</td>
    <td>Yeo-Johnson + Quantile Transformation</td>
  </tr>
  <tr>
    <td>Outliers</td>
    <td>IQR capping</td>
  </tr>
  <tr>
    <td>32 Features</td>
    <td>Variance Threshold + P-value filtering</td>
  </tr>
  <tr>
    <td>Deployment</td>
    <td>Gunicorn + Render</td>
  </tr>
</table>

<hr>

<h2>📈 Sample Prediction Results</h2>

<h3>⚠️ High Churn Risk</h3>
<table>
  <tr><td>Tenure</td><td>2 months</td></tr>
  <tr><td>Contract</td><td>Month-to-month</td></tr>
  <tr><td>Monthly Charges</td><td>$95.50</td></tr>
  <tr><td>Payment Method</td><td>Electronic check</td></tr>
  <tr><td><strong>Prediction</strong></td><td><strong>Customer will CHURN</strong></td></tr>
</table>

<h3>✅ Low Churn Risk</h3>
<table>
  <tr><td>Tenure</td><td>60 months</td></tr>
  <tr><td>Contract</td><td>Two year</td></tr>
  <tr><td>Monthly Charges</td><td>$45.00</td></tr>
  <tr><td>Payment Method</td><td>Credit card (auto)</td></tr>
  <tr><td><strong>Prediction</strong></td><td><strong>Customer will STAY</strong></td></tr>
</table>

<hr>

<h2>📁 Project Structure</h2>
<pre><code>teleco-churn-prediction/
│
├── app.py                          # Flask application
├── main.py                         # Pipeline orchestration
├── all_models.py                   # 9 ML models
├── feature_scalling.py             # Scaling module
├── var_transformation.py           # Transformation
├── cat_to_num.py                   # Categorical encoding
├── filter_methods.py               # Feature selection
├── Interpolation_Techniques.py     # Missing values
├── logging_code.py                 # Logging config
├── model.pkl                       # Trained AdaBoost model
├── standar_Scaler.pkl              # Fitted scaler
├── columns.pkl                     # Feature names
├── requirements.txt                # Dependencies
├── Procfile                        # Deployment config
├── templates/
│   └── index.html                  # Web interface
├── static/
│   └── images/                     # SIM card images
└── logs/                           # Application logs
</code></pre>

<hr>

<h2>📚 References</h2>
<ul>
  <li><a href="https://flask.palletsprojects.com/">Flask Documentation</a></li>
  <li><a href="https://scikit-learn.org/stable/">Scikit-learn Documentation</a></li>
  <li><a href="https://xgboost.readthedocs.io/">XGBoost Documentation</a></li>
  <li><a href="https://render.com/docs">Render Documentation</a></li>
  <li><a href="https://imbalanced-learn.org/">Imbalanced-learn Documentation</a></li>
</ul>

<hr>

<h2>👨‍💻 Project By</h2>
<p><strong>R Indhira</strong></p>
<p>📅 Last Updated: April 2026</p>

<hr>

<h2>🔗 Project Links</h2>
<ul>
  <li>📦 <a href="#">GitHub Repository</a></li>
  <li>🌐 <a href="#">Live Demo</a></li>
</ul>

<hr>

<div align="center">
  <p>Built with ❤️ using Python, Flask, Scikit-learn, and XGBoost</p>
</div>
