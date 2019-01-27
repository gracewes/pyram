FROM python:3.6-stretch
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /app/
CMD ["python", "pyram.py"]
