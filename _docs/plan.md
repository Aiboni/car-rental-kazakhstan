# Car Rental Marketplace Kazakhstan
## Product Specification

Status: Draft
Version: 1.0

## 1. Project Overview

Car Rental Marketplace Kazakhstan is a web platform
connecting car owners and renters across Kazakhstan.

Users can find vehicles, compare rental conditions,
make bookings, and manage rentals.

## 2. Target Market

Country: Kazakhstan
Cities: Almaty, Astana, and other cities
Currency: KZT

## 3. Problems

- Difficult car search
- Unclear rental prices and deposits
- Inconvenient booking process
- Difficult rental management for owners

## 4. User Roles

### Renter
- Register using phone and SMS OTP
- Submit identity and driving documents
- Search and filter cars
- View car details
- Book available cars
- Choose payment method
- Manage bookings
- Leave reviews
- Report disputes

### Car Owner
- Apply for owner status
- Submit ownership and insurance documents
- Publish and manage vehicles
- Set rental price and deposit
- Configure cancellation policy
- Manage rentals
- Review renters
- Manage subscriptions

### Admin
- Verify users and owners
- Moderate car listings
- Manage users
- Review disputes
- Resolve no-show cases
- Monitor bookings and payments

## 5. Authentication

Authentication uses phone numbers and SMS OTP.

- Phone number format: +7
- OTP expiration: 5 minutes
- SMS simulation in MVP
- Secure server-side sessions
- Role-based permissions

## 6. Vehicle Listings

Each vehicle includes:

- Brand and model
- Year
- City
- Photos
- Daily rental price
- Deposit
- Transmission
- Fuel type
- Seats
- Vehicle class
- Owner information
- Availability calendar
- Cancellation policy
- Reviews and ratings

## 7. Advanced Search

Filters:
- City
- Brand
- Price
- Vehicle class
- Year
- Transmission
- Fuel type
- Seats
- Rating
- Available dates

## 8. Booking

Instant booking is supported.

Online payments:
- Reserve dates for 15 minutes
- Confirm after successful simulated payment
- Release dates after payment failure or timeout

Pay at pickup:
- Confirm booking immediately

Overlapping bookings must be prevented.

## 9. Booking Lifecycle

Statuses:
- Pending Payment
- Confirmed
- Active
- Completed
- Cancelled
- Payment Failed
- No-Show
- Disputed

Handover and return include:
- Electronic reports
- Vehicle condition photos
- Damage reporting

## 10. Payments

Payment methods:
- Online simulated payment
- Pay at pickup

Real payment processing is outside MVP scope.

## 11. Deposits

Deposits can be recorded online or at pickup.

Deposit statuses:
- Pending
- Paid
- Refunded
- Partially Refunded
- Under Dispute

## 12. Cancellation Policies

Flexible:
100% refund at least 24 hours before pickup.

Moderate:
100% refund at least 72 hours before pickup.
50% refund for later cancellation.

Strict:
100% refund at least 7 days before pickup.
0% refund for later cancellation.

Refund calculations are automated.

Owner cancellation:
- Full rental refund
- Full deposit refund
- Warning issued to owner

No-show cases are reviewed by Admin.

## 13. Reviews

Two-way reviews are supported.

Renters review owners and vehicles.
Owners review renters.

Reviews are allowed after completed rentals.
Ratings range from 1 to 5.

## 14. Notifications

- In-App notifications
- Simulated Email notifications
- Simulated SMS notifications

Events:
- Booking confirmation
- Booking cancellation
- Payment status
- Verification result
- Rental reminders
- Dispute decisions

## 15. Pricing

Owners configure:
- Daily rental price
- Long-term rental discounts
- Additional services
- Deposit amount

Total rental price is shown before booking.

## 16. Monetization

Free:
- 0 KZT per month
- 10% booking commission
- Up to 3 cars

Pro:
- 9990 KZT per month
- 5% booking commission
- Up to 20 cars
- Priority listing

Commission rate is fixed at booking.

Commission is recorded after the successful
completion of a paid rental.

When Pro expires:
- Owner moves to Free
- Existing listings remain active
- New listings are blocked above the Free limit

## 17. Disputes

Administrators review damage disputes.

Evidence includes:
- Handover reports
- Return reports
- Photos
- Comments from both parties

Administrator decisions are recorded.

## 18. Technology Stack

Frontend: HTML, CSS, JavaScript
Backend: Python FastAPI
Database: PostgreSQL
API: REST JSON
Backend testing: Pytest

## 19. MVP Scope

Balanced MVP.

Includes:
- Authentication
- User roles
- Car listings
- Advanced search
- Instant booking
- Simulated payments
- Document verification
- Reviews
- Notifications
- Admin dashboard
- Subscription simulation
- Deposit and dispute management

## 20. Development Workflow

1. Brainstorming
2. Specification
3. Architecture
4. GitHub Issues
5. Implementation
6. Automated testing
7. Review
8. Merge and close issues

## 21. Acceptance Criteria

- Users can authenticate with simulated SMS OTP.
- Only verified renters can book cars.
- Only approved owners can publish cars.
- Users can filter available vehicles.
- Overlapping bookings are prevented.
- Online booking holds expire after 15 minutes.
- Payments work in simulation mode.
- Cancellation refunds follow saved policy.
- Reviews require completed rentals.
- Admin can review documents and disputes.
- Free and Pro limits are enforced.
- Commission rates are fixed at booking.
- Important backend features have automated tests.

## 22. Remaining Decisions

Before implementation, clarify:
- Rental day calculation and time zone rules
- Cancellation boundary conditions
- Handling late payments after hold expiration
- Payment and deposit settlement states
- Document upload and retention rules
- Detailed subscription expiration behavior

These items must be resolved before implementing
the affected features.
