from v1.models import Place

def update_places():
    json =  _get_place_json()
    if json is not None:
        try:
            new_place = Place()
