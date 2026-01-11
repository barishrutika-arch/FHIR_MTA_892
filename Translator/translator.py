import uuid
import pandas as pd

df = pd.read_csv("sample_data.csv")

for _, row in df.iterrows():
    patient_id = str(uuid.uuid4())
    print(f"Creating Patient with UUID: {patient_id}")
