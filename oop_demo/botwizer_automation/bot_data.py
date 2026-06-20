from abc import ABC, abstractmethod


class TargetingAction(ABC):
    """ Base class representing a targeting action (Abstraction) """

    @abstractmethod
    def process_target(self, target_name):
        """ Process target name (abstract method) """
        pass


class HashtagTargeter(TargetingAction):
    """ Targets posts under a specific hashtag (Inheritance) """

    def process_target(self, target_name):
        """ Polymorphic implementation of processing a hashtag target """
        try:
            # Simulate searching hashtag and liking/commenting
            print(f"Searching hashtag page: #{target_name}")
            print(f"Liking most recent post under #{target_name}")
            print(f"Adding comment to hashtag post: #{target_name}")
            return True
        except ValueError as error:
            print(f"Value error processing hashtag: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error processing hashtag: {error}")
            return False


class AccountTargeter(TargetingAction):
    """ Targets posts of a specific account (Inheritance) """

    def process_target(self, target_name):
        """ Polymorphic implementation of processing an account target """
        try:
            # Simulate visiting profile and performing interaction
            print(f"Visiting user account profile: @{target_name}")
            print(f"Liking recent post of user @{target_name}")
            print(f"Following user account: @{target_name}")
            return True
        except ValueError as error:
            print(f"Value error processing account: {error}")
            return False
        except Exception as error:
            print(f"Unexpected error processing account: {error}")
            return False


class BotSession:
    """ Manages user session and targets (Encapsulation) """

    def __init__(self):
        # Private attributes encapsulating data from external modification
        self.__username = ""
        self.__password = ""
        self.__targets = []
        self.__comments = []

    def get_username(self):
        """ Getter for username """
        return self.__username

    def set_username(self, username_value):
        """ Setter for username with input validation """
        try:
            if not username_value or len(username_value.strip()) == 0:
                raise ValueError("Username cannot be empty")
            self.__username = username_value.strip()
        except ValueError as error:
            print(f"Validation error setting username: {error}")
            raise ValueError(f"Invalid username: {error}")

    def get_password(self):
        """ Getter for password """
        return self.__password

    def set_password(self, password_value):
        """ Setter for password with validation """
        try:
            if not password_value or len(password_value.strip()) < 6:
                raise ValueError("Password must be at least 6 characters")
            self.__password = password_value.strip()
        except ValueError as error:
            print(f"Validation error setting password: {error}")
            raise ValueError(f"Invalid password: {error}")

    def get_targets(self):
        """ Getter for targets list """
        return self.__targets

    def add_target(self, target_name):
        """ Add a target to the target list """
        try:
            if not target_name or len(target_name.strip()) == 0:
                raise ValueError("Target name cannot be empty")
            self.__targets.append(target_name.strip())
        except ValueError as error:
            print(f"Validation error adding target: {error}")
            raise ValueError(f"Invalid target: {error}")

    def get_comments(self):
        """ Getter for comments list """
        return self.__comments

    def add_comment(self, comment_text):
        """ Add a comment to the comments list """
        try:
            if not comment_text or len(comment_text.strip()) == 0:
                raise ValueError("Comment text cannot be empty")
            self.__comments.append(comment_text.strip())
        except ValueError as error:
            print(f"Validation error adding comment: {error}")
            raise ValueError(f"Invalid comment: {error}")
