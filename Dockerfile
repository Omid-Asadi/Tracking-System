FROM tracking:1.0
MAINTAINER OmidAsadi
ENV DEBIAN_FRONTEND="noninteractive"

#RUN apt update
#RUN apt upgrade -y
#RUN apt full-upgrade
#RUN apt install apt-utils -y
#RUN apt install unzip
#RUN apt install net-tools
#RUN apt install git -y

#RUN mkdir /var/www/
#RUN mkdir /var/www/tracking/
#WORKDIR /var/www/tracking/
#RUN git clone https://github.com/Omid-Asadi/Tracking-System.git .


RUN apt install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update
RUN apt install python3.11 -y
RUN apt install python3-pip
RUN apt install -y python3.11-distutils
RUN apt install libmysqlclient-dev

#RUN mkdir /var/www/tracking/venv
#RUN pip install virtualenv
#RUN virtualenv -p python3.11 /var/www/tracking/venv
#ENV PATH="/var/www/tracking/venv/bin:$PATH"
#RUN pip install -r /var/www/tracking/requirements.txt
