# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Dict, Text, Any, List, Union

from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class HotelServiceAction(FormAction):
    # action名称
    def name(self) -> Text:
        return "hotel_service_select_action"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        hotel_service_option = tracker.get_slot("hotel_service_option")
        # hotel_house_service_option = tracker.get_slot('hotel_house_service_option')
        # hotel_send_service_option = tracker.get_slot('hotel_send_service_option')
        # hotel_moving_into_again_service_option = tracker.get_slot('hotel_moving_into_again_service_option')
        if hotel_service_option == "h1":
            return ["hotel_service_option"]
        elif hotel_service_option == "h2":
            return ["hotel_service_option", "hotel_house_service_option"]
        elif hotel_service_option == "h3":
            return ["hotel_service_option", "hotel_send_service_option"]
        elif hotel_service_option == "h4":
            return ["hotel_service_option"]
        elif hotel_service_option == "h5":
            return ["hotel_service_option"]
        elif hotel_service_option == "h6":
            return ["hotel_service_option", "hotel_moving_into_again_service_option"]
        return ["hotel_service_option"]

    def slot_mappings(self) -> Dict[Text, Any]:
        """映射所需槽位"""
        return {
            "hotel_service_option": self.from_entity(entity="hotel_service_option"),
            "hotel_house_service_option": self.from_entity(entity="hotel_house_service_option"),
            "hotel_moving_into_again_service_option": self.from_entity(entity="hotel_moving_into_again_service_option"),
            "hotel_send_service_option": self.from_entity(entity="hotel_send_service_option")
        }    

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        hotel_service_option = tracker.get_slot('hotel_service_option')
        hotel_house_service_option = tracker.get_slot('hotel_house_service_option')
        hotel_send_service_option = tracker.get_slot('hotel_send_service_option')
        hotel_moving_into_again_service_option = tracker.get_slot('hotel_moving_into_again_service_option')
        buttons = [
            {'title': '继续', 'payload': '/restart{"restart": "yes"}'}
        ]
        if hotel_service_option == "h1":
            dispatcher.utter_message("wifi账号是：shulvxiaomi  密码是:xiaomi110", buttons=buttons)
            return []
        elif hotel_service_option == "h2":
            if hotel_house_service_option > "d0":
                dispatcher.utter_message("好的，马上处理", buttons=buttons)
                return []
        elif hotel_service_option == "h3":
            if hotel_send_service_option > "n0":
                dispatcher.utter_message("好的，马上送到", buttons=buttons)
                return []
        elif hotel_service_option == "h4":
            dispatcher.utter_message("好的，马上处理", buttons=buttons)
            return []
        elif hotel_service_option == "h5":
            dispatcher.utter_message("好的，马上处理", buttons=buttons)
            return []
        elif hotel_service_option == "h6":
            if hotel_moving_into_again_service_option > "z0":
                dispatcher.utter_message("好的，马上办理续住", buttons=buttons)
                return []
        dispatcher.utter_message("请问你有什么需要帮助的吗？", buttons=buttons)
        return []
