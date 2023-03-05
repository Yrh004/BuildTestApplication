FROM python:3.11

# Expose Ports
EXPOSE 5849

# Setting Persistent data
VOLUME ["/data"]

# Running Python Applocation
CMD ["python3", main.py]