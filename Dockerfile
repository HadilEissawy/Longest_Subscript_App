FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . ./

# Make the command line argument accessible
ENTRYPOINT ["python", "L_Subscript.py"]