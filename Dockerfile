FROM python:3.9

RUN mkdir /code
WORKDIR /code
ADD bots/. /code/

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

CMD ["python", "search_keyword.py"]
