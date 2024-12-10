FROM python:3.9

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    # Add any other dependencies here
# Install OpenCV
RUN pip install opencv-python

# Set the working directory in the container
WORKDIR /app

# Copy your project files into the container
COPY . .

# Expose a port if needed (for web apps, etc.)
# EXPOSE 8080

# Define the command to run when the container starts
CMD ["python", "your_script.py"]  # Replace with your script