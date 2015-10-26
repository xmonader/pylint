"""Check exceeding negations in boolean expressions trigger warnings"""

# pylint: disable=singleton-comparison

def unneeded_not():
    """This is not ok
    """
    bool_var = True
    someint = 2
    if not not bool_var:  # [unneeded-not]
        pass
    if not someint == 1:  # [unneeded-not]
        pass
    if not someint != 1:  # [unneeded-not]
        pass
    if not someint < 1:  # [unneeded-not]
        pass
    if not someint > 1:  # [unneeded-not]
        pass
    if not someint <= 1:  # [unneeded-not]
        pass
    if not someint >= 1:  # [unneeded-not]
        pass
    if not not someint:  # [unneeded-not]
        pass
    if not bool_var == True:  # [unneeded-not]
        pass
    if not bool_var == False:  # [unneeded-not]
        pass
    if not bool_var != True:  # [unneeded-not]
        pass
    if not True == True:  # [unneeded-not]
        pass


def not_checked():
    """This is ok"""
    bool_var = True
    someint = 2
    if not(bool_var == False and someint == 1):
        pass