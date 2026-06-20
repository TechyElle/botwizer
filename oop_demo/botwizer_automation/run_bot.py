import sys
from botwizer_automation.bot_data import BotSession, HashtagTargeter, AccountTargeter


class BotwizerAutomationRunner:
    """ Importer class that runs the botwizer automation flow """

    def run(self):
        # Open standard input file stream
        self.input_file = open(0)
        
        # Instantiate the data holder object
        self.session = BotSession()
        
        # Local state variables initialized within run
        self.username_input = ""
        self.password_input = ""
        self.target_type = ""
        self.targets_list = []
        self.comments_list = []

        try:
            print("=== Botwizer OOP Automation CLI ===")
            
            # Read username from stdin
            print("Please enter your Instagram username:")
            self.username_input = self.input_file.readline().strip()
            self.session.set_username(self.username_input)

            # Read password from stdin
            print("Please enter your Instagram password (min 6 characters):")
            self.password_input = self.input_file.readline().strip()
            self.session.set_password(self.password_input)

            # Read target type from stdin
            print("Choose target type (1 for Hashtag, 2 for Account):")
            self.target_type = self.input_file.readline().strip()
            if self.target_type not in ["1", "2"]:
                raise ValueError("Target type must be either 1 or 2")

            # Collect targets until empty line
            print("Enter target names (one per line, press enter on empty line to stop):")
            while True:
                target_line = self.input_file.readline()
                if not target_line:
                    break
                target_name = target_line.strip()
                if len(target_name) == 0:
                    break
                try:
                    self.session.add_target(target_name)
                    self.targets_list.append(target_name)
                except ValueError as error:
                    print(f"Skipping invalid target name: {error}")

            # Collect comments until empty line
            print("Enter comments (one per line, press enter on empty line to stop):")
            while True:
                comment_line = self.input_file.readline()
                if not comment_line:
                    break
                comment_text = comment_line.strip()
                if len(comment_text) == 0:
                    break
                try:
                    self.session.add_comment(comment_text)
                    self.comments_list.append(comment_text)
                except ValueError as error:
                    print(f"Skipping invalid comment text: {error}")

            # Instantiate corresponding targeter polymorphically
            if self.target_type == "1":
                targeter = HashtagTargeter()
                print("\nInitializing hashtag automation...")
            else:
                targeter = AccountTargeter()
                print("\nInitializing account automation...")

            # Run target processing using polymorphism
            print("\n--- Processing Targets ---")
            for target_item in self.session.get_targets():
                print(f"Processing target: {target_item}")
                success = targeter.process_target(target_item)
                if success:
                    print(f"Successfully processed: {target_item}")
                else:
                    print(f"Failed to process: {target_item}")

            # Print summary of findings
            print("\n--- Summary of Execution ---")
            print(f"Username used: {self.session.get_username()}")
            print(f"Total targets processed: {len(self.session.get_targets())}")
            print(f"Total comments stored: {len(self.session.get_comments())}")

        except ValueError as error:
            print(f"Value Error occurred: {error}")
        except TypeError as error:
            print(f"Type Error occurred: {error}")
        except Exception as error:
            print(f"An unexpected error occurred during execution: {error}")
        finally:
            # Always close the input file at the end of run
            self.input_file.close()
            print("Input session closed.")


# Instantiate program and call run method
if __name__ == "__main__":
    runner = BotwizerAutomationRunner()
    runner.run()
