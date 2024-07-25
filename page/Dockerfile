FROM python:3.10

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip3 install numpy
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install -r /code/requirements.txt
RUN pip install python-dotenv

COPY . /code

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]