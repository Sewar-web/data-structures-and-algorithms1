from hashmap_left_join import __version__
from hashmap_left_join.left_join import left_join


def test_version():
    assert __version__ == '0.1.0'

def test_one():
    
    hash = {'fond':'enamored',
    'wrath':'anger',
    'diligent':'employed'
}

    
    hash1 = {'fond':'averse',
    'wrath':'delight',
    'diligent':'idle'
  }
    assert left_join(hash,hash1)==[['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle']]




def test_tow():
    
    hash = {
    'fond':'enamored',
    'wrath':'anger',
    'diligent':'employed',
    'outfit':'garb',
    'guide':'usher'
          }

  
    hash1 = {
    'fond':'averse',
    'wrath':'delight',
    'diligent':'idle',
    'guide':'follow',
    'flow':'jam'
    }

    assert left_join(hash,hash1)==[['fond', 'enamored', 'averse'], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', 'NULL'], ['guide', 'usher', 'follow']]




def test_three():
    
    hash = {
    'outfit':'garb',
    'guide':'usher'
          }

  
    hash1 = {
    'fond':'averse',
    'wrath':'delight',
    'diligent':'idle',
    'guide':'follow',
    'flow':'jam'
    }

    assert left_join(hash,hash1)==[['outfit', 'garb', 'NULL'], ['guide', 'usher', 'follow']]




def test_بخعق():
    
    hash = {
}

    
    hash1 = {
  }
    assert left_join(hash,hash1)==[]

