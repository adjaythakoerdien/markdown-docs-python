FROM python:3.12

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app
COPY templates /code/app/templates
# CMD ["fastapi", "run", "app/main.py", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
CMD ["fastapi", "run", "app/main.py", "--port", "3013", "--proxy-headers"]
