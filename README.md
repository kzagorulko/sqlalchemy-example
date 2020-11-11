## SQLAlchemy + postgres example

### Setup


#### Virtual environment setup

```bash
python3 -m venv .venv

or

python -m venv .venv
```

#### Database setup

(on postgres console)

```bash
create database "sqlalchemy_demo";
create user "flower_dev_user" with encrypted password 'sqlalchemy_demo_user';
grant all privileges on database "sqlalchemy_demo" to "sqlalchemy_demo_user";
```

#### Day-to-day setup

##### unix

```bash
source .venv/bin/activate  # unix
```

##### windows

```bash
.venv\Scripts\activate.bat
```

##### exit environment

```bash
deactivate
```

### Requirements

```bash
pip install -r requirements.txt
```

### Migrations

```bash
# make automatic migration
make db-migrate

# upgrade database to head
make db-upgrade

# downgrade database at one revision
make db-downgrade
```

### Usage

```python
from main import create_user, get_users, get_user, update_user, delete_user

create_user('Laurence', 'Laurence Wachowski', 'matrix')

#
# result:
# Created! Id: 1
#

get_users()

#
# result:
# <User id=1 name=Laurence fullname=Laurence Wachowski nickname=matrix>
#

get_user(1)

#
# result:
# <User id=1 name=Laurence fullname=Laurence Wachowski nickname=matrix>
#

update_user(1, name='Lana', fullname='Lana Wachowski', nickname='jupiter')

#
# result:
# Updated
#

delete_user(1)

#
# result:
# Deleted
#

```
