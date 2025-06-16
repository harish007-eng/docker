FROM python:3-slim
COPY flask-api.py /
ENV FLASK_APP=flask-api.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
