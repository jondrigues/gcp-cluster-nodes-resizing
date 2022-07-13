from flask import escape
from pprint import pprint
from functions_framework import http
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

@http
def gcp_cluster_nodes_resizing(request):
    body_request = request.get_json(silent=True)

    project = body_request['project']
    location = body_request['location']
    cluster = body_request['cluster']
    node_pool = body_request['nodePool']
    node_count = body_request['nodeCount']

    name = "projects/{0}/locations/{1}/clusters/{2}/nodePools/{3}".format(project, location, cluster, node_pool)
    body = {"nodeCount": node_count}

    service = discovery.build('container', 'v1', credentials=GoogleCredentials.get_application_default())

    response = service.projects()\
        .locations()\
        .clusters()\
        .nodePools()\
        .setSize(name=name, body=body)\
        .execute()

    return str(response)
