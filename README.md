# Car Rental Marketplace Kazakhstan

## Project Overview
Car Rental Marketplace Kazakhstan is a web application where people can rent cars from private owners.

## User Roles
- Renter: searches and books cars
- Car Owner: lists cars and manages rentals
- Admin: verifies users and resolves disputes

## Technology Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python FastAPI
- Database: PostgreSQL
- Styling: CSS
- API: REST API

## Main Features
- SMS authentication
- Advanced car search
- Instant booking
- Online and offline payments
- Document verification
- Reviews and ratings
- Rental management
- Admin dashboard
- Email and SMS notifications
- Free and Pro subscriptions

## Development Methodology
AI-Native Development
Spec-Driven Development

## Project Status
Planning and Specification

## PostgreSQL Database Setup

### Requirements
- PostgreSQL 17
- Python 3
- SQLAlchemy
- Alembic
- Psycopg

### Configuration

Create a .env file in the project root:

DATABASE_URL=postgresql+psycopg://car_rental_user:YOUR_PASSWORD@localhost:5432/car_rental_db

Replace YOUR_PASSWORD with your local database password.
Never commit .env to GitHub.

### Apply database migrations

Run:

    .\.venv\Scripts\python.exe -m alembic upgrade head

### Run automated tests

Run:

    .\.venv\Scripts\python.exe -m pytest -q

### Current database tables

- users
- alembic_version
