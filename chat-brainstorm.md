# Car Rental Marketplace Kazakhstan
## Brainstorming Session

### Project Idea
Build a car rental marketplace for Kazakhstan.

### Target Market
Kazakhstan, including Almaty, Astana, and other cities.

### Problems
1. Difficult car search
2. Unclear rental prices and deposits
3. Inconvenient booking process
4. Difficult rental management for owners

### User Roles
- Renter
- Car Owner
- Admin

### Booking
Instant booking.

Online payments use a 15-minute temporary hold.
Pay-at-pickup bookings are confirmed immediately.

### Payments
- Online payment (simulated in MVP)
- Payment at pickup
- Flexible deposit (online or at pickup)

### Cancellation
Owners choose Flexible, Moderate, or Strict policies.
Refunds are calculated automatically.
Owner cancellation results in a full refund and a warning.

### Reviews
Two-way ratings between renters and owners.

### Verification
Renters submit identity and driving documents.
Owners undergo advanced document verification.
Administrators approve or reject verification.

### Search
Advanced search by city, brand, price, class,
year, transmission, fuel, seats, rating, and dates.

### Listings
Detailed car pages with photos, prices, deposits,
availability, owner information, and reviews.

### Notifications
In-App, Email, and SMS.

### Rental Lifecycle
Booking, payment, handover, active rental,
return inspection, completion, and reviews.

Electronic handover reports and damage photos.
Administrators mediate disputes and no-show cases.

### Pricing
Daily price, long-term discounts, extra services,
and a separate deposit.

### Business Model
Free: 0 KZT/month, 10% commission, maximum 3 cars.
Pro: 9990 KZT/month, 5% commission, maximum 20 cars.

Commission rates are fixed at booking.
Commission is charged after completed paid rentals.

After Pro expires, existing listings stay active,
but new listings are blocked above the Free limit.

### Technology
Frontend: HTML, CSS, JavaScript
Backend: Python FastAPI
Database: PostgreSQL

### MVP
Balanced MVP with simulated payment,
SMS, and email integrations.

### Development Approach
Specification before code.
Implementation through GitHub Issues.
Testing and QA for each implemented feature.

### Notes
This document summarizes the decisions from the
interactive brainstorming conversation.
It is not a verbatim chat transcript.
