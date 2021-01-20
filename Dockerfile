FROM python:3.6
MAINTAINER name  onmouse@163.com
WORKDIR /app
ADD . /app
RUN pip install --upgrade pip && pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
EXPOSE 5000
CMD python3 ./run.py
