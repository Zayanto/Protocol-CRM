# project

#### Project environment setup (OS: Linux)
1. Install necessary packages from the Ubuntu Repositories

    ```shell script
    sudo apt update
    sudo apt install -y python3-python3-dev libpq-dev postgresql postgresql-contrib nginx curl redis supervisor
    ``` 

2. Create PostgreSQL Database and User
    ```shell script
    sudo -u postgres psql -c "CREATE DATABASE project;"
    sudo -u postgres psql -c "CREATE USER admin WITH PASSWORD 'admin';"
    sudo -u postgres psql -c "ALTER ROLE admin SET client_encoding TO 'utf8';"
    sudo -u postgres psql -c "ALTER ROLE admin SET default_transaction_isolation TO 'read committed';"
    sudo -u postgres psql -c "ALTER ROLE admin SET timezone TO 'UTC';"
    sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE project TO admin;"
    ```

3. Create a Python Virtual Environment for the Project
    ```shell script
    sudo apt install python3-venv
    ```
4. Clone repo from Git
    ```shell script
        mkdir "project" && cd "project"
        git clone https://github.com/radugaf/project.git .
    ```
5. Install dependency python packages

    ```shell script
    python3 -m venv venv
    source venv/bin/activate
    
    pip install -r requirements.txt
    deactivate
    ```

6. Modify `venv/bin/active` file
    ```text
        ...
    
        unset VIRTUAL_ENV
        if [ ! "${1-}" = "nondestructive" ] ; then
        # Self destruct!
            unset -f deactivate
        fi
        
        # unset all the environment variables
        unset ENV_TYPE
        unset SECRET_KEY
        unset STRIPE_TEST_PUBLISHABLE_KEY
        unset STRIPE_TEST_SECRET_KEY
    }
    
    ...
    
    if [ -n "${BASH-}" ] || [ -n "${ZSH_VERSION-}" ] ; then
    hash -r 2>/dev/null
    fi
    
    
    # set all the environment variables
    export ENV_TYPE="DEVELOPMENT"
    export SECRET_KEY=v&64ny@1!bygkq+fx5v_-y=nj3in@5^g)&(5q9%e#)fme1%rs=
    export STRIPE_TEST_PUBLISHABLE_KEY=pk_test_8mZ216teiA96kbPpAWmfz6Hz00XFo6tCA6
    export STRIPE_TEST_SECRET_KEY=sk_test_51G4L75Fh1uRkuYPnfuyD9lufIbPKwWgiI6OYi3xS5Wf2HjRDpETJty8pQAi9w8kESFOjdt4jG9MUAThgWgYl1IAS00ZFFIowe0
    ```

7. Migrate database and create a superuser
    ```shell script
    # considering you are in ~/maoss/ directory
    source venv/bin/activate
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser    
    ```
