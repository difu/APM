import os
import requests

apm_endpoint=os.getenv("APM_ENDPOINT")
apm_public_key=os.getenv("APM_PUBLICKEY")

apm_upload_endpoint_url="%s/20200101/observations/public-span?dataFormat=zipkin&dataFormatVersion=2&dataKey=%s" % (apm_endpoint, apm_public_key)


def http_transport(encoded_span):
    result = requests.post(
      #Construct a URL that communicate with Application Performance Monitoring
      apm_upload_endpoint_url,
      data=encoded_span,
      headers={'Content-Type': 'application/json'},
      )
    return result