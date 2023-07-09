# Use a base image with Python pre-installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the working directory
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose the port on which your Flask app runs (assuming it's 5000)
EXPOSE 5000

# Specify the command to run your Flask app
CMD ["python3", "app.py"]