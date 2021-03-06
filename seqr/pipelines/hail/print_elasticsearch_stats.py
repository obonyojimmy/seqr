from utils.run_annotation_utils import print_elasticsearch_stats

import os
import pip

pip.main(['install', 'elasticsearch'])
import elasticsearch


# to get the ip address, run  `kubectl describe pod elasticsearch-1019229749-vhghc`
ELASTICSEARCH_SERVICE_HOSTNAME = os.environ.get('ELASTICSEARCH_SERVICE_HOSTNAME', "10.48.0.105") #"elasticsearch-svc") #"localhost") #"k8solo-01")
ELASTICSEARCH_PORT = os.environ.get('ELASTICSEARCH_SERVICE_PORT', "30001") #"9200"
es = elasticsearch.Elasticsearch(ELASTICSEARCH_SERVICE_HOSTNAME, port=ELASTICSEARCH_PORT)

print_elasticsearch_stats(es)
