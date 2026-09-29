# Campus Lost & Found Management System

## 1. Problem Statement
Students may lose personal belongings such as ID cards, books, wallets, keys, or other items within the college campus. At the same time, students may find items belonging to other students.
Without an organized system, recording, searching, and claiming these items can be difficult and time-consuming.
The Campus Lost & Found Management System provides a simple Python-based solution for recording lost and found items, searching for records, and submitting claims.

## 2. Scope of the Project
The project focuses on managing lost and found items within a college campus.
The system covers:

- Recording lost items.
- Recording found items.
- Viewing lost and found records.
- Searching for items.
- Submitting claims for items.
- Viewing submitted claims.
- Providing administrator functions for managing records and claims.

The current version is a console-based application and uses text files for storing data.

## 3. Target Users
The main users of the system are:

### Students
Students can:

- Report lost items.
- Report items they have found.
- Search for lost or found items.
- Submit claims for found items.
- View relevant records.

### Administrator
The administrator can:

- Log in to the administrator section.
- View lost-item records.
- View found-item records.
- View submitted claims.
- Manage claims through the administrator menu.

## 4. High-Level Features

### Lost Item Management
Allows users to add and view lost-item records containing information such as item name, colour, location, and date.

### Found Item Management
Allows users to add and view found-item records containing information such as item name, colour, location, and date.

### Item Search
Allows users to search for an item in lost or found records. The search supports case-insensitive matching.

### Claim Management
Allows users to submit claims by providing the item name, claimant name, and proof or description. New claims are stored with a Pending status.

### Administrator Management
Provides an administrator login and options for viewing lost items, found items, claims, and managing claims.
