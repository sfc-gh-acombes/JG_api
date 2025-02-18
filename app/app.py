from connector import connect
from fastapi import FastAPI, Request
import os

api_password = os.environ.get("API_PASSWORD")
jg_id = int(os.environ.get("JG_ID"))
correct_answer = os.environ.get("CORRECT_ANSWER")

app = FastAPI(title="Jeudis Givres API", version="1.0.0")

@app.get("/")
def root(request: Request):
    endpoints = {
        "To see current ladder [GET]": f"{request.url}ladder",
        "To submit your answer [GET]": f"{request.url}submit"
    }

    return {
        "API_status": "running",
        "API Documentation": f"{request.url}docs",
        "Available endpoints": endpoints,
    }

@app.get("/ladder")
def ladder():
    ctx = connect()
    cursor = ctx.cursor()
    try:
        cursor.execute("SELECT * FROM POINTS LIMIT 100")
        ladder = cursor.fetchall()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        ctx.close()
    return ladder

@app.get("/submit")
def submit(password,user,answer):

    if password == api_password:
        correct = answer == correct_answer

        ctx = connect()
        cursor = ctx.cursor()

        cursor.execute(
            f"""
            SELECT COALESCE(MAX(ATTEMPT), 0) + 1 FROM REQUESTS WHERE USER = '{user}'
            """
            )
        attempt = cursor.fetchone()[0]

        if attempt < 5:
            cursor.execute(
                f"""
                INSERT INTO REQUESTS
                (REQUEST_TS, USER, ANSWER, JG_ID, ATTEMPT, CORRECT)
                VALUES (CURRENT_TIMESTAMP(), '{user}', '{answer}', {jg_id}, {attempt}, {correct})
                """
                )
            if correct:
                return {"message":"congrats"}
            else:
                return {"message":"try again, remaining attempts: "+str(5-attempt)}
        else:
            return {"error":"maximum attempts reached"}
        cursor.close()
        ctx.close()

    else:
        return {"error":"incorrect password"}
