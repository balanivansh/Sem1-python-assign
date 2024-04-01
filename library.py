from datetime import datetime, timedelta

class Library:
    def __init__(self):
        self.catalog = {}
        self.users = {}
        self.transactions = {}

    def display_catalog(self):
        print("Catalog:")
        for book_id, details in self.catalog.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Available: {details['quantity']}")

    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {'name': name, 'checked_out': [], 'overdue_fines': 0}
            print(f"User {name} with ID {user_id} registered successfully.")
        else:
            print("User ID already exists. Please choose a different ID.")

    def checkout_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.catalog:
            print("Book not found in catalog.")
            return
        if self.catalog[book_id]['quantity'] == 0:
            print("Book not available for checkout.")
            return
        if len(self.users[user_id]['checked_out']) >= 3:
            print("User has reached the maximum limit of checked out books.")
            return

        self.users[user_id]['checked_out'].append({'book_id': book_id, 'checkout_date': datetime.now()})
        self.catalog[book_id]['quantity'] -= 1
        print(f"Book {self.catalog[book_id]['title']} checked out successfully by user {self.users[user_id]['name']}.")

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        if book_id not in self.catalog:
            print("Book not found in catalog.")
            return
        found_book = None
        for book in self.users[user_id]['checked_out']:
            if book['book_id'] == book_id:
                found_book = book
                break
        if not found_book:
            print("Book not checked out by this user.")
            return

        checkout_date = found_book['checkout_date']
        due_date = checkout_date + timedelta(days=14)
        return_date = datetime.now()
        if return_date > due_date:
            overdue_days = (return_date - due_date).days
            overdue_fine = overdue_days
            self.users[user_id]['overdue_fines'] += overdue_fine
            print(f"Book returned {overdue_days} days late. Overdue fine: ${overdue_fine}.")
        else:
            print("Book returned successfully.")
        self.catalog[book_id]['quantity'] += 1
        self.users[user_id]['checked_out'].remove(found_book)

    def list_overdue_books(self, user_id):
        if user_id not in self.users:
            print("User not registered.")
            return
        overdue_books = []
        total_fine = 0
        for book in self.users[user_id]['checked_out']:
            checkout_date = book['checkout_date']
            due_date = checkout_date + timedelta(days=14)
            if datetime.now() > due_date:
                overdue_days = (datetime.now() - due_date).days
                overdue_fine = overdue_days
                overdue_books.append({'book_id': book['book_id'], 'title': self.catalog[book['book_id']]['title'], 'fine': overdue_fine})
                total_fine += overdue_fine
        if overdue_books:
            print("Overdue Books:")
            for book in overdue_books:
                print(f"Book ID: {book['book_id']}, Title: {book['title']}, Fine: ${book['fine']}")
            print(f"Total Fine: ${total_fine}")
        else:
            print("No overdue books found.")