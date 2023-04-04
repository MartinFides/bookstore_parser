# BOOKSTORE PARSER
Bookstore Parser is a Dockerized app that enables extraction of data from the official web pages of book stores.
The app provides information about books such as author, title and price grouped by company.

Currently, only one book store is supported.

## Installation
To install and run the app, follow these steps:
- Clone the repository:
```shell
  git clone https://github.com/MartinFides/bookstore_parser.git
```
- Change project directory:
```shell
  cd bookstore_parser
```
- Make sure startup.sh is executable:
```shell
chmod +x startup.sh
```
- Run the startup script:
```shell
  ./startup.sh
```

This will build the Docker image and start the container with the app.
The **output** can be seen **in** the **terminal** and is also stored in **output.txt** in the project root folder.
