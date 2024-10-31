import streamlit as st

from datetime import datetime
import yfinance as yf 
import matplotlib.pyplot as plt


st.write(":blue[Merhaba Sayfamiza] :red[**Hosgeldiniz**] :sunglasses:")


symbol = st.sidebar.text_input('Hisse Senedi', value='GOOGL')
st.title(symbol+ ' Grafik')
start_date = st.sidebar.date_input('Başlangıç Tarihi' ,value=datetime(2024,10,10))
end_date = st.sidebar.date_input('Bitiş Tarihi' ,value=datetime.now())


df = yf.download(symbol,start=start_date, end=end_date)
st.subheader('Hİsse Senedi Grafiği')
st.line_chart(df['Close'])


#col1, col2, col3 = st.columns([1,2,1])

#col1.markdown(":red[_Hosgeldiniz_]")






#progress_bar = col2.progress(0)

#check_button = col2.button("Kontrol")

#for perc_completed in range(100):
 
#   time.sleep(0.05)
    
#progress_bar.progress(perc_completed+1)
    
   
# col2.success("tamamlandi")

