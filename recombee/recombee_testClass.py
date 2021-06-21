

class Recommendation:
    # this is cought from the front
    boosters = {
        "empty": "",
        "booster_for_happy": "if a then b",
        "booster_for_sad": "if b then a",
    }
    filters = {
        "empty": "",
        "preference_filter1": "filter by some value",
        "preference_filter2": "filter by some value",
    }

    scenarios = {
        "empty": "",
        "main": "main_music"
    }

    def __init__(self, recom_type, user_id=0, item_id=0, scenario="empty", filter="empty", booster="empty",
                 number_of_items=5):
        self.user_id = user_id
        self.item_id = item_id
        self.recom_type = recom_type
        self.scenario = self.scenarios[scenario]
        self.rfilter = self.filters[filter]
        self.booster = self.boosters[booster]
        self.number_of_items = number_of_items

    def get_result(self):
        if recom_type == "itu":
            client.send(
                RecommendItemsToUser(self.user_id, self.number_of_items, scenario=self.scenario, cascade_create=False,
                                     filter=self.rfilter, booster=self.booster))
        elif recom_type == "iti":
            client.send(RecommendItemsToItem(self.item_id, self.user_id, self.number_of_items, scenario=self.scenario,
                                             cascade_create=False, filter=self.rfilter, booster=self.booster))

    def add_rating(self, rating):
        # rating [-1;1]
        result = client.send(AddRating(self.user_id, self.item_id, rating, cascade_create=False))
        return result

    def view_portion(self, portion):
        # portion [0;1]
        client.send(SetViewPortion(self.user_id, self.item_id, portion, cascade_create=False))
