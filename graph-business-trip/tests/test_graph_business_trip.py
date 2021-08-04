from graph_business_trip import __version__
from graph_business_trip.business_trip import Graph 


def test_version():
    assert __version__ == '0.1.0'


def test_trip():
    g=Graph()
    a=g.add_node('Pandora')
    b=g.add_node('Arendelle')
    c=g.add_node('Metroville')
    d=g.add_node('Monstropolis')
    e=g.add_node('Naboo')
    f=g.add_node('Narnia')

    g.add_edge(b,a,150)  
    g.add_edge(c,a,82)   
    g.add_edge(c,b,99)
    g.add_edge(b,d,42)
    g.add_edge(d,b,42)
    g.add_edge(c,f,37)
    g.add_edge(d,e,73)
    g.add_edge(f,e,250)
    
   
    assert g.business_trip(['Naboo', 'Pandora'])=='False,$0'

    assert g.business_trip(['Naboo', 'Narnia'])=='False,$0'

    assert g.business_trip(['Metroville', 'Pandora',])=='True,$82'

    assert g.business_trip(['Arendelle', 'Pandora',])=='True,$150'

    assert g.business_trip(['Narnia', 'Naboo',])=='True,$250'

    assert g.business_trip(['Metroville', 'Arendelle',])=='True,$99'

    assert g.business_trip(['Arendelle', 'Monstropolis', 'Naboo'])=='True,$115'




   
