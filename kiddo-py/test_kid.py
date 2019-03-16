from kid import Kid


def test_kid_asks_mommy_for_food():
    kid = Kid()
    answer = kid.ask_mommy_for_food()
    assert answer == 'yes'


def test_kid_asks_daddy_for_food():
    kid = Kid()
    answer = kid.ask_daddy_for_food()
    assert answer == 'yes'
