#!/usr/bin/python
import json

#filepath = sys.argv[1]
#file = open(filepath)
#json_info = json.load(file)

def pr(thing_to_print, num_indents):
    indent = "   "
    s = indent * num_indents
    return s + thing_to_print

def format(js, indents):
    formatted = ""
    formatted += pr("{\n", indents)
    for item in js:
        valtype = type(js[item]).__name__
        if valtype == 'dict':
            formatted += pr('"'+item+'"'+':\n', indents+1)
            formatted += format(js[item], indents+1)
        elif valtype == 'unicode':
            formatted += pr('"{}": "{}",\n'.format(item, js[item]), indents + 1)
        else:
            formatted += pr('"{}": {},\n'.format(item, js[item]), indents + 1)
    if indents == 0:
        formatted += pr("}", indents)
    else:
        formatted += pr("},\n", indents)
    return formatted

def combineDicts(dicts):
    ret = {}
    for d in dicts:
        for item in d:
            valtype = type(d[item]).__name__
            try:
                if valtype == 'list':
                    ret[item].extend(d[item])
                    ret[item] = list(set(ret[item]))
                elif valtype == 'dict':
                    ret[item] = combineDicts([ret[item], d[item]])
                else:
                    ret[item].append(d[item])
            except KeyError:
                if valtype == 'list' or valtype == 'dict':
                    ret[item] = d[item]
                else:
                    ret[item] = [d[item]]
    return ret

