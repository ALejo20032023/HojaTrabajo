# Docker Multi-Container Application

This project demonstrates a multi-container web application using Docker Compose with Flask and PostgreSQL.

## Project Structure

```
docker-lab/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Flask container configuration
├── docker-compose.yml # Multi-container orchestration
└── README.md          # This file
```

## Prerequisites

1. **Docker Desktop** must be installed and running
2. **Docker Compose** (included with Docker Desktop)

## Quick Start

### 1. Start Docker Desktop
Make sure Docker Desktop is running on your system.

### 2. Build and run the services
```bash
docker compose up -d
```

### 3. Verify the containers are running
```bash
docker ps
```

You should see two containers:
- `flask-app` (Flask application)
- `postgres-db` (PostgreSQL database)

## Testing the Application

### 1. Verify connection to database
```bash
curl http://localhost:8080
```
Expected response: "App connected to PostgreSQL"

### 2. Add a new message
```bash
curl -X POST "http://localhost:8080/add?texto=HolaDocker"
```
Expected response: "Message added: HolaDocker"

### 3. List all messages
```bash
curl http://localhost:8080/list
```
Expected response: JSON with all stored messages

## Testing Data Persistence

### 1. Stop the containers
```bash
docker compose down
```

### 2. Start them again
```bash
docker compose up -d
```

### 3. Check that messages still exist
```bash
curl http://localhost:8080/list
```

The messages should still be there thanks to the persistent volume `db_data`.

## Application Endpoints

- `GET /` - Creates the messages table and verifies database connection
- `POST /add?texto=<message>` - Adds a new message to the database
- `GET /list` - Retrieves all messages from the database

## Architecture

- **Flask App**: Runs on port 8080 (mapped from container port 5000)
- **PostgreSQL**: Runs on default port 5432 (internal to Docker network)
- **Volume**: `db_data` ensures data persistence across container restarts
- **Network**: Both containers communicate through Docker's default network

## Environment Variables

The Flask application uses these environment variables for database connection:
- `DB_HOST`: db (container name)
- `DB_NAME`: mensajesdb
- `DB_USER`: admin
- `DB_PASSWORD`: admin123

## Troubleshooting

If you encounter issues:

1. **Docker Desktop not running**: Start Docker Desktop application
2. **Port conflicts**: Ensure port 8080 is not in use by another application
3. **Permission issues**: Make sure Docker has proper permissions on Windows

## Clean Up

To remove all containers, networks, and volumes:
```bash
docker compose down -v
```

This will also remove the persistent database volume, so all data will be lost.
