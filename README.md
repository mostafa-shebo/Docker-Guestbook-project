# Docker-Guestbook-project
A simple guestbook application built with python (Flask) and PostgreSQL, running in Docker containers using docker compose.



![Docker-Guestbook-project](https://github.com/user-attachments/assets/f4ce2898-7543-4b37-b6e0-0cc29dbf0108)



## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Architecture](#architecture)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
- Git: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Installation

1. Clone the repository:
   git clone https://github.com/mostafa-shebo/Docker-Guestbook-project.git

         Optional ((
            You can pull the images through docker HUB by the below command
               1/ docker pull mostafaabdelaziz/guestbook-web:v1
               2/ docker pull mostafaabdelaziz/postgres:v1
         ))
   
   cd guestbook


3. Build and start the containers:
  docker-compose up --build

## Usage
Once the containers are up and running, you can access the application in your web browser at http://localhost:5000.

## Database Setup
To set up the PostgreSQL database and create the necessary tables, follow these steps:

1.Access the PostgreSQL container:
  docker exec -it guestbook-db-1 psql -U postgres -d guestbook

2.Create the entries table:
  CREATE TABLE entries (
      id SERIAL PRIMARY KEY,
      title TEXT NOT NULL,
      content TEXT NOT NULL,
      created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );

3.Verify the table creation:
  \dt

4.Exit the PostgreSQL shell:
\q

## Architecture
The architecture of the Guestbook application is illustrated below:



![Directory Structure](https://github.com/user-attachments/assets/3d889a7f-38f4-4bdf-b81d-51317881b202)



![Diagram Structure](https://github.com/user-attachments/assets/4d96a8bf-6555-4473-9d5d-93f87aa03076)



## Troubleshooting
If you encounter any issues, you can check the logs of your containers with the following command:

    docker-compose logs
    Common Issues
    Internal Server Error:
    Ensure that the PostgreSQL database is set up correctly and that the entries table exists. Check the database logs for authentication errors.
      
## Contributing
Please read CONTRIBUTING.md for details on the code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

This structure and the inclusion of the architecture diagram will help users understand the components and interactions within your project. If you need further assistance with the diagram or any other part of the README, feel free to ask!
