import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
import joblib
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def load_data():
    df = pd.read_csv("fan_data.csv")
    df['datetime'] = pd.to_datetime(df['control_date'] + ' ' + df['control_time'])
    df['hour'] = df['datetime'].dt.hour
    df['is_awake'] = df['hour'].apply(lambda x: 1 if 8 <= x < 23 else 0)
    df['prev_state'] = df['F_state'].shift(1).fillna(0)
    df['hours_since_change'] = df['datetime'].diff().dt.total_seconds() / 3600
    return df.dropna()

def train_model():
    df = load_data()
    features = ['hour', 'is_awake', 'prev_state', 'hours_since_change']
    X = df[features]
    y = df['F_state']
    
    # Create pipeline with feature names preservation
    model = make_pipeline(
        StandardScaler(),
        GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
    )
    
    model.fit(X, y)
    
    # Save both model and feature names
    joblib.dump({
        'model': model,
        'feature_names': features
    }, 'fan_model_gb_v2.pkl')
    
    print(f"Model trained with {len(df)} samples. Test prediction:", 
          model.predict(pd.DataFrame([[14, 1, 0, 2]], columns=features)))

if __name__ == '__main__':
    train_model()