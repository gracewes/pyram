FROM python:3.6-stretch as Base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
#EXPOSE 5000
EXPOSE 80
COPY . /app/
CMD ["python", "pyram.py"]
