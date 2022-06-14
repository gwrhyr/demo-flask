# last upd by gwrhyr
# last upd on 2022/06/09
FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY ./app /app/
EXPOSE 5000
