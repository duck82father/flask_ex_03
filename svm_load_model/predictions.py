import joblib
import pandas as pd
import os
import time
from svm_model.models import Question
from svm_model.forms import QuestionForm, AnswerForm

cwd = os.getcwd()

# 저장된 모델 불러오기
loaded_model = joblib.load(os.path.join(cwd, "svm_load_model", "svm_model.pkl"))

def loader(three, blk):

    print(three, blk)

    # 새로운 데이터
    new_data = pd.DataFrame({
        '3P': [three],
        'BLK': [blk]
    })

    # 모델을 사용한 예측
    predictions = loaded_model.predict(new_data)

    print(predictions)
    
    return predictions

