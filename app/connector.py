import os
import snowflake.connector

def connect() -> snowflake.connector.SnowflakeConnection:
    creds = {
        'host': os.getenv('SNOWFLAKE_HOST'),
        'port': os.getenv('SNOWFLAKE_PORT'),
        'protocol': "https",
        'account': os.getenv('SNOWFLAKE_ACCOUNT'),
        'authenticator': "oauth",
        'token': open('/snowflake/session/token', 'r').read(),
        'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
        'database': os.getenv('SNOWFLAKE_DATABASE'),
        'schema': os.getenv('SNOWFLAKE_SCHEMA'),
        'client_session_keep_alive': True
    }
    return snowflake.connector.connect(**creds)

conn = connect()
