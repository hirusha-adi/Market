# Market

a marketplace with a secure user login system to post items to sell

# How to start?

## Debian/Ubuntu

### 1. Setup MongoDB

1. install mongodb
    ```bash
    sudo apt update && sudo apt install mongodb -y
    ```

2. enable the service
    ```bash
    sudo systemctl enable mongodb --now
    ```

3. edit the config file
    ```bash
    sudo nano /etc/mongodb.conf
    ```

    1. change `bind_ip` from `127.0.0.1` to `0.0.0.0`
        ```
        bind_ip = 0.0.0.0
        ```

    2. save and exit

4. restart the service
    ```bash
    sudo systemctl restart mongodb
    ```

5. MongoDB is now publicly accessible by the default Port and the Server IP. Now, create an account and enable authorization for security
    1. Start MongoDB CLI
        ```
        mongo
        ```
    
    2. Switch to the default pre-made admin database
        ```
        use admin
        ```
    
    3. create a new user
        ```
        db.createUser(
            {
            user: "AdminUserName",
            pwd: "SuperSecretPassword",
            roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
            }
        )
        ```
    
    4. exit

6. The new user is created, Now, You have to make logging-in required
    1. edit the config file
    ```
    sudo nano /etc/mongodb.conf
    ```

    2. `Ctrl+W` to search and edit
    ```
    authorization: enabled
    ```

    3. restart the service
    ```
    sudo systemctl restart mongod
    ```


### 2. Setup the `Market`

1. install main dependencies
    ```bash
    sudo apt update && sudo apt install git nano python3 python3-pip -y
    ```

2. clone the repo and cd into it
    ```bash
    git clone "https://github.com/hirusha-adi/Market.git"
    cd Market
    ```

3. install python requirements
    ```bash
    python3 -m pip install requirements.txt
    ```

4. edit the settings
    ```bash
    nano ./database/settings.json
    ```

    1. dgfdg
    2. sedfd

5. start the web applicaion
    ```bash
    python3 market.py
    ``` 

