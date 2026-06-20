import unittest
from botwizer_automation.bot_data import (
    BotSession,
    HashtagTargeter,
    AccountTargeter,
    TargetingAction,
)


class TestOopAutomation(unittest.TestCase):
    """ Test suite for botwizer OOP automation codebase """

    def test_encapsulation_username(self):
        """ Test that username is properly encapsulated and validated """
        session = BotSession()
        
        # Test valid username set/get
        try:
            session.set_username("devglitchtest")
            self.assertEqual(session.get_username(), "devglitchtest")
        except ValueError as error:
            self.fail(f"Valid username raised ValueError: {error}")

        # Test invalid empty username throws ValueError
        with self.assertRaises(ValueError):
            session.set_username("")

    def test_encapsulation_password(self):
        """ Test that password is properly encapsulated and validated """
        session = BotSession()
        
        # Test valid password set/get
        try:
            session.set_password("mypassword123")
            self.assertEqual(session.get_password(), "mypassword123")
        except ValueError as error:
            self.fail(f"Valid password raised ValueError: {error}")

        # Test short password throws ValueError
        with self.assertRaises(ValueError):
            session.set_password("12345")

    def test_encapsulation_targets_and_comments(self):
        """ Test that targets and comments lists are properly encapsulated """
        session = BotSession()
        
        # Test adding valid targets
        try:
            session.add_target("python")
            session.add_target("programming")
            self.assertEqual(session.get_targets(), ["python", "programming"])
        except ValueError as error:
            self.fail(f"Valid target raised ValueError: {error}")

        # Test empty target throws ValueError
        with self.assertRaises(ValueError):
            session.add_target("")

        # Test adding valid comments
        try:
            session.add_comment("Great post!")
            session.add_comment("Thanks for sharing.")
            self.assertEqual(session.get_comments(), ["Great post!", "Thanks for sharing."])
        except ValueError as error:
            self.fail(f"Valid comment raised ValueError: {error}")

        # Test empty comment throws ValueError
        with self.assertRaises(ValueError):
            session.add_comment("")

    def test_abstraction(self):
        """ Test that abstract class cannot be instantiated directly """
        # Verify instantiation of abstract base class raises TypeError
        with self.assertRaises(TypeError):
            TargetingAction()

    def test_inheritance_and_polymorphism(self):
        """ Test inheritance and polymorphic behavior of targeters """
        hashtag_targeter = HashtagTargeter()
        account_targeter = AccountTargeter()

        # Verify inheritance
        self.assertTrue(isinstance(hashtag_targeter, TargetingAction))
        self.assertTrue(isinstance(account_targeter, TargetingAction))

        # Verify polymorphic process_target return values and messages
        try:
            hashtag_result = hashtag_targeter.process_target("coding")
            account_result = account_targeter.process_target("jack_coder")
            
            self.assertTrue(hashtag_result)
            self.assertTrue(account_result)
        except Exception as error:
            self.fail(f"Polymorphic methods raised unexpected exception: {error}")


if __name__ == "__main__":
    unittest.main()
