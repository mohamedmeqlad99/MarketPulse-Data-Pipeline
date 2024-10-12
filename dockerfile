FROM apache/airflow:2.7.1

# Copy the requirements file into the container
COPY requirements.txt /requirements.txt

# Install the required Python packages
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
RUN pip install --upgrade pip setuptools


# Copy your dags and requirements into the image
COPY requirements.txt /



# Set the entry point (this might already be set in the base image, so adjust as needed)
ENTRYPOINT ["/entrypoint"]

# Expose ports if necessary
EXPOSE 8080
