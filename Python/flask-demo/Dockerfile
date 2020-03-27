FROM frolvlad/alpine-python3:latest

LABEL maintainer="1494136313@qq.com"

RUN /bin/sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add --no-cache python3-dev curl && \
    rm -rf /var/cache/apk/*

COPY ./requirements-base.txt .

RUN pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 install -r requirements-base.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ENV FLASK_APP=manage.py

ENV FLASK_ENV=development

EXPOSE 5000

WORKDIR /usr/local/src/flask-demo/

CMD ["flask","run","-h","0.0.0.0"]