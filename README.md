## AirBnB: A Persistent Object Storage Engine with Console Interface

This project implements a persistent object storage engine along with a console interface for managing objects. It provides an abstraction layer between your application logic and data storage, allowing you to easily switch between different storage backends without modifying your codebase.

### Project Description

**Components:**

- **Storage Engine:** Provides a robust and flexible way to store and retrieve data objects. It handles serialization and persistence of objects to a file (JSON format in this case).
- **Console Interpreter:** Acts as a command-line tool for interacting with the storage engine. It allows users to create, retrieve, update, and delete objects.

**Key Features:**

- **Abstraction:** Separates data storage concerns from application logic.
- **Persistence:** Stores data objects to a JSON file, ensuring data preservation even after program termination.
- **Console Interface:** Offers a user-friendly way to interact with the storage engine.
- **Flexibility:** Supports various object models and can be extended to use different storage backends in the future.

### Requirements

- **Programming Language:** Python 3 (version 3.8.5)
- **Code Style:** `pycodestyle` (version 2.8.\*)
- **Text Editor:** vi, vim, or emacs
- **Unit Testing:** `unittest` module
- **Operating System:** Ubuntu 20.04 LTS

### Console Interpreter

The console acts as a simple shell specifically designed for managing objects. It provides functionalities for:

- **Creating objects:** Users can specify the object type (e.g., `User`, `Place`) to create a new instance.
- **Retrieving objects:** Objects can be retrieved based on their class name and ID.
- **Listing objects:** Retrieves a list of all objects or filtered by class name.
- **Updating objects:** Attribute values can be modified for existing objects.
- **Deleting objects:** Objects can be removed from storage.

**Modes:**

- **Interactive Mode:** Provides a prompt for user input and command execution.
- **Non-Interactive Mode:** Allows piping commands from text files to the console.

### Usage

1. Run the console: `./console.py`
2. Use commands to manage objects.
   - `help`: Lists available commands with descriptions.
   - `quit`: Exits the console.

**Example Commands:**

- `create User`: Creates a new User object.
- `show User 1234-5678-9101`: Displays information for a User with ID 1234-5678-9101.
- `all BaseModel`: Lists all BaseModel objects.
- `update BaseModel 1234-5678-9101 email "someone@gmail.com"`: Updates the email attribute for a BaseModel with ID 1234-5678-9101.

**Dynamic Commands (available for defined models):**

- `[class_name].all()`: Retrieves all objects of a specific class (e.g., `User.all()`).
- `[class_name].count()`: Counts the number of objects of a specific class (e.g., `User.count()`).
- `[class_name].show(id)`: Displays information for an object of a specific class with a given ID (e.g., `User.show("1234-1536-7358")`).
- `[class_name].destroy(id)`: Deletes an object of a specific class with a given ID (e.g., `User.destroy("1234-1536-7358")`).
- `[class_name].update(id, attribute_name, value)`: Updates an attribute for an object of a
