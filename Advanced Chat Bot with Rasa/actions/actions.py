# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideCourseFees(Action):
    def name(self) -> str:
        return "action_provide_course_fees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        # Determine the course based on the user's message
        course = tracker.get_slot('course')  # Example slot where course information might be stored

        if course == 'computer_science':
            response = "The course fees for a BSc (Hons) in Computer Science are 1,600,000.00 LKR."
        elif course == 'software_engineering':
            response = "The course fees for a BSc (Hons) in Software Engineering are 1,600,000.00 LKR."
        else:
            response = "I'm not sure about that course. Can you please provide more details?"

        dispatcher.utter_message(text=response)
        return []
