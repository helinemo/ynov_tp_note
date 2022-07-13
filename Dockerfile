FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip



RUN pip install streamlit
RUN pip install -U Jinja2
RUN pip install pytest
RUN pip install joblib
RUN pip install sklearn

COPY . .

CMD streamlit run model_dashboard.py