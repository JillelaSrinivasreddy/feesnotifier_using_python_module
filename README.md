# FeeNotifier_using_python_modules

A Python-based fee management system designed for admins to manage user details, send OTP-based authentication, and notify users about their fee status via email. The system features modular imports for handling notifications for fee-pending and fee-cleared statuses.

## Features

- *OTP-Based Authentication:*  
  Users receive a one-time password (OTP) for secure login and verification.

- *Email Notifications:*  
  Automatically sends email notifications to users based on their fee status.

- *Modular Notifications:*  
  Custom modules are implemented to handle both fee-pending and fee-cleared notifications.

## Requirements

- Python 3.x
- Standard Python libraries:
  - random
  - smtplib
  - email.mime modules

