# Naive_Bayes_Classifier
This Python code is designed to perform breast cancer detection using a Naive Bayes classifier. It imports necessary libraries, preprocesses the dataset, trains the classifier, and evaluates its accuracy.
<!DOCTYPE html>
<html>
<head>
    <title> Breast Cancer Detection with Naive Bayes Classifier </title>
</head>
<body>

<h1> Breast Cancer Detection with Naive Bayes Classifier </h1>

<p> This Python code is designed to detect breast cancer using a Gaussian Naive Bayes classifier. It reads a breast cancer dataset from a CSV file, preprocesses the data, and trains the classifier to make predictions. The main output of this code is the accuracy of the classifier's predictions on a test dataset. </p>

<h2> How it Works </h2>

<ol>
    <li> The code imports necessary libraries, including NumPy, pandas, and Matplotlib. </li>
    <li> It defines an accuracy function to calculate the accuracy of model predictions. </li>
    <li> The <code>breastCancerPreparation()</code> function reads the dataset ('breastCancer2.csv'), preprocesses it, and prepares the data for training and testing. </li>
    <li> It splits the dataset into training and testing sets, with 25% of the data used for testing. </li>
    <li> The code trains a Gaussian Naive Bayes classifier on the training data. </li>
    <li> It uses the trained classifier to make predictions on the test data. </li>
    <li> The accuracy of the classifier's predictions is calculated and printed to the console. </li>
</ol>

<h2> Output </h2>

<p> The primary output of this code is the accuracy of the Naive Bayes classifier's predictions on the test dataset. The accuracy represents the percentage of correctly predicted cases in the test dataset. </p>

<h3> Example Output </h3>

<pre>
Naive Bayes Classifier Accuracy =:  96.50 %
</pre>

<p> The accuracy value may vary depending on the dataset and the random seed used for splitting the data, but it provides an evaluation of the classifier's performance in breast cancer detection. </p>

</body>
</html>
