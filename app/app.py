from connector import connect
from fastapi import FastAPI, Request
import ngrok
import os

api_password = os.environ.get("API_PASSWORD")
jg_id = int(os.environ.get("JG_ID"))
correct_answer = os.environ.get("CORRECT_ANSWER")
port = os.environ.get("PORT")

app = FastAPI(title="Jeudis Givres API", version="1.0.0")

listener = ngrok.forward(f"localhost:{port}", authtoken_from_env=True)

@app.get("/")
def root(request: Request):

    endpoints = {
        "To see current ladder [GET]": f"{request.url}ladder",
        "To submit your answer [GET]": f"{request.url}submit"
    }
    return {
        "API_status": "running",
        "Available endpoints": endpoints,
    }

@app.get("/ladder")
def ladder():
    ctx = connect()
    cursor = ctx.cursor()
    try:
        cursor.execute("SELECT * FROM POINTS LIMIT 100")
        ladder = cursor.fetchall()
        return ladder
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "internal error, see server logs"}


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

        if attempt <= 5:
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

    else:
        return {"error":"incorrect password"}
