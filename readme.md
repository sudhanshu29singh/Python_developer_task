# Create a virtual environment
python -m venv "environment_name"
source environment_name/bin/activate  # On Windows use `environment_name\Scripts\activate`


example -->>
Activate the virtual environment
		myenv\Scripts\activate
Deactivate the virtual environment 
		deactivate

# Install dependencies
pip install -r requirements.txt

# open db browser and navigate to our project_folder and than
 --  Create databse example.db
 --  CREATE table IF NOT EXISTS users (
	 user_id INTEGER PRIMARY KEY AUTOINCREMENT,
	 name VARCHAR (50) NOT NULL,
     email VARCHAR(100) NOT NULL UNIQUE,
	 join_date date NOT NULL
    );
 -- CREATE table IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
 	user_id INTEGER NOT NULL,
 	amount REAL NOT NULL,
 	transaction_date date NOT NULL,
 	FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
# Run the Dash application
python app.py

# Navigate to http://127.0.0.1:8050



