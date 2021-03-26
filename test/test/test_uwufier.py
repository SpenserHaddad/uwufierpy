from uwufier import uwufy


def test_uwufy_hello_world():
    uwud = uwufy("hello world!")
    assert uwud == "hewwo wowwd!"