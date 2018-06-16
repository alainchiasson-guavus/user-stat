# Run build python
FROM python:3

#Install curl in container.
RUN apt-get -y update && apt-get install -y curl

WORKDIR /usr/src/app

COPY . /usr/src/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["api.py"]
