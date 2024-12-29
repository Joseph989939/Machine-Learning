## Machine-Learning-Project
這個repository保存了我於機器學習相關知識學習期間完成的程式設計專案。
## Project Source Codes:
1. [Email address validator](https://github.com/Joseph989939/Machine-Learning-project/blob/main/email%20address%20validator/validEmailAddress_2.py)
    - 給定10個feature vector的條件，如email的字串中是否包含'@'，若有則給定數值1，若無則給定數值為0，每筆email經10個feature判斷後會有10個0或1的數值，以numpy array形式保存。另創造一組對應10個feature的權重(weight)，以numpy array形式保存。透由兩組numpy array所得分數來判斷該email是否為正確email格式，最後輸入validation data來驗證該模型的準確度
2. 爛番茄影評AI評價系統
   - 爛番茄是美國的一個電影及電視評論彙整網站，每部電影都有眾多用戶在上面留下他們對該部電影的評價，此project將能協助我們對某部電影的影評進行評價，判斷這些影評是好評或負評。主要透由將含有polarity.train (train data)中的每行影評字串tokenization，將每個token即其出現次數以dictionary形式儲存，如{feature(str):frequency(int)} 

