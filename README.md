## Uranus

## Step 1: Install library
```sh
pip install -r requirements.txt
```

## Step 2: Migration Database
```sh
alembic upgrade head
```
```sh
alembic downgrade base
```

## Other: Update resource
```sh
pyrcc5 ui/resource.qrc -o ui/resource_rc.py
```

## Other: Update ui
```sh
pyuic5 main_window.ui -o main_window_ui.py

```



## Other: Lưu thay đổi của database
```sh
alembic revision --autogenerate -m "first commit"

```