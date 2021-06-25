from ll_zip.ll_zip import LinkedList ,zip_ll
from ll_zip import __version__

def test_version():
    assert __version__ == '0.1.0'


def test_zip_one():
    ll1=LinkedList()
    ll1.append(5)
    ll1.append(7)
    ll1.append(0)
    ll2=LinkedList()
    ll2.append(15)
    ll2.append(17)
    expect='{5}->{15}->{7}->{17}->{0}->None'
    actuall=str(zip_ll(ll1 ,ll2))
    assert actuall==expect


def test_zip_tow():
    ll1=LinkedList()
    ll1.append(5)
    ll1.append(7)
    ll2=LinkedList()
    ll2.append(15)
    ll2.append(17)
    expect='{5}->{15}->{7}->{17}->None'
    actuall=str(zip_ll(ll1 ,ll2))
    assert actuall==expect


