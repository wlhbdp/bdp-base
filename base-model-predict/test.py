import pandas as pd
import model_predict.predict_way as predict

if __name__ == '__main__':
    df = pd.read_csv("/Users/wlhbdp/sample.csv", nrows=1)
    print(df)
    print(predict.Predict.predict_by_joblib("xgb_fraud_score_model.pkl", df))
