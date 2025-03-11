CREATE NETWORK RULE allowed_api_ip
  MODE = INGRESS
  TYPE = IPV4
  VALUE_LIST = ('52.183.42.53');

CREATE NETWORK POLICY public_network_policy
  ALLOWED_NETWORK_RULE_LIST = ('allowed_api_ip')
