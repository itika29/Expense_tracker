💸 Expense Tracker (SQLite Version)
This branch transitions the project from temporary dictionary storage to a persistent SQLite database. It focuses on data reliability and structured query handling.

🚀 Key Improvements
Data Persistence: Uses a local .db file, so your expenses and budget aren't lost when the program exits.

Structured Queries: Implemented SQL logic to fetch, sum, and update financial records.

Date-Specific Search: Added functionality to filter and view expenses based on the date of entry.

Budget Management: Dynamic calculation of the remaining balance by subtracting total expenses from the set budget.

📂 Project Structure
main.py: Handles the CLI menu and user interactions.

fundamentalfunc.py: Contains the core database logic and SQL CRUD operations.

🚦 How to Use
Switch to this branch:
git checkout sqlite-version

Bash
  git checkout sqlite-version
Run the program:
  python main.py
Bash
python main.py

🛠️ Tech Stack
Language: Python 3.x
Database Engine: SQLite3

🗺️ Roadmap
Next Version: Migration to MySQL for centralized database management.

Future Version: Transition to a web-based interface using Flask.

Data Analysis: Potential integration with Pandas for advanced financial reporting and insights.

Developed as part of a learning journey in Backend Fundamentals and Data Structures.
