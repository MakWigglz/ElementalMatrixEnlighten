FROM python:3.9

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    # Add any other dependencies here
# Install OpenCV
RUN pip install opencv-python

# Set the working directory in the container
WORKDIR /app   # Copy the current directory contents into the container at /workspace
COPY . /workspace


# Copy your project files into the container
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt


# Expose a port if needed (for web apps, etc.)
# EXPOSE 8080   # Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "your_script.py"]  # Replace with your script  # Run app.py when the container launches
