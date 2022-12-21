def while_get_position():
    pass

def try_except_get_django_model(Model,id_name):
    "methode to return model object or none in one line"
    try:
        model = Model.objects.get(id=id_name)
    except Model.DoesNotExist:
        model=None
    return model