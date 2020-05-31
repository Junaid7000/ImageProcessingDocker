FROM python:latest

COPY img_rainbow.jpeg ./
COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt
ADD ./test.py ./

CMD ["python", "test.py"]