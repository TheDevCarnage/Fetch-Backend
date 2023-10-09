# Fetch Assessment Solution

This Django REST Framework (DRF) application provides several endpoints for managing users and points. It includes the following features:

1. Welcome Message: A default endpoint that displays a welcome message.
2. Create User: An endpoint to create a new user with an initial balance of 0 points.
3. Create Payer and Add Points: An endpoint to create a payer and add points for a specific user.
4. Spend Points: An endpoint that allows a user to spend points and deduct the balance from their total points.
5. Check User Balance: An endpoint to check the balance of a specific user, along with a history of points granted by various payers.

## Getting Started

Follow these steps to set up and run the application:

1. Create the Virtual Environment (venv) in the root directory of the project:
`python -m venv myenv`
activate the environment by using: `myenv\Scripts\activate`

3. Install Dependencies: `pip install -r requiremwnts.txt`

4. Navigate to the `FetchAssignment` sub-directory: `cd FetchAssignment`

5. Run Database Migrations:
  `python manage.py makemigrations rewards`
  `python manage.py migrate`
7. Start the Development Server:
   `python manage.py runserver`
By default, the development server runs on port 8000.

## Endpoints

Navigate to the following endpoints to interact with the application:

- Welcome Message: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Create User: [http://127.0.0.1:8000/users](http://127.0.0.1:8000/users) (Create a user and copy the ID)
- Create Payer and Add Points: [http://127.0.0.1:8000/add](http://127.0.0.1:8000/add) (Create a payer, add points, and provide the user ID)
- Spend Points: [http://127.0.0.1:8000/spend/](http://127.0.0.1:8000/spend/) (Pass the number of points you want to spend)
- Check User Balance: [http://127.0.0.1:8000/balance/user_id/](http://127.0.0.1:8000/balance/user_id/) (Replace `user_id` with the user's actual ID to check their balance)

Please note that this application does not include authentication, and user IDs must be provided manually in the URLs for the "Check User Balance" endpoint.
