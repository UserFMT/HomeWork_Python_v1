import pytest

from stringUtils import StringUtils

@pytest.mark.positive_test
@pytest.mark.parametrize('text, res',
                         # позитивные проверки
                         [('hello', 'Hello'),
                          ('Hello', 'Hello'),
                          (' hello', ' hello'),
                          ('1hello', '1hello'),
                          ('hello, word', 'Hello, word')
                          ])
def test_capitilize_positive(text, res):
    stringutils = StringUtils()
    assert stringutils.capitilize(text) == res

@pytest.mark.negative_test
@pytest.mark.parametrize('text, res', [
                         # негативные проверки
                          (None, None),
                          ('', ''),
                          (' ', ' ')
                         ])
def test_capitilize_negative(text, res):
    stringutils = StringUtils()
    assert stringutils.capitilize(text) == res


@pytest.mark.positive_test
@pytest.mark.parametrize('text, res', [
                         # позитивные проверки
                         (' HELLO', 'HELLO'),
                         ('Hello', 'Hello'),
                         ('    12TEXT', '12TEXT'),
                         ('  Пробел в конце  ', 'Пробел в конце  '),
                         (' ', '')
                         ])
def test_trim_pozitive(text, res):
    stringutils = StringUtils()
    assert stringutils.trim(text) == res

@pytest.mark.negative_test
@pytest.mark.parametrize('text, res', [
                         # негативные проверки
                         ('', ''),
                         (None, None)])
def test_trim_negative(text, res):
    stringutils = StringUtils()
    assert stringutils.trim(text) == res


@pytest.mark.parametrize('text, delimeter, res', [
                         # позитивные проверки
                         ('1,2,3,4', ',', (['1', '2', '3', '4'])),
                         ('er:gf:er', ':', (['er', 'gf', 'er'])),
                         ('er gf :er', ' ', (['er', 'gf', ':er'])),
                         (',er,gf,er', ',', (['', 'er', 'gf', 'er'])),
                         ('er,gf,er,', ',', (['er', 'gf', 'er', ''])),
                         ('1 :2 :3', ' :', (['1', '2', '3'])),
                         # негативные проверки
                         ('1,2,3,4', ' ', (['1,2,3,4'])),
                         ('', ':', ([])),
                         (None, None, None)])
def test_to_list(text, delimeter, res):
    stringutils = StringUtils()
    assert stringutils.to_list(text, delimeter) == res


@pytest.mark.parametrize('text, symbol, res', [
                         # позитивнные проверки
                         (' HELLO', ' ', True),
                         ('Hello', 'l', True),
                         ('Hello', 'G', False),
                         ('Hello', '', False),
                         ('123df 8*sjdfh', ' ', True),
                         # негативные проверки
                         ('Hello', 'll', False),
                         ('123df 8*sjdfh', 8, False),
                         ('', '', False),
                         (None, None, False)])
def test_contains(text, symbol, res):
    stringutils = StringUtils()
    assert stringutils.contains(text, symbol) == res


@pytest.mark.parametrize('text, symbol, res', [
                         # позитивнные проверки
                         (' HELLO', ' ', 'HELLO'),
                         ('Hello', 'h', 'Hello'),
                         ('Hellloll', 'll', 'Helo'),
                         ('hello, work', ' w', 'hello,ork'),
                         ('Hello', 'll', 'Heo'),
                         # негативные проверки
                         ('', '', ''),
                         ('', '123', ''),
                         ('123 ', '', '123 ',),
                         ('Всем привет !', None, 'Всем привет !')])
def test_delete_symbol(text, symbol, res):
    stringutils = StringUtils()
    assert stringutils.delete_symbol(text, symbol) == res


@pytest.mark.parametrize('text, symbol, res', [
                         # позитивнные проверки
                         (' HELLO', ' ', True),
                         ('Hello', 'h', False),
                         ('123!Hello Friend', '1', True),
                         # негативные проверки
                         ('', '', True),
                         (' ', ' ', True),
                         ('Hello', 1, False),
                         (None, None, False)])
def test_starts_with(text, symbol, res):
    stringutils = StringUtils()
    assert stringutils.starts_with(text, symbol) == res


@pytest.mark.parametrize('text, symbol, res', [
                         # позитивнные проверки
                         ('Magadan', 'n', True),
                         ('Magadan', 'N', False),
                         ('Magadan ', ' ', True),
                         ('Magadan 1', '1', True),
                         # негативные проверки
                         ('Magadan', '', True),
                         ('', '', False),
                         ('', '12', False),
                         ('Vector', 'rr', False),
                         (None, None, False)])
def test_end_with(text, symbol, res):
    stringutils = StringUtils()
    assert stringutils.end_with(text, symbol) == res


@pytest.mark.parametrize('text, res', [
                          # позитивнные проверки
                          ('', True),
                          (' ', True),
                          (' fgh ', False),
                          ('W', False),
                          # негативные проверки
                          (None, False),
                          ('\n', False)])
def test_is_empty(text, res):
    stringutils = StringUtils()
    assert stringutils.is_empty(text) == res


@pytest.mark.parametrize('lst, joiner, res', [
                         # позитивнные проверки
                         ([1, 2, 3], ',', '1,2,3'),
                         (["", "f", "y", "6"], ':', ':f:y:6'),
                         ([1, "/", "f", " ", "\n"], ' ', '1 / f   \n'),
                         # негативные проверки
                         ('', '', ''),
                         (None, None, None)])
def test_list_to_string(lst, joiner, res):
    stringutils = StringUtils()
    assert stringutils.list_to_string(lst, joiner) == res
