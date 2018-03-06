a=raw_input("")
def CamelCase(praveena):
    import re
    return ''.join(x.capitalize() or '_' for x in praveena.split('_'))
print CamelCase(a)
