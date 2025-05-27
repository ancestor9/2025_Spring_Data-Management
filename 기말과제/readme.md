## 기말과제(Term Paper)

#### 1. 제출기한 : 2025.6.12(목) 오후 13시 까지
#### 2. 점수 비중 : 기말(70%) + 중간(30%)
#### 3. 과제 제출 요구사항(Requirements)
- a. 가독성 있게 코드를 제출, 보고서를 제출 (notebook인 경우는 코드와 텍스트 셀을 적절히 사용 권장)
- b. 자료 확보는 [KOBACO 광고비 데이터셋 바로가기](https://adstat.kobaco.co.kr/mcr/portal/dataSet/mdssInfoPage.do?orderState=regDt&pageSize=10&pageIndex=1&searchItem=all&searchText=&datasetId=DS_MST_0000000257#)에서 3년치 2017,208,2019년도 merge
- c. 추출할 컬럼 selected_cols = ['A_001', 'A_003', 'A_006', 'A_007', 'A_016', 'A_019', 'A_027', 'B_03_026', 'B_03_027', 'C_01_001#1', 'C_01_001#2', 'C_01_024']
    - 'C_01_024' :  구매의향에 대한 6점 척도로 특정점수 이상은 구매, 미만은 비구매로 이진분류(Binary Classification)으로 문제를 재정의 하는 것을 추천 
- d. 자료 변환(Data Preprocessing)
    - 모든 자료는 코드매핑하라(decode) : 1,2 --> 남자, 여자  
    - 범주형자료와 수치형자료를 판단하여 정의하라
    - 결측치를 대체하라(missing value imputation)
    - 이상치를 제거하라
    - 특성공학을 통해 자료 scaling, 특성변수 추출(countevector 사용 등)
- e. Target 변수는 C_01_033("PPL 제품/서비스/장소 실제 구입/이용 여부")로 정의하라
- f. 훈련과 검증데이터를 무작위로 80:20 비율로 구분하여 검증데이터를 hold out하라
- g. 사이킷런의 [Gaussian Naive Bayes](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html) 알고리즘을 데이터에 fit(learn, train)하여 모델을 생성하라
- h. 검증데이터로 모델의 성능을 정확도(accuracy)와 confusion matrix를 생성하라
- i. 특성변수 추출은 자율적으로 하여 예측모형의 성능지표(accuracy)를 최대로 하게 하라

#### 4. 제출 방법 : e-class


[Machine Learning Process — Overview, quoted by Analytics Vidhya]

<img src ="https://miro.medium.com/v2/resize:fit:640/format:webp/1*dx5lJ2lm1XuDI7jVVIP4SQ.png">
