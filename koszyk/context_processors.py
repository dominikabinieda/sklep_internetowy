from koszyk.models import Koszyk

def koszyk(request):
    return {'koszyk': Koszyk(request)}