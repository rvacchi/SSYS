# start by pulling the python image
FROM python:3

WORKDIR /code

# copy the requirements file into the image
COPY requirements.txt .

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
CMD [ "python", "hello-world.py" ]



