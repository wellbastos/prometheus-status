From ubuntu:latest
 
RUN apt update && apt install git python3-pip -y

RUN mkdir /app

WORKDIR /app

ADD app/ /app

RUN pip3 install git+https://github.com/ABORGT/PylertAlertManager.git

RUN pip3 install -r requirements.txt

CMD [ "python3", "./promstatus.py" ]