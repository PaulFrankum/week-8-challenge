Django Challenge: Build a Simple E-commerce Orders Screen 
Project Overview 
This project is a basic Orders Management page for an e-commerce platform. You'll 
design a single Django model to manage customer orders, allowing users to create, 
view, update, and delete orders through a web interface. 
Challenge Objectives 
1. Create, view, update, and delete orders. 
2. Use Django's ModelForm for easy form creation and data handling. 
3. Set up URL patterns, views, and templates to handle CRUD operations. 
4. Style templates using Bootstrap for a simple and clean UI. 
Project Structure 
plaintext 
Copy code 
ecommerce/ 
├── ecommerce/                  
│   ├── settings.py 
│   ├── urls.py 
│   └── wsgi.py 
├── orders/                     
│   ├── migrations/ 
│   ├── templates/ 
│   │   └── orders/ 
# Main project settings 
# Orders app for managing orders 
│   │       ├── order_list.html             
│   │       ├── order_form.html             
# Displays all orders 
# Form for creating/editing orders 
│   │       └── order_confirm_delete.html   # Confirmation page for deleting 
orders 
│   ├── models.py                
# Order model definition 
│   ├── views.py                 
# Views for CRUD operations 
│   ├── forms.py                 
│   └── urls.py                  
└── manage.py                    
# Form linked to Order model 
# URL patterns for CRUD operations 
# Django management script 
Key Concepts and Learning Outcomes 
By completing this challenge, you will: 
• Understand Django’s MVT architecture. 
• Set up URL routing and views for basic CRUD operations. 
• Work with Django models and ModelForms. 
• Use Django ORM to query and manage data. 
• Apply Bootstrap for simple styling. 
User Story 
As a store owner, I want to manage my orders by creating, viewing, updating, and 
deleting them so that I can keep track of customer purchases. 
Acceptance Criteria 
1. Create an Order: Users can create an order with details like customer name, 
product name, quantity, and order date. 
2. View Orders: Users can view a list of all orders. 
3. Update an Order: Users can update details of an existing order. 
4. Delete an Order: Users can delete an order from the list. 
Instructions 
Step 1: Set Up the Project 
1. Initialize Django Project: Start a new Django project and create an app called 
orders. 
2. Define Order Model: Add a model named Order with the following fields: 
o customer_name: CharField 
o product_name: CharField 
o quantity: IntegerField 
o order_date: DateField 
3. Create Migrations: Run python manage.py makemigrations and python 
manage.py migrate to set up the database. 
Step 2: Build the Views and URLs 
1. Views: 
o Create views for each CRUD operation: list, create, edit, and delete. 
2. URLs: 
o Set up URL patterns in orders/urls.py for each view, linking to /orders/, 
/orders/create/, /orders/edit/<id>/, and /orders/delete/<id>/. 
Step 3: Set Up Templates 
1. Templates: 
o order_list.html: Lists all orders. 
o order_form.html: Handles form display for creating and editing orders. 
o order_confirm_delete.html: Provides a confirmation page before 
deletion. 
Step 4: Add Bootstrap Styling (Optional) 
• Use Bootstrap to style the templates. Add Bootstrap via CDN in the base 
template for a responsive UI. 
Step 5: Run and Test 
• Start the Django server: python manage.py runserver 
• Test all CRUD functionalities by navigating to the appropriate URLs. 
Example Commands 
bash 
# Create a new Django project 
django-admin startproject ecommerce 
# Navigate into the project directory 
cd ecommerce 
# Start the orders app 
python manage.py startapp orders 
# Apply migrations 
python manage.py makemigrations 
python manage.py migrate 
# Run the development server 
python manage.py runserver 
Example CRUD Workflow 
1. Create an Order: Go to /orders/create/, fill out the form, and submit to create 
a new order. 
2. View Orders: Visit /orders/ to see a list of all current orders. 
3. Update an Order: Go to /orders/edit/<id>/ to edit an existing order. 
4. Delete an Order: Go to /orders/delete/<id>/ to delete an order. 
Happy coding!       
