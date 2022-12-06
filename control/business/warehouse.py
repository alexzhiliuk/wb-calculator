from control.models import Warehouse


def get_warehouse(user):
    try:
        warehouse = user.warehouse
    except:
        warehouse = Warehouse.objects.create(user=user, space=0, occupied_space=0)
        
    return warehouse