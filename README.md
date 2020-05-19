# Datadog Host to CSV

A small utility to retrieve a CSV containing all Datadog hosts [currently reporting](https://docs.datadoghq.com/api/v1/hosts/).

## Setting up your Python environment

Create a Python environment and install dependencies.

```bash
# Create a Python virtual environment
python3 -m venv env
# Activate the environment
. venv/bin/activate
# Install dependencies
pip install -r requirements.txt
```

## Usage

This utility can be used in to query the Datadog API and generate a CSV containing host metadata.

### Notes

- It currently retrieves a maximum of 1000 hosts; pagination has not been implemented.

- It only asserts whether the hosts is in AWS. At the moment it does not account for other cloud providers.

```bash
python hosts_to_csv.py
# Output:Output: 2020-05-19_10-01-03.csv
```
