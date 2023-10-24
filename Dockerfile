# start from an official image
FROM python:3.10-slim

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src
    
# install our dependencies
# we use --system flag because we don't need an extra virtualenv
COPY Pipfile /opt/services/djangoapp/src/
RUN pip install pipenv &&\
    pipenv lock &&\
    pipenv install --system 

COPY swagger-ui /opt/services/djangoapp/swagger
    
# copy our project code
COPY . /opt/services/djangoapp/src
RUN cd ctk_container && python manage.py collectstatic --no-input -v 3

# expose the port 8000
EXPOSE 80

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "ctk_container", "--bind", ":80", "ctk_app.wsgi:application"]