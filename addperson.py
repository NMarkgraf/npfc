#!/usr/bin/env python3

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
addperson.py (Release 1.0.0)
=============----------------------------------------------------------------------
(C) in 2015/16 by Norman Markgraf (nmarkgraf (at) hotmail (dot) com

Pandoc addperson filter
Implemented all in phyton under panflute.
Older releases (<1.9) are written in Haskel
but only worked with pandoc before 1.17.0.3!

History :
---------
Release 1.0.0 nm (09.12.2016) Initial Concept derived from moreblocks


Please try PEP8 ! ;-)

> pep8 --show-source --first moreblocks-2.py

Problems?
    - maybe you should use "#!/usr/bin/env python" as first line? ;-)pandoc
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
from panflute import (Header, Plain, RawInline, RawBlock,
                      toJSONFilter, debug, Block, MetaInlines)


relax = True
curPerson = ''

def prepare(doc):
    debug('Starting "addperson.py" ...')


def finalize(doc):
    debug('Ending "addperson.py" ...')


def beginPersonTag(person):
    global relax
    global curPerson
    if person == '':
        txt = "\\relax"
        relax = True
    else:
        txt = ("\\begin{columns}[T,onlytextwidth]\n"
               "\t\\begin{column}[t]{0.74\\textwidth}")
        relax = False
        curPerson = person
    return RawBlock(txt, format='latex')


def endPersonTag():
    global relax
    global curPerson
    if relax:
        txt = "\\relax"
    else:
        txt = ("\t\\end{column}\n"
               "\t\\begin{column}{0.24\\textwidth}\n"
                "\t\t\\personDB{"+curPerson+"}\n"
               "\t\\end{column}\n"
               "\\end{columns}\n")
        relax = True
        curPerson = ''
    return RawBlock(txt, format='latex')

def addperson(e, doc):
    # print(doc.format)
    if doc.format == "latex" or doc.format == "beamer":
        if isinstance(e, Header):
            # debug(e)
            if e.level == 3 or e.level == 5:
                if 'personbegin' in e.classes:
                    person = e.attributes['person']
                    return beginPersonTag(person)
                elif 'personend' in e.classes:
                    return endPersonTag()
                else:
                    return
            else:
                return
        else:
            return
    else:
        return
    return


if __name__ == "__main__":
    toJSONFilter(addperson, prepare=prepare, finalize=finalize)
