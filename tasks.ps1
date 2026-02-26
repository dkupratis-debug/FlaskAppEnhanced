param(
    [Parameter(Position=0)]
    [ValidateSet("install","dev","test","lint","run","prod")]
    [string]$Task = "test"
)

function Use-Venv {
    if (Test-Path ".\venv\Scripts\activate") {
        . .\venv\Scripts\activate
    }
}

switch ($Task) {
    "install" {
        python -m venv venv
        Use-Venv
        pip install -r requirements.txt
    }
    "dev" {
        Use-Venv
        pip install -r requirements-dev.txt
    }
    "test" {
        Use-Venv
        pytest -q
    }
    "lint" {
        Use-Venv
        ruff check .
    }
    "run" {
        Use-Venv
        python app.py
    }
    "prod" {
        $env:FLASK_ENV = "production"
        Use-Venv
        gunicorn -c gunicorn.conf.py wsgi:app
    }
}
