import pandas as pd
import joblib
from datetime import datetime, timedelta

class FanNotifier:
    def __init__(self):
        saved = joblib.load('fan_model_gb_v2.pkl')
        self.model = saved['model']
        self.feature_names = saved['feature_names']
        self.last_action = None
        
    def predict_action(self, current_time, last_change_time, current_state=0):
        hours_inactive = (current_time - last_change_time).total_seconds() / 3600
        
        # Create proper DataFrame with feature names
        input_data = pd.DataFrame([[
            current_time.hour,
            1 if 8 <= current_time.hour < 23 else 0,
            current_state,
            hours_inactive
        ]], columns=self.feature_names)
        
        # Guaranteed notifications
        if hours_inactive > 2 and current_state == 0:
            return "ON", 0.95
        elif hours_inactive > 3 and current_state == 1:
            return "OFF", 0.90
            
        # Model prediction
        pred = self.model.predict(input_data)[0]
        proba = self.model.predict_proba(input_data)[0][1]
        return ("ON" if pred == 1 else "OFF"), proba

    def get_notification(self, current_time=None, last_change_time=None):
        current_time = current_time or datetime.now()
        last_change_time = last_change_time or (current_time - timedelta(hours=2.5))
        
        action, confidence = self.predict_action(current_time, last_change_time)
        
        if confidence > 0.6:
            msg = f"🔔 Fan should be turned {action} (Confidence: {confidence:.0%})"
            self.last_action = (current_time, action)
            return msg
        return "No action needed (normal operation)"

if __name__ == '__main__':
    notifier = FanNotifier()
    
    # Test cases
    tests = [
        ("Morning activation (OFF->ON)", datetime(2025,5,10,10,0), datetime(2025,5,10,7,30), 0),
        ("Afternoon maintain (ON->ON)", datetime(2025,5,10,15,0), datetime(2025,5,10,13,0), 1),
        ("Evening off (ON->OFF)", datetime(2025,5,10,23,0), datetime(2025,5,10,20,0), 1),
        ("Current time prediction", datetime.now(), datetime.now() - timedelta(hours=3), 0)
    ]
    
    for desc, curr, last, state in tests:
        print(f"\n{desc} at {curr.strftime('%H:%M')}:")
        print(notifier.get_notification(curr, last))
        