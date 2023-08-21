from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# 받은 데이터프레임에 대해 feature에 정규화를 한 후 train/test 셋을 나눠주고 반환하는 함수
def create_feature_target(df, split=0.2):
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split, random_state=0)
    std_scale = StandardScaler()
    std_scale.fit(X_train)
    X_train_std = std_scale.transform(X_train)
    X_test_std = std_scale.transform(X_test)
    return X_train_std, X_test_std, y_train, y_test

# 분류 평가함수
def clf_eval(y_test, pred):
    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred, average='macro')
    recall = recall_score(y_test, pred, average='macro')
    f1 = f1_score(y_test, pred, average='macro')
    conf_matrix = confusion_matrix(y_test, pred)
    class_report = classification_report(y_test, pred)
    print('<evaluate>')
    print('accuracy:', accuracy)
    print('precision:', precision)
    print('recall:', recall)
    print('f1:', f1)
    print("="*60)
    print('<confusion matrix>\n', conf_matrix)
    print("="*60)
    print('<class report>\n', class_report)
