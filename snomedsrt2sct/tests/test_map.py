from snomedsrt2sct import map


def test_ok():
    # 976004,T-48780,Structure of ovarian vein (body structure)
    val = map('T-48780')
    assert val['SCT'] == '976004'


def test_no_mapping():
    val = map('INVALID_VALUE')
    assert val is None

def test_leading_whitespaces():
    val = map('    T-48780')
    assert val['SCT'] == '976004'


def test_trailing_whitespaces():
    val = map('T-48780    ')
    assert val['SCT'] == '976004'