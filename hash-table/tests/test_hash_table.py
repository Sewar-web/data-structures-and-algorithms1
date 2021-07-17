
from typing import Hashable
from hash_table.hash_table import Hashtable
from hash_table import __version__


def test_version():
    assert __version__ == '0.1.0'


table=Hashtable(1024)


def test_add():
   
   table.add('sewar',"cat")
   assert table.map[table.hash('sewar')].head.data== ('sewar', 'cat')

def test_GetValue_from_key():
   
   table.add('swar',"cookies")
   assert table.get('swar')=="cookies"




def test_not_exist():
   
   assert table.get('asd')=='null'


def test_handle_collision():
   
   table.add('ahmad',12)
   assert table.map[table.hash('ahmad')].head.data==  ('ahmad', 12)



def test_retrieve_collision():
   
   table.add('ahmad',12)
   table.add('hamad',"oreo")

   assert table.get('ahmad')==12
   assert table.get('hamad')=='oreo'




def test_hash_in_range():
   table.add('thrwat',"mom")
   table.add('doaa',"friend")
   table.add('deaa',"bro")

   assert table.hash('thrwat')==366
   assert table.hash('doaa')== 527
   assert table.hash('doaa') <= 1024

  

