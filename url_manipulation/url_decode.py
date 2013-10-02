import re
import urlparse

""" Url parsing utilities """


def get_url_param_mappings(response):
    """
    Parses url response for parameter pairs
    """
    match = re.search('/(.*\?)(\S*)', response)
    if match:
        return dict(urlparse.parse_qsl(match.groups()[1]))
    return {}