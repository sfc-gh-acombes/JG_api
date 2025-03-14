CREATE OR REPLACE USER SERV_API
  DEFAULT_ROLE = 'SERV_API_ROLE'
  TYPE = 'SERVICE';
ALTER USER SERV_API SET RSA_PUBLIC_KEY=""; -- To adapt with public key in .secrets/*

CREATE ROLE SERV_API_ROLE;

GRANT USAGE ON DATABASE API TO ROLE SERV_API_ROLE;
GRANT USAGE ON SCHEMA API.PUBLIC TO ROLE SERV_API_ROLE;
GRANT SELECT, INSERT ON TABLE API.PUBLIC.REQUESTS TO ROLE SERV_API_ROLE;
GRANT SELECT ON VIEW API.PUBLIC.POINTS TO ROLE SERV_API_ROLE;

GRANT USAGE ON WAREHOUSE API_WH TO ROLE SERV_API_ROLE;
GRANT ROLE SERV_API_ROLE TO USER SERV_API;
ALTER USER SERV_API SET DEFAULT_ROLE = "SERV_API_ROLE";
