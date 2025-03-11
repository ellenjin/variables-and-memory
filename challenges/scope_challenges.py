def challenge_01():
    # 1: local (42)
    outer_value = 42

    print(f"The value from outside is: {outer_value}")

def challenge_02():
    # 2: global (1729)
    print(f"The value from outside is: {outer_value}")

def challenge_03():
    # 3: we declare after we try to call 'inner_value' -- error
    print(f"The value from outside is: {inner_value}")

    inner_value = 42

def challenge_04():
    # 4: accesses global, not local. Python always assumes local unless explicitly global, so the difference
    # between this one and challenge 2 is that the variable is being declared locally
    print(f"The value from outside is: {outer_value}")

    outer_value = 42

outer_value = 1729