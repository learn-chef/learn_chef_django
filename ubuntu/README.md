learn\_chef\_django
=================

# Manual setup (no Chef)

We'll later be using Chef to deploy, but for now...

1. Run `install.sh`.

  ```bash
sudo bash ./install.sh
```

When prompted for a database password, enter **learnchef**.

1. Set up the database.

  ```bash
mysql --user=root --password=learnchef
> CREATE DATABASE random\_images\_db;
> exit
```

1. Run the migrations.

  ```bash
python manage.py sqlmigrate random_images 0001
python manage.py migrate
```

1. Run the app

  ```bash
python manage.py runserver&
```

The app will be available at http://127.0.0.1:8000.
