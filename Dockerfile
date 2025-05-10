# Use a slim Debian Bookworm image with Python 3.12
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Install system dependencies for WeasyPrint
RUN apt-get update && apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libgdk-pixbuf-2.0-0 \
    libharfbuzz0b \
    libfontconfig1 \
    python3-dev \
    gcc \
    g++ \
    libc-dev \
    libffi-dev \
    zlib1g-dev \
    libjpeg-dev \
    libopenjp2-7-dev \
    libwebp-dev \
    && rm -rf /var/lib/apt/lists/* \
    && ldconfig

# Debug: Verify libgobject-2.0-0 is installed
RUN ldconfig -p | grep libgobject || echo "libgobject not found" && \
    find /usr/lib -name libgobject-2.0.so* || echo "libgobject file not found"

# Copy requirements.txt
COPY . .

# Install Python dependencies, building WeasyPrint from source
RUN pip install -r requirements.txt

# Copy test script
COPY test_weasyprint.py .

# Set LD_LIBRARY_PATH to ensure libraries are found
ENV LD_LIBRARY_PATH=/usr/lib:/usr/lib/x86_64-linux-gnu

EXPOSE 5000

# Run test script
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
