import pandas as pd

def load_and_preprocess_data(filepath="fan_data.csv"):
    # Load data
    df = pd.read_csv(filepath)
    
    # Drop rows with missing critical columns
    df = df.dropna(subset=["F_state", "control_date", "control_time"])
    
    # Convert to datetime
    df["datetime"] = pd.to_datetime(df["control_date"] + " " + df["control_time"])
    
    # Feature engineering
    df["hour"] = df["datetime"].dt.hour
    df["minute"] = df["datetime"].dt.minute
    df["day_of_week"] = df["datetime"].dt.dayofweek
    df["control_from_encoded"] = df["control_from"].map({"A": 0, "R": 1})
    
    # Lag features
    df = df.sort_values("datetime")
    df["prev_state"] = df["F_state"].shift(1)
    df["prev_speed"] = df["F_speed"].shift(1)
    df["time_since_last"] = df["datetime"].diff().dt.total_seconds() / 60
    
    # Drop NA rows from lag features
    df = df.dropna()
    
    return df

if __name__ == "__main__":
    df = load_and_preprocess_data()
    print("Data preprocessing complete. Sample data:")
    print(df.head())