# 1. Start from an official Python image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the dependencies file
COPY requirements.txt .

# 4. Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy ALL project files into the container
COPY . .

# 6. Expose the port that Flask is running on (defined in app.py)
EXPOSE 5000

# 7. Command to run the API when the container starts
CMD ["python", "app.py"]