# bakery-management

APIs for a simple bakery management app written in django

### Setup

- clone the repo `git clone git@github.com:dbads/bakery-management.git`
- create virtual environment `python3 -m venv /path/to/venv`
- activate the venv `souce venv/bin/activate`
- install dependencies `pip install -r requirements.txt`
- make migrations `python manage.py makemigrations`
- migrate `python manage.py migrate`

For Registering/Login/Logout/change password go to `localhost:8000/users/auth/register`, `localhost:8000/users/auth/login`

then

- start the api server `python manage.py runserver`

visit `localhost:8000/users/` for users `localhost:8000/products/` for products and `localhost:8000/orders/` for orders also you can make api requests from postman as per the given psotman collection and environment in this repo

Features

- Account creation
- Staff users can create/view/edit/delete `products/ingredients`
- Users can create orders with any number of products/ingredients
- Users can see their orders

#### reach out to me at <a href="mailto:deepakbharti@mnnit.ac.in">deepakbharti@mnnit.ac.in</a> for any queries.
