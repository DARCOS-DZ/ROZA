def while_get_position(best_position=object,sorted_flower_array_from_user=dict):
    """
    This function fetches the closest possibility of ``position object`` for this order
    """
    while best_position is None:
        is_get_position=False
        for flower in sorted_flower_array_from_user:
            quantity = sorted_flower_array_from_user[flower]
            sorted_flower_array_from_user.update({flower:quantity+1})
            print(f"flower {flower} and quantity = {quantity}")
            print(sorted_flower_array_from_user)
    return best_position


def handel_dictionary(dict):
    for key in dict:
        value = int(dict[key])



def try_except_get_django_model(Model,id_name):
    "methode to return ``model`` object or none in one line"
    try:
        model = Model.objects.get(id=id_name)
    except Model.DoesNotExist:
        model=None
    return model