#!/usr/bin/env python3

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
moreblocks.py (Release 1.0.0)
=============----------------------------------------------------------------------
(C) in 2016 by Norman Markgraf (nmarkgraf (at) hotmail (dot) com

Pandoc moreblocks filter
Reimplemented all in phyton under panflute.
Older releases (<1.9) are written in Haskel
but only worked with pandoc before 1.17.0.3!


History (Pyhton3 and panflute):
-------------------------------
Release 1.0.0 nm (08.12.2016) New code! Now Pyhton3 and panflute as grid.


Please try PEP8 ! ;-)

> pep8 --show-source --first moreblocks-2.py

Problems?
    - maybe you should use "#!/usr/bin/env python" as first line? ;-)pandoc
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
from panflute import (Header, Plain, RawInline, RawBlock,
                      toJSONFilter, debug, Block, MetaInlines)

blockmap = {
    'theorem':      'Satz',
    'definition':   'definition',
    'exercise':     'Uebung',
    'example':      'Beispiel',
    'examples':     'examples',
    'proof':        'Beweis',
    'remark':       'Bemerkung',
    'remarks':      'Bemerkungen',
    'fact':         'Fakt',
    'facts':        'Fakten',
    'lemma':        'Lemma',
    'solution':     'Loesung'
}

"""
"""
def prepare(doc):
    debug('Starting "moreblocks.py" ...')
    for key in blockmap:
        tmp = doc.get_metadata('moreblocks.'+key, blockmap[key])
        if isinstance(tmp, MetaInlines):
            tmp = tmp.content[0].text
            debug(tmp)
            debug('Changing '+key+'='+blockmap[key]+' to '+key+'='+tmp)
            blockmap[key] = tmp


def finalize(doc):
    debug('Ending "moreblocks.py" ...')


def endTag(tag):
    return '\\end{'+tag+'}\n'


def moreblocks(e, doc):
    # print(doc.format)
    if doc.format == "latex" or doc.format == "beamer":

        if isinstance(e, Header):
            # debug(e)
            if e.level == 4:
                tag = ""
                label = '\\label{' + e.identifier + '}' if e.identifier else ''
                tag = ''
                for key in blockmap:
                    if key in e.classes:
                        tag = blockmap[key]
                if tag == '':
                    if 'endblock' in e.classes:
                        return Plain()  # RawBlock('\\relax', format='latex')?
                    else:
                        return

                left = RawInline('\\begin{'+tag+'}[', format='latex')
                right = RawInline(']'+label+'\n', format='latex')

                n = Plain()
                n.content = [left] + list(e.content) + [right]
                i = 1
                # debug(doc.content[e.index+i])
                while not(isinstance(doc.content[e.index+i], Header)):
                    i += 1
                    # debug(doc.content[e.index+i])

                doc.content.insert(e.index+i,
                                   RawBlock(endTag(tag), format='latex'))
                return n

            else:
                return
        else:
            return
    else:
        return


if __name__ == "__main__":
    toJSONFilter(moreblocks, prepare=prepare, finalize=finalize)
