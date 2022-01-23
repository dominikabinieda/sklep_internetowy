from .koszyk import Koszyk

def koszyk(request):
    return {'koszyk': Koszyk(request)}