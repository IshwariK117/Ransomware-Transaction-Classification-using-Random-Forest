# Ransomware-Transaction-Classification-using-Random-Forest

![Interface](https://github.com/IshwariK117/Ransomware-Transaction-Classification-using-Random-Forest/blob/main/ransomware%20SS.jpeg)

## Introduction

Developed a sophisticated system to identify ransomware transactions, focusing on distinguishing normal transactions from ransomware-related ones. Implemented using the Random Forest machine learning method after outperforming other models. Utilized a standard dataset with over 3,000 samples covering five ransomware families.

## Abstract

### Abstract of the Idea

Ransomware is a type of malicious software that restricts access to a victim's data until a ransom is paid. While some versions encrypt files, making them unreadable, others simply lock the device. In more advanced forms, known as crypto viral extortion, files are encrypted in a way that makes recovery without the decryption key nearly impossible. The whole ransomware economy revolves around cryptocurrency. Hence, the classification of normal and ransomware transactions plays a vital role in ransomware attack forensics. 

We aim to construct a sophisticated system capable of identifying ransomware transactions. We have performed a feasibility analysis of state-of-the-art machine learning models and found that <span style="background-color: yellow">Random Forest performs far better than other classification models</span>. For the aforementioned scenario, we have used a standard dataset with over 3,000 samples, focusing on five different types of ransomware families: Cerber, Locky, TeslaCrypt, Yakes, and Reveton. Hence, we are proposing a ransomware transaction classification model based on the <span style="background-color: yellow">Random Forest machine learning method</span>.

## Getting Started

To get started with the project, you will need to have a Google account and access to Google Colab. Follow the steps below to begin:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:
    ```bash
    git clone https://github.com/IshwariK117/Ransomware-Transaction-Classification-using-Random-Forest.git
    ```
2. **Open Google Colab**: Go to [Google Colab](https://colab.research.google.com/) and sign in with your Google account.
3. **Upload Notebooks**: Upload the notebooks from the cloned repository to your Google Colab environment.

## Data

The dataset used in this project contains over 3,000 samples covering five different ransomware families. You can find the dataset [here](https://github.com/Rmayalam/Ransomware_Paranoia/blob/main/Dataset.txt).

1. Cerber
2. Locky
3. TeslaCrypt
4. Yakes
5. Reveton

Each sample includes features that help in distinguishing between normal transactions and ransomware-related transactions.

## Methodology

The project utilizes the Random Forest machine learning method for classification. Random Forest was chosen after a thorough feasibility analysis and comparison with other machine learning models. It showed superior performance in terms of accuracy and robustness in identifying ransomware transactions.

## Results

The Random Forest model demonstrated high accuracy in classifying transactions as either normal or ransomware-related. The results indicate that this model is effective in the forensic analysis of ransomware attacks, providing a reliable tool for cybersecurity professionals.

## Contributing

Contributions to this repository are welcome! If you have a notebook or an improvement that you would like to share, please follow these steps:

1. **Fork the repository**
2. **Create a new branch** (`git checkout -b feature-branch`)
3. **Commit your changes** (`git commit -am 'Add new feature'`)
4. **Push to the branch** (`git push origin feature-branch`)
5. **Create a new Pull Request**
