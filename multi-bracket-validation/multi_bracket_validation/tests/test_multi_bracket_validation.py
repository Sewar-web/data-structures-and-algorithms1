from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation
from multi_bracket_validation import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_multi_bracket_validation():
    actual = multi_bracket_validation('()[[Extra Characters]]')
    expected = True
    assert actual == expected

def test_multi_bracket_validation2():
    actual = multi_bracket_validation('({]})}')
    expected = False
    assert actual == expected

def test_multi_bracket_validation3():
    actual = multi_bracket_validation('({())))')
    expected = False
    assert actual == expected

def test_multi_bracket_validation4():
    actual = multi_bracket_validation('[({()})]')
    expected = True
    assert actual == expected