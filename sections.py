#!/usr/bin/env python3

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
sections.py (Release 1.0.0)
============-----------------------------------------------------------------------
(C) in 2017 by Norman Markgraf (nmarkgraf (at) hotmail (dot) com



History (Pyhton3 and panflute):
-------------------------------
Release 1.0.0 nm (19.01.201/) Initial Release


Please try PEP8 ! ;-)

> pep8 --show-source --first splitblockold.py

Problems?
    - maybe you should use "#!/usr/bin/env python" as first line? ;-)pandoc
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
from panflute import (Header, Plain, RawInline, RawBlock, Span,
                      toJSONFilter, debug, Block, MetaInlines)


sectionlist = []

def prepare(doc):
    debug('Starting "sections.py" ...')


def finalize(doc):
    global sectionlist
    inc = 0
    for (pos, name) in sectionlist:
        debug("adding : "+name+" at $pos")
        doc.content.insert(pos+inc, RawBlock("\n\\section*{"+name+"}\n", format="latex"))
        inc = inc + 1
    debug('Ending "sections.py" ...')


def sections(e, doc):
    # print(doc.format)
    if doc.format == "latex" or doc.format == "beamer":

        if isinstance(e, Header):
            # debug(e)
            if e.level == 2 :
                if "section" in e.classes:
                    newsection = e.attributes['name']
                    global sectionlist 
                    sectionlist += [(e.index, newsection)]
                    debug('new section:'+ newsection)
                    return
            else:
                return
        else:
            return
    else:
        return


if __name__ == "__main__":
    toJSONFilter(sections, prepare=prepare, finalize=finalize)
