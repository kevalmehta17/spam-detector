import pandas as pd

# Preprocessing File help to load and clean the dataset which is cruicial for the model training

def load_and_clean_data(file_path):
    # Load the dataset
    df = pd.read_csv(file_path,encoding="latin-1")
    df = df.iloc[:, :2] #select all rows and first two columns
    df.columns = ['label','message'] 
    df['label'] = df['label'].map({'ham':0, 'spam':1}) 
    df.dropna(inplace=True) #remove null values
    return df

if __name__ == "__main__":
    data = load_and_clean_data('../data/spam.csv')
    print(data.head())