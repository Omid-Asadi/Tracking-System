FROM tracking:1.1
MAINTAINER OmidAsadi
ENV DEBIAN_FRONTEND="noninteractive"

RUN apt update
RUN apt install python3-pip -y

RUN apt upgrade -y
RUN apt install apt-utils -y
RUN apt install net-tools
RUN apt install git -y

RUN mkdir /var/www/
RUN mkdir /var/www/tracking/
RUN mkdir /var/www/tracking/src/
RUN mkdir /var/www/tracking/venv/
WORKDIR /var/www/tracking/src/
RUN git clone https://github.com/Omid-Asadi/Tracking-System.git .
RUN mkdir /var/www/tracking/src/logs/


RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install python3.11 -y
RUN apt install python3-pip -y
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.11 1
RUN apt install python3.11-dev -y
RUN apt install python3.11-venv -y
RUN apt install python3.11-distutils -y
RUN apt install python3.11-gdbm -y
RUN apt install python3.11-tk -y
RUN apt install python3.11-lib2to3 -y


RUN apt install virtualenv -y
RUN virtualenv -p python3.11 /var/www/tracking/venv/
ENV PATH="/var/www/tracking/venv/bin:$PATH"
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "migrate"]