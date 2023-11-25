## Uranus

## Step 1: Install library
```sh
pip install -r requirements.txt
```

## Step 2: Migration Database
```sh
alembic upgrade head
```

## Other: Update resource
```sh
pyrcc5 ui/resource.qrc -o ui/resource_rc.py
```