# pull official base image
FROM python:3.11-bullseye

LABEL maintainer="Adeleke Oluwafemi"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 


# set the working directory
WORKDIR /app

# copy the source code
COPY . /app/



# install pip project dependencies
RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt


# expose ports
EXPOSE 8000


# run the application
