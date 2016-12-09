import os
from django.contrib.gis.utils import LayerMapping
from sig.models import Distrito

dict_mapping = {
    'codigo' : 'codigo',
    'nombre' : 'nombre',
    'provincia' : 'provinciai',
    'geom' : 'MULTIPOLYGON',
}

shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'DISTRITOS.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Distrito, shp, dict_mapping,
    )
    lm.save(strict=True, verbose=verbose)