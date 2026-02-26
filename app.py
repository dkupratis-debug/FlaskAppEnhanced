try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    # Optional dependency; app still runs without .env loading.
    pass

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
