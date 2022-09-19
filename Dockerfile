FROM python:3.8
# setup environment variable
ENV DockerHOME=/web/app/django

# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

# copy whole project to your docker home directory.
COPY . $DockerHOME
# run this command to install all dependencies
RUN pip install -r requirements.txt
# port where the Django app runs

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangosandbox.wsgi:application"]