# System Architecture

## Project
Car Rental Marketplace Kazakhstan

## Architecture Style
Web application with REST API.

## Frontend
HTML5, CSS3, Vanilla JavaScript.

Responsibilities:
- Display car listings
- Search and filtering
- Booking interface
- User dashboards
- Admin dashboard

## Backend
Python FastAPI.

Responsibilities:
- Authentication using SMS OTP
- User roles and permissions
- Document verification
- Car listing management
- Booking availability and reservations
- Payment simulation
- Cancellation and refunds
- Reviews and ratings
- Notifications
- Subscription management
- Dispute resolution

## Database
PostgreSQL with SQLAlchemy ORM.

Main entities:
- User
- OwnerApplication
- VerificationDocument
- Car
- CarImage
- Booking
- Payment
- Deposit
- HandoverReport
- DamageReport
- Dispute
- Review
- Notification
- Subscription
- Commission

## Authentication
Phone number and SMS OTP.
Use simulated SMS in the MVP.
Use secure server-side sessions.

## Booking
Pay-at-pickup bookings confirm immediately.

Online payments reserve selected dates
for 15 minutes before payment confirmation.

Prevent overlapping confirmed bookings.

## Payments
Use simulated payment transactions.
Do not process real money.

## Security
- Role-based access control
- Secure session cookies
- OTP expiration and rate limiting
- Protected document storage
- Input validation
- Database transactions for booking operations
- No secrets in Git

## Testing
Use Pytest for backend tests.
Test booking conflicts, permissions,
payments, subscriptions, and refunds.

## Deployment
Local development first.
Production deployment is outside initial MVP scope.
