FROM python:latest

ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg opus-tools bpm-tools
RUN python -m pip install --upgrade pip
RUN python -m pip install wheel Pyrogram TgCrypto
RUN python -m pip install pytgcalls ffmpeg-python psutil

RUN git clone https://github.com/mastermindvrtx/Riyuk-SingerVrtxBot.git && \
    cd Riyuk-SingerVrtxBot && \
    pip3 install -U -r requirements.txt

WORKDIR /Riyuk-SingerVrtxBot
CMD python3 main.py


