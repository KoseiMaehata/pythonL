import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image#画像を使うときに必要なもの
import time #sleepを使うため

st.title("Streamlit 入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1行目": [1,2,3,4],
    "2行目": [10,20,30,40] 
})

#dataframeはwriteと違い詳細設定が可能
st.write(df)
st.dataframe(df,width=100,height=100)
#ハイライト追加
st.dataframe(df.style.highlight_max(axis=0),width=100,height=100)

st.table(df.style.highlight_max(axis=0))

#magicコマンド
"""
# 章
## 節
### 項

、、、python

import streamlit as st

import numpy as np

import pandas as pd

、、、

"""

df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
st.write(df1)

st.line_chart(df1)#折れ線グラフ
st.area_chart(df1)#チャートには様々な種類がある

#map
df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.78],
    columns=["lat","lon"]
)
st.map(df2)

#インタラクティブなウィジェット
if st.checkbox("show image"):#返し値はtrue or falseが原則
    img = Image.open("sample.jpg")
    st.image(img, caption="slime",use_column_width=True)

option = st.selectbox(
    "あなたの好きな数字を教えてください。",
    list(range(1,11))
    )
"あなたの好きな数字は",option,"です。"

text = st.text_input("あなたの趣味を教えてください。")
"あなたの趣味は",text

text1 = st.slider("あなたの今の調子は?",0,100,50)#数字は最低値、最高値、初期値を表す
"コンディション",text1

#レイアウトを整える
##sidebar
text3 = st.sidebar.text_input("あなたの趣味は")
text4 = st.sidebar.slider("あなたの今の調子は",0,50,100)
"趣味は",text3,"で、コンディションは",text4

left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ内容を解く")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ内容を解く")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ内容を解く")

#ブレグレスバーの表示
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.1)#時間停止0.1秒
"done"


