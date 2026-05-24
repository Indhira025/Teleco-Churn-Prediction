<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teleco Customer Churn Prediction | README</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #24292e;
            background: #f6f8fa;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        /* Header Section */
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 16px;
            padding: 40px;
            margin-bottom: 30px;
            color: white;
            text-align: center;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 15px;
        }

        .header h1 i {
            margin-right: 15px;
        }

        .header p {
            font-size: 1.2rem;
            opacity: 0.95;
            max-width: 700px;
            margin: 0 auto;
        }

        .badges {
            margin-top: 25px;
            display: flex;
            justify-content: center;
            gap: 12px;
            flex-wrap: wrap;
        }

        .badge {
            background: rgba(255,255,255,0.2);
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 0.85rem;
            font-weight: 500;
            display: inline-block;
        }

        /* Card Style */
        .card {
            background: white;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.08);
            border: 1px solid #e1e4e8;
        }

        .card h2 {
            font-size: 1.5rem;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
            display: inline-block;
        }

        .card h3 {
            font-size: 1.2rem;
            margin: 20px 0 12px 0;
            color: #1a1a2e;
        }

        .card h4 {
            font-size: 1rem;
            margin: 15px 0 8px 0;
            color: #667eea;
        }

        /* Grid Layout */
        .grid-2 {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .grid-3 {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .grid-4 {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }

        @media (max-width: 768px) {
            .grid-2, .grid-3, .grid-4 {
                grid-template-columns: 1fr;
            }
        }

        /* Feature List */
        .feature-list {
            list-style: none;
            padding: 0;
        }

        .feature-list li {
            padding: 10px 0;
            border-bottom: 1px solid #e1e4e8;
            display: flex;
            align-items: center;
        }

        .feature-list li:last-child {
            border-bottom: none;
        }

        .feature-list li i {
            color: #667eea;
            width: 28px;
            margin-right: 12px;
        }

        /* Table Styles */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }

        th, td {
            padding: 10px 12px;
            text-align: left;
            border-bottom: 1px solid #e1e4e8;
        }

        th {
            background: #f6f8fa;
            font-weight: 600;
        }

        tr:hover {
            background: #f8f9fa;
        }

        /* Code Block */
        pre {
            background: #f6f8fa;
            padding: 16px;
            border-radius: 8px;
            overflow-x: auto;
            font-size: 0.85rem;
            border: 1px solid #e1e4e8;
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
        }

        code {
            font-family: 'SF Mono', Monaco, 'Courier New', monospace;
            background: #f6f8fa;
            padding: 2px 6px;
            border-radius: 4px;
            font-size: 0.85rem;
        }

        /* Button */
        .btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            padding: 12px 24px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            margin: 10px 5px;
            transition: transform 0.2s;
            border: none;
            cursor: pointer;
        }

        .btn:hover {
            transform: translateY(-2px);
        }

        .btn-outline {
            background: transparent;
            border: 2px solid #667eea;
            color: #667eea;
        }

        .btn-outline:hover {
            background: #667eea;
            color: white;
        }

        /* Stats */
        .stat-box {
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 12px;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: 700;
            color: #667eea;
        }

        .stat-label {
            font-size: 0.85rem;
            color: #586069;
        }

        /* Result Boxes */
        .result-high-risk {
            background: #fee2e2;
            padding: 15px;
            border-radius: 12px;
            border-left: 4px solid #dc2626;
        }

        .result-low-risk {
            background: #dcfce7;
            padding: 15px;
            border-radius: 12px;
            border-left: 4px solid #16a34a;
        }

        .result-high-risk h3 {
            color: #dc2626;
            margin-top: 0;
        }

        .result-low-risk h3 {
            color: #16a34a;
            margin-top: 0;
        }

        /* Footer */
        .footer {
            text-align: center;
            padding: 30px;
            border-top: 1px solid #e1e4e8;
            margin-top: 30px;
            color: #586069;
        }

        /* Links */
        a {
            color: #667eea;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }
            .header {
                padding: 25px;
            }
            .header h1 {
                font-size: 1.8rem;
            }
        }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1><i class="fas fa-chart-line"></i> Teleco Customer Churn Prediction</h1>
            <p>AI-Powered Customer Retention Intelligence | Predict customer churn with 78% accuracy</p>
            <div class="badges">
                <span class="badge"><i class="fab fa-python"></i> Python 3.x</span>
                <span class="badge"><i class="fas fa-flask"></i> Flask</span>
                <span class="badge"><i class="fas fa-brain"></i> Scikit-learn</span>
                <span class="badge"><i class="fas fa-chart-bar"></i> XGBoost</span>
                <span class="badge"><i class="fab fa-github"></i> Open Source</span>
            </div>
        </div>

        <!-- Quick Links -->
        <div style="text-align: center; margin-bottom: 25px;">
            <a href="#overview" class="btn"><i class="fas fa-info-circle"></i> Overview</a>
            <a href="#installation" class="btn btn-outline"><i class="fas fa-download"></i> Installation</a>
            <a href="#models" class="btn btn-outline"><i class="fas fa-chart-simple"></i> Models</a>
            <a href="#api" class="btn btn-outline"><i class="fas fa-code"></i> API</a>
        </div>

        <!-- Overview Section -->
        <div class="card" id="overview">
            <h2><i class="fas fa-info-circle"></i> Project Overview</h2>
            <p>This project develops a machine learning web application that predicts whether a telecommunications customer will churn (leave the service). The application analyzes customer account details, demographics, subscribed services, and payment history to provide real-time churn predictions.</p>
            
            <div class="grid-3" style="margin-top: 20px;">
                <div class="stat-box">
                    <div class="stat-number">9</div>
                    <div class="stat-label">ML Models Evaluated</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">78.14%</div>
                    <div class="stat-label">Best Model Accuracy</div>
                </div>
                <div class="stat-box">
                    <div class="stat-number">&lt;2s</div>
                    <div class="stat-label">Prediction Time</div>
                </div>
            </div>
        </div>

        <!-- Key Features -->
        <div class="card">
            <h2><i class="fas fa-star"></i> Key Features</h2>
            <div class="grid-2">
                <ul class="feature-list">
                    <li><i class="fas fa-mobile-alt"></i> SIM Card Selection (Jio, Airtel, Vi, BSNL)</li>
                    <li><i class="fas fa-chart-line"></i> Real-time Churn Predictions</li>
                    <li><i class="fas fa-tachometer-alt"></i> 29 Input Features Analysis</li>
                    <li><i class="fas fa-cloud-upload-alt"></i> Live Deployment on Render</li>
                </ul>
                <ul class="feature-list">
                    <li><i class="fas fa-file-alt"></i> Comprehensive Data Preprocessing Pipeline</li>
                    <li><i class="fas fa-chart-bar"></i> 9 ML Models Comparison</li>
                    <li><i class="fas fa-chart-pie"></i> ROC-AUC Visualization</li>
                    <li><i class="fas fa-mobile"></i> Responsive Web Interface</li>
                </ul>
            </div>
        </div>

        <!-- Dataset -->
        <div class="card">
            <h2><i class="fas fa-database"></i> Dataset Description</h2>
            <div class="grid-2">
                <div>
                    <h3>Specifications</h3>
                    <table>
                        <tr><th>Attribute</th><th>Value</th></tr>
                        <tr><td>Total Records</td><td>7,043 customers</td></tr>
                        <tr><td>Features</td><td>21 columns</td></tr>
                        <tr><td>Target Variable</td><td>Churn (Yes/No)</td></tr>
                        <tr><td>Source</td><td>IBM / Kaggle</td></tr>
                    </table>
                </div>
                <div>
                    <h3>Feature Categories</h3>
                    <table>
                        <tr><th>Category</th><th>Features</th></tr>
                        <tr><td>Demographics</td><td>gender, SeniorCitizen, Partner, Dependents</td></tr>
                        <tr><td>Account</td><td>tenure, Contract, PaperlessBilling, PaymentMethod</td></tr>
                        <tr><td>Services</td><td>PhoneService, InternetService, Streaming, Security</td></tr>
                        <tr><td>Partner</td><td>Teleco_Partner (BSNL, Jio, Vodafone, Airtel)</td></tr>
                    </table>
                </div>
            </div>
        </div>

        <!-- Technology Stack -->
        <div class="card">
            <h2><i class="fas fa-cogs"></i> Technology Stack</h2>
            <div class="grid-3">
                <div>
                    <h3><i class="fab fa-python"></i> Backend</h3>
                    <ul class="feature-list">
                        <li>Python 3.x</li>
                        <li>Flask</li>
                        <li>Scikit-learn</li>
                        <li>XGBoost</li>
                        <li>Pandas & NumPy</li>
                        <li>Pickle</li>
                    </ul>
                </div>
                <div>
                    <h3><i class="fas fa-code"></i> Frontend</h3>
                    <ul class="feature-list">
                        <li>HTML5</li>
                        <li>CSS3 (Flex/Grid)</li>
                        <li>JavaScript</li>
                        <li>Font Awesome</li>
                    </ul>
                </div>
                <div>
                    <h3><i class="fas fa-cloud"></i> Deployment</h3>
                    <ul class="feature-list">
                        <li>Render.com</li>
                        <li>Gunicorn</li>
                        <li>Git & GitHub</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Models Performance -->
        <div class="card" id="models">
            <h2><i class="fas fa-chart-simple"></i> Model Performance Comparison</h2>
            <table>
                <thead>
                    <tr><th>Model</th><th>Accuracy</th><th>Precision (Churn)</th><th>Recall (Churn)</th></tr>
                </thead>
                <tbody>
                    <tr><td>KNN</td><td>69.6%</td><td>44%</td><td>71%</td></tr>
                    <tr><td>Naive Bayes</td><td>66.9%</td><td>42%</td><td>88%</td></tr>
                    <tr><td>Logistic Regression</td><td>76.0%</td><td>51%</td><td>81%</td></tr>
                    <tr><td>Decision Tree</td><td>73.4%</td><td>47%</td><td>51%</td></tr>
                    <tr><td>Random Forest</td><td>78.0%</td><td>56%</td><td>60%</td></tr>
                    <tr style="background:#f0f4ff;"><td><strong>AdaBoost</strong></td><td><strong>74.1%</strong></td><td><strong>49%</strong></td><td><strong>83%</strong></td></tr>
                    <tr><td>Gradient Boosting</td><td>74.5%</td><td>49%</td><td>80%</td></tr>
                    <tr><td><strong>XGBoost</strong></td><td><strong>78.1%</strong></td><td><strong>55%</strong></td><td><strong>75%</strong></td></tr>
                    <tr><td>SVM</td><td>77.3%</td><td>53%</td><td>76%</td></tr>
                </tbody>
            </table>
        </div>

        <!-- Final Model -->
        <div class="card">
            <h2><i class="fas fa-crown"></i> Final Model Selection</h2>
            <pre><code>lr = LogisticRegression(max_iter=1000)
model = AdaBoostClassifier(estimator=lr, n_estimators=5)
model.fit(x_train_scaled, y_train)</code></pre>
            <div class="grid-2" style="margin-top: 15px;">
                <div>
                    <h3>Confusion Matrix</h3>
                    <pre>                 Predicted
              No Churn  Churn
Actual No Churn    752    304
Actual Churn        61    292</pre>
                </div>
                <div>
                    <h3>Why AdaBoost?</h3>
                    <ul class="feature-list">
                        <li>Excellent recall for churn (83%)</li>
                        <li>Good balance of precision and recall</li>
                        <li>Effective with imbalanced data</li>
                        <li>Interpretable results</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Installation -->
        <div class="card" id="installation">
            <h2><i class="fas fa-download"></i> Installation & Setup</h2>
            <pre><code># Clone the repository
git clone https://github.com/yourusername/teleco-churn-prediction.git
cd teleco-churn-prediction

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Access at http://localhost:5000</code></pre>
        </div>

        <!-- Deployment -->
        <div class="card">
            <h2><i class="fas fa-rocket"></i> Deployment (Render)</h2>
            <pre><code># Build Command
pip install -r requirements.txt

# Start Command
gunicorn app:app

# Environment
Python 3.x</code></pre>
            <div class="grid-2" style="margin-top: 15px;">
                <div>
                    <h3>Required Files</h3>
                    <ul class="feature-list">
                        <li>app.py - Flask application</li>
                        <li>model.pkl - Trained model</li>
                        <li>standar_Scaler.pkl - Fitted scaler</li>
                        <li>columns.pkl - Feature names</li>
                        <li>requirements.txt - Dependencies</li>
                        <li>Procfile - Start command</li>
                        <li>templates/ - HTML templates</li>
                    </ul>
                </div>
                <div>
                    <h3>Live Demo</h3>
                    <p>The application is deployed and accessible online.</p>
                </div>
            </div>
        </div>

        <!-- API Documentation -->
        <div class="card" id="api">
            <h2><i class="fas fa-code"></i> API Documentation</h2>
            <h3>POST /api/predict</h3>
            <p>Send customer data to receive churn prediction</p>
            <pre><code>{
  "tenure": 24.5,
  "monthly_charges": 89.50,
  "total_charges": 2148.00,
  "senior_citizen": 0,
  "partner": "Yes",
  "dependents": "No",
  "contract": "Month-to-month"
}</code></pre>
            <h3>Response</h3>
            <pre><code>{
  "success": true,
  "prediction": 1,
  "churn": true,
  "confidence": 0.83,
  "message": "Customer will churn"
}</code></pre>
        </div>

        <!-- Challenges & Solutions -->
        <div class="card">
            <h2><i class="fas fa-exclamation-triangle"></i> Challenges & Solutions</h2>
            <div class="grid-2">
                <div>
                    <h3>Missing Values</h3>
                    <p><strong>Solution:</strong> Linear interpolation for TotalCharges</p>
                    
                    <h3>Class Imbalance (73/27)</h3>
                    <p><strong>Solution:</strong> SMOTE balancing to 4,118/4,118</p>
                    
                    <h3>Non-normal Distributions</h3>
                    <p><strong>Solution:</strong> Yeo-Johnson + Quantile Transformation</p>
                </div>
                <div>
                    <h3>Outliers</h3>
                    <p><strong>Solution:</strong> IQR capping (1.5× rule)</p>
                    
                    <h3>32 Features</h3>
                    <p><strong>Solution:</strong> Variance Threshold + P-value filtering → 29 features</p>
                    
                    <h3>Deployment</h3>
                    <p><strong>Solution:</strong> Gunicorn + Render with requirements.txt</p>
                </div>
            </div>
        </div>

        <!-- Sample Results -->
        <div class="card">
            <h2><i class="fas fa-chart-bar"></i> Sample Prediction Results</h2>
            <div class="grid-2">
                <div class="result-high-risk">
                    <h3><i class="fas fa-exclamation-triangle"></i> High Churn Risk</h3>
                    <p><strong>Tenure:</strong> 2 months | <strong>Contract:</strong> Month-to-month</p>
                    <p><strong>Monthly Charges:</strong> $95.50 | <strong>Payment:</strong> Electronic check</p>
                    <p><strong>Prediction:</strong> Customer will CHURN</p>
                </div>
                <div class="result-low-risk">
                    <h3><i class="fas fa-check-circle"></i> Low Churn Risk</h3>
                    <p><strong>Tenure:</strong> 60 months | <strong>Contract:</strong> Two year</p>
                    <p><strong>Monthly Charges:</strong> $45.00 | <strong>Payment:</strong> Credit card (auto)</p>
                    <p><strong>Prediction:</strong> Customer will STAY</p>
                </div>
            </div>
        </div>

        <!-- Project Structure -->
        <div class="card">
            <h2><i class="fas fa-folder-tree"></i> Project Structure</h2>
            <pre><code>teleco-churn-prediction/
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
└── logs/                           # Application logs</code></pre>
        </div>

        <!-- Data Preprocessing -->
        <div class="card">
            <h2><i class="fas fa-chart-line"></i> Data Preprocessing Pipeline</h2>
            <div class="grid-2">
                <div>
                    <h4>1. Missing Value Handling</h4>
                    <p>Linear interpolation for TotalCharges (11 missing values)</p>
                    
                    <h4>2. Variable Transformation</h4>
                    <p>Yeo-Johnson (tenure) | Quantile Transformation (charges)</p>
                    
                    <h4>3. Outlier Handling</h4>
                    <p>IQR capping (1.5× rule)</p>
                </div>
                <div>
                    <h4>4. Categorical Encoding</h4>
                    <p>One-Hot + Ordinal Encoding (Contract)</p>
                    
                    <h4>5. Feature Selection</h4>
                    <p>Variance Threshold + P-value filtering (p < 0.05)</p>
                    
                    <h4>6. Class Balancing & Scaling</h4>
                    <p>SMOTE | StandardScaler</p>
                </div>
            </div>
        </div>

        <!-- References -->
        <div class="card">
            <h2><i class="fas fa-book"></i> References</h2>
            <div class="grid-2">
                <div>
                    <ul class="feature-list">
                        <li><i class="fas fa-file-alt"></i> <a href="https://flask.palletsprojects.com/" target="_blank">Flask Documentation</a></li>
                        <li><i class="fas fa-brain"></i> <a href="https://scikit-learn.org/stable/" target="_blank">Scikit-learn Documentation</a></li>
                        <li><i class="fas fa-chart-bar"></i> <a href="https://xgboost.readthedocs.io/" target="_blank">XGBoost Documentation</a></li>
                    </ul>
                </div>
                <div>
                    <ul class="feature-list">
                        <li><i class="fas fa-cloud"></i> <a href="https://render.com/docs" target="_blank">Render Documentation</a></li>
                        <li><i class="fas fa-chart-line"></i> <a href="https://imbalanced-learn.org/" target="_blank">Imbalanced-learn Documentation</a></li>
                        <li><i class="fas fa-database"></i> <a href="#">IBM Telco Customer Churn Dataset</a></li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Future Enhancements -->
        <div class="card">
            <h2><i class="fas fa-microchip"></i> Future Enhancements</h2>
            <div class="grid-3">
                <div>
                    <h3>Model Improvements</h3>
                    <ul class="feature-list">
                        <li>Neural Networks (MLP, LSTM)</li>
                        <li>CatBoost, LightGBM</li>
                        <li>Voting / Stacking Ensemble</li>
                    </ul>
                </div>
                <div>
                    <h3>Application</h3>
                    <ul class="feature-list">
                        <li>Mobile App (React Native)</li>
                        <li>Prediction History</li>
                        <li>PDF/Excel Export</li>
                    </ul>
                </div>
                <div>
                    <h3>Deployment</h3>
                    <ul class="feature-list">
                        <li>Docker Containerization</li>
                        <li>Kubernetes Orchestration</li>
                        <li>CI/CD Pipeline</li>
                    </ul>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p><strong>Project By:</strong> R Indhira</p>
            <p><strong>Last Updated:</strong> April 2026</p>
            <p>
                <i class="fab fa-github"></i> <a href="#">GitHub Repository</a> &nbsp;|&nbsp;
                <i class="fas fa-external-link-alt"></i> <a href="#">Live Demo</a>
            </p>
            <p style="margin-top: 15px; font-size: 0.85rem;">
                <i class="fas fa-code"></i> Built with Python, Flask, Scikit-learn, and XGBoost
            </p>
        </div>
    </div>
</body>
</html>
