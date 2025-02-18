import os
import snowflake.connector as sc

private_key_path = os.environ.get("PRIVATE_KEY_PATH")

def connect():
    creds = {
        'user':'SERV_API',
        'account':'sfseeurope-acombes_jg_aws',
        'warehouse':'API_WH',
        'database':'API',
        'schema':'PUBLIC',
        'private_key_file':private_key_path
    }
    return sc.connect(**creds)

if __name__ == "__main__":
    ctx = connect()
    cursor = ctx.cursor()

    try:
        cursor.execute("SELECT current_user(), current_role()")
        print('current user and role :\n',cursor.fetchone())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        ctx.close()
