"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""
def fn_hack_10():
    result="fooziman"
    reemplazo = {
        'f': 'F',
        'o': '0',
        'z': 'Z',
        'i': '1',
        'm': 'M',
        'a': '@',
        'n': 'N'
    }
    result_mod= []
    for caracter in result:
        caracter_mod = reemplazo.get(caracter, caracter)
        result_mod.append(caracter_mod)
    return result_mod

