import re
import urlparse


def get_url_param_mappings(response):
    match = re.search('/(.*\?)(\S*)', response)
    if match:
        return dict(urlparse.parse_qsl(match.groups()[1]))
    return {}