# my_library

## About this application

## My_library
The Application aims to provide modules to easely manage libraries, also the most frequent actions made into this environment, like rent and return books, create, search, update and delete books and authors registrations.

The primary actions to create, search(read), update and delete are based into the "my_library" Odoo Module.

## My_library_return

This module is a back-end abstraction of the returning rent books actions and validations

## My_module 

This module is a front-end GUI abstraction to easely manage the users, authors, books and organizations that are interacting through the application.

## Attention!

The main module app is the "my_library", and the "my_library_return" is a complementar module of the main app, it means that the main app could work without the complementar module installed, but the complementar app does not work without the main app has been installed.

In other words, the "my_library_return" is an external dependency associated to the "my_library" app, and it was not developed to work by itself, but the "my_library" could work without "my_library_return" has been installed too.

This same relation occurs between "my_module" and "my_library", but, in this case the app does not have the "my_module" GUI as a required dependency, in other words, the use of this module is optional.

# First Steps to Use and Running the Module

## Pre requisites

First of all, you need these technologies to run this module:

- Python 3 or above installed in your Virtual Environment

- A Python Virtual Environment created to recieve the Odoo Instance and Odoo Framework

- An Odoo Instance pre-configured with an Virtual Environment activated

- Obs.: For this module I used a Virtual Environment named "odoo-12.0"

- A file .cfg into the odoo-dev/odoo with the name of the instance, example: "odoo-12.0.cfg"

# How to run

- First of all, clone this repository at the local-addons folder inside the odoo-dev folder

- After that you will initiate the venv of the instance, for example:

Terminal command: 
    
    source ~/odoo-12.0/bin/activate

- And now you initialize the Odoo Server with the following command:
    
Terminal command:

    odoo/odoo-bin --addons-path=odoo/addons,local-addons/

Also if you want to see the server executing the debug checks during live, you could add "--log-level=debug" to the command.

Terminal command with live debug activated

    odoo/odoo-bin --addons-path=odoo/addons,local-addons/ --log-level=debug

# Using watchdog lib to live-restart the odoo instance server

Once you have making some progress to update features in methods, models and so on, restarting the instance serve could be a repetitive work, with this auto-reload lib you could gain more time to the develeopment process.

## How to install it?

1. Make sure that you have activated your python development environment before install the package

2. After that, type this command in your terminal:

        odoo/odoo-bin -c ~/odoo-dev/odoo/odoo-12.0.cfg --dev=all

For more information, access the documentation of this lib in odoo docs.

# How to check if the module has been load succesfully:

- Check if the server log of the terminal had run the instance and initiated the services with http statuses 200, if not, the terminal will show the error.

- Access the Odoo instance UI with admin login credentials

- Navigate to the Apps section

- Remove the apps filter

- type in the search box:

        my_library
    
- If the module has been found, click at the install button, also you can check if the installation of the module is running.

- As soon as it finishes the installation, Odoo will refresh the page to access the module's UI.

- Finally, try to register a book, considering that you must activate the session's super-user mode.

# If you encounter any problem at the module execution, what you can do?

- You can create an issue here in the repository and I gonna see what happened.

- You can you send me an email with the subject "my_module issue".

For both options I will respond as soon as possible with pleasure to learn and help in learning the framework.

# Future features to be implemented

- [ Work In Progress ] - Refactor Security Indentities Credentials Validations
- [ Work In Progress ] - Conclusion of My_Module GUI wizards
- [ To-Do ] - Containerization of the module with Docker
- [ To-Do ] - Automated Tests
- [ To-Do ] - Internationalization
