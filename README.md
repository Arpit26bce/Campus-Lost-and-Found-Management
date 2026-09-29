# Campus Lost & Found Management System

## Overview

The **Campus Lost & Found Management System** is a Python-based console application developed to manage lost and found items within a college campus.

The system allows users to report lost items, report found items, search for records, and submit claims. An administrator section is also included for viewing records and managing claims.

## Objectives

* Provide an organized way to record lost and found items.
* Allow users to search for lost or found items.
* Provide a simple claim submission system.
* Provide administrator functionality for managing records and claims.
* Apply Python programming concepts to a real-world problem.

## Technologies Used

* Python
* Functions
* Modules
* Dictionaries
* Lists
* Conditional Statements
* Loops
* File Handling
* Text Files

## Project Structure

```text
Campus-Lost-and-Found/
│
├── README.md
├── statement.md
├── main.py
├── lost.py
├── found.py
├── find.py
├── claim.py
├── admin.py
├── lost.txt
├── found.txt
└── claims.txt
```

## Features

### 1. Lost Item Management

* Add details of a lost item.
* Store item name, colour, location and date.
* View stored lost-item records.

### 2. Found Item Management

* Add details of a found item.
* Store item name, colour, location and date.
* View stored found-item records.

### 3. Item Search

* Search for lost items.
* Search for found items.
* Perform case-insensitive searches.

### 4. Claim Management

* Submit a claim for a found item.
* Enter claimant name and proof/details.
* Store claim information.
* New claims are assigned Pending status.
* View submitted claims.

### 5. Administrator

* Administrator login.
* View lost items.
* View found items.
* View claims.
* Approve or reject claims.

## Installation

### Prerequisites

Before running the project, make sure the following are installed:

* Python 3.x
* A Python-compatible IDE such as Visual Studio Code (optional)

### Installing Python

1. Download and install Python 3.x.
2. During installation on Windows, enable **Add Python to PATH**.
3. Verify the installation by opening Command Prompt and running:

```bash
python --version
```

If Python is installed correctly, the installed Python version will be displayed.

### Downloading the Project

Clone the repository using Git:

```bash
git clone https://github.com/Arpit26bce/Campus-Lost-and-Found-Management.git
```

Move into the project directory:

```bash
cd Campus-Lost-and-Found
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### Running the Project

Since all project files are located in the same folder, run:

```bash
python main.py
```

The main menu will then be displayed in the terminal.

##  Testing Instructions

After running `main.py`, test the following functions.

### Test 1: Add Lost Item

1. Select `Add Lost Item`.
2. Enter the item name.
3. Enter the colour.
4. Enter the location.
5. Enter the date.
6. Verify that the lost-item record is stored successfully.

### Test 2: View Lost Items

1. Select `View Lost Items`.
2. Verify that the stored lost-item records are displayed.

### Test 3: Add Found Item

1. Select `Add Item Found`.
2. Enter the item name.
3. Enter the colour.
4. Enter the location.
5. Enter the date.
6. Verify that the found-item record is stored successfully.

### Test 4: View Found Items

1. Select `View Items Found`.
2. Verify that the stored found-item records are displayed.

### Test 5: Search Item

1. Select `Find Lost Item`.
2. Choose whether to search lost or found items.
3. Enter the item name.
4. Verify that the correct matching record is displayed.
5. Test the search using both uppercase and lowercase letters.

### Test 6: Submit Claim

1. Select `Claim Item`.
2. Enter the item name.
3. Enter the claimant's name.
4. Enter proof or a description of ownership.
5. Verify that the claim is stored with `Pending` status.

### Test 7: View Claims

1. Select `View Item Claims`.
2. Verify that submitted claims are displayed.

### Test 8: Administrator Login

1. Select `Admin Login`.
2. Enter the administrator credentials.
3. Verify that the administrator menu opens after successful login.
4. Test the available administrator options.

### Test 9: Invalid Input

1. Enter an invalid menu option.
2. Verify that an appropriate error message is displayed.

### Expected Result

All major functions should execute successfully, records should be stored and retrieved correctly, search results should be displayed appropriately, and invalid inputs should be handled with suitable messages.

