# 1) Use the Python/Alpine-Linux image matching your project's version
FROM python:3.12-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# 2) Install UV
RUN pip install uv

# 3) Source the virtual env and run uv sync to install the project
# Note: Alpine Linux uses the 'sh' shell, which uses '.' instead of 'source'.
# We use '--all-groups' to ensure the dev dependencies (like pytest) are installed.
RUN uv venv && \
    . .venv/bin/activate && \
    uv sync --all-groups

# 4) Run pytest
# This runs the tests automatically during the image build process. 
# If tests fail, the Docker build will fail (which is great for CI/CD pipelines!)
RUN . .venv/bin/activate && pytest

# 5) Ends with launching your project
# We use CMD to specify the default command when the container actually runs
CMD ["/bin/sh", "-c", ". .venv/bin/activate && python src/calculator/calculator.py"]