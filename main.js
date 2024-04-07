let jsondata = require('./selfpractice.json');
let array = [
    [
      'What is Data Science',
      'What is Machine Learning',
      'What is Scientific Data',
      'What is Neural Networking',
      'What is Data Mining',
      'What is Feature Extraction',
      'What is Supervised Learning',
      'What is Unsupervised Learning',
      'What is Ensemble Learning',
      'What is Clustering',
      'What is Data Cleansing',
      'What is Model Evaluation',
      'What is Bias-Variance Tradeoff',
      'What is Hyperparameter Tuning',
      'What is Decision Tree'
    ],
    [
      'What is Data Engineering',
      'What is Data Management',
      'What is ETL',
      'What is Data Architecture',
      'What is Data Governance',
      'What is Data Integration',
      'What is Data Warehousing',
      'What is Data Quality',
      'What is Data Security',
      'What is Data Migration',
      'What is Data Governance Framework',
      'What is Data Profiling',
      'What is Data Storage',
      'What is Data Replication',
      'What is Data Modeling'
    ],
    [
      'What is Data Analysis',
      'What is Data Visualization',
      'What is Exploratory Data Analysis (EDA)',
      'What is Descriptive Statistics',
      'What is Inferential Statistics',
      'What is Correlation Analysis',
      'What is Regression Analysis',
      'What is Hypothesis Testing',
      'What is Time Series Analysis',
      'What is Predictive Modeling',
      'What is A/B Testing',
      'What is Cohort Analysis',
      'What is Data Mining'
    ]
  ]
let pick = [7,6,7]
let [fields,questions,mcqs,correct]=[['Data Science','Data Engineering','Data Analyst'],[[],[],[]],[],[]]
pick.forEach((total,index1) => {
    for (let index = 0; index < total; index++) {
        questions[index1].push(array[index1][Math.floor(Math.random() * array[index1].length)])
    }
});

for (let index = 0; index < fields.length; index++) {
    questions[index].forEach(question => {
        mcqs.push(jsondata.Questions[fields[index]][question]['options'])
        correct.push(jsondata.Questions[fields[index]][question]['correct_answer'])
    });
}

console.log(questions)
console.log(mcqs)
console.log(correct)