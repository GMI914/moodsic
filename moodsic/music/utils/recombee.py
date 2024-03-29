from recombee_api_client.api_requests import RecommendItemsToItem, AddRating, RecommendItemsToUser, SetViewPortion, AddDetailView
from recombee_api_client.api_client import RecombeeClient

client = RecombeeClient('moodsic-dev', 'Pb4MhOK6751HmdEGmvISdFJqXjLDWEtVkyb2AIY4Cn1EL3vQWy9V0B236OGEj8iy')


class Recommendation:
    # this is caught from the front
    boosters = {
        "empty": None,
        "booster_for_happy": "if a then b",
        "booster_for_sad": "if b then a",
    }
    filters = {
        "empty": None,
        "happy": "'mood' == \"happy\"",
        "cheerful": "'mood' == \"cheerful\"",
        "gloomy": "'mood' == \"gloomy\"",
        "sad": "'mood' == \"sad\"",
    }

    scenarios = {
        "empty": None,
        "main": "main_music",
    }

    def __init__(self,
                 recom_type='iti',
                 user_id=0,
                 item_id=0,
                 scenario="empty",
                 r_filter="empty",
                 booster="empty",
                 number_of_items=10
                 ):
        self.user_id = user_id
        self.item_id = item_id
        self.recom_type = recom_type
        self.scenario = self.scenarios[scenario]
        self.computed_filter = self.filters.get(r_filter, None)
        self.booster = self.boosters[booster]
        self.number_of_items = number_of_items * 3

    def get_result(self):
        if self.recom_type == "itu":
            return client.send(RecommendItemsToUser(
                user_id=self.user_id, count=self.number_of_items, scenario=self.scenario, cascade_create=False,
                filter=self.computed_filter, booster=self.booster))
        elif self.recom_type == "iti":
            return client.send(RecommendItemsToItem(
                item_id=self.item_id, target_user_id=self.user_id, count=self.number_of_items, scenario=self.scenario,
                cascade_create=False, filter=self.computed_filter, booster=self.booster))
        elif self.recom_type == "itius":
            result_1 = client.send(RecommendItemsToItem(
                item_id=self.item_id, target_user_id=self.user_id, count=self.number_of_items, scenario=self.scenario,
                cascade_create=False, filter=self.computed_filter, booster=self.booster))
            result_2 = client.send(RecommendItemsToUser(
                user_id=self.user_id, count=self.number_of_items, scenario=self.scenario, cascade_create=False,
                filter=self.computed_filter, booster=self.booster))
            return {'recomms': result_1.get('recomms', []) + result_2.get('recomms', [])}

    def add_detail_view(self):
        client.send(AddDetailView(self.user_id, self.item_id, cascade_create=True))
        

    def add_rating(self, rating):
        # rating [-1;1]
        result = client.send(AddRating(self.user_id, self.item_id, rating, cascade_create=False))
        return result

    def view_portion(self, portion):
        # portion [0;1]
        client.send(SetViewPortion(self.user_id, self.item_id, portion, cascade_create=False))
