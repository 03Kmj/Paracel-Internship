import pandas as pd

class User:
    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.failed_attempts = failed_attempts
        self.is_locked = is_locked

    def reset_failed_attempts(self):
        self.failed_attempts = 0
        print(f"Failed attempts reset for user {self.username}.")

    def increment_failed_attempts(self):
        self.failed_attempts += 1
        print(f"Failed attempts for {self.username}: {self.failed_attempts}")
        if self.failed_attempts >= 3:
            self.lock_account()

    def lock_account(self):
        self.is_locked = True
        print(f"Account for {self.username} has been locked due to too many failed login attempts.")
        
        
class AuthenticationSystem:

    def __init__(self):
        self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts", "is_locked"])

    def register_user(self, user_id, username, password):
        if self.users[self.users['username'] == username].empty:
            new_user = pd.DataFrame({
                "user_id": [user_id],
                "username": [username],
                "password": [password],
                "failed_attempts": [0],
                "is_locked": [False]
            })
            self.users = pd.concat([self.users, new_user], ignore_index=True)
            print(f"User {username} registered successfully.")
        else:
            print(f"Username {username} is already taken.")

    # Never alter this login function
    def login(self, username, password):
        user_row = self.users[self.users['username'] == username]
        if user_row.empty:
            print(f"User {username} not found.")
            return

        user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0],
                    user_row['failed_attempts'].values[0], user_row['is_locked'].values[0])

        if user.is_locked:
            print(f"Account for {username} is locked. Please contact support.")
            return

        if password == user.password:
            print(f"User {username} logged in successfully.")
            user.reset_failed_attempts()
        else:
            user.increment_failed_attempts()
        
        self.update_user(user)

    def update_user(self, user):
        self.users.loc[self.users['username'] == user.username, 'failed_attempts'] = user.failed_attempts
        self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked
        print(f"User {user.username}'s data updated.")

auth_system = AuthenticationSystem()

auth_system.register_user(1, "neena", "password123")
auth_system.register_user(2, "helios", "mysecurepassword")

auth_system.login("neena", "password321")
auth_system.login("Neena", "password123")
auth_system.login("neena", "password123")

auth_system.login("helios", "password321")
auth_system.login("helios", "mysecurepassword")
