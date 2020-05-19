from datadog import initialize, api
from os import environ
from sys import argv
from datetime import datetime
import csv

# This is not essential; see https://github.com/DataDog/datadogpy#environment-variables
OPTIONS = {
    'api_key': environ['DD_API_KEY'],
    'app_key': environ['DD_APP_KEY'],
    'api_host': environ['DD_SITE_URL']
}
# Initialize the Datadog API client.
initialize(**OPTIONS)


def get_all_hosts(count):
    # API returns a maximum of 1000 hosts.
    return api.Hosts.search(count=1000)


def get_host_details(host):
    # Keys should correspond to fieldnames.
    return {
        'hostname': host['host_name'],
        'last_reported_time': host['last_reported_time'],
        'agent': 'agent' in host['sources'],
        'apm': 'trace' in host['apps'],
        'aws': 'aws' in host['apps'],
        'datadog_tags': host['tags_by_source']['Datadog']
    }


def get_csv_writer(file):
    fieldnames = ['hostname', 'last_reported_time',
                  'agent', 'apm', 'aws', 'datadog_tags']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    return writer


def hosts_to_csv():
    # API returns a maximum of 1000 hosts.
    all_hosts = get_all_hosts(count=1000)
    filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.csv'
    with open(filename, mode='w') as csv_file:
        writer = get_csv_writer(csv_file)
        for host in all_hosts['host_list']:
            writer.writerow(get_host_details(host))
    print('Output: ' + filename)


hosts_to_csv()
