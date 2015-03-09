import sys

from hexlighter.core import *
from hexlighter import conf
from hexlighter.termrenderer import TermRenderer

def main():
    if conf.file:
        f = open(conf.file, "r")
    else:
        f = sys.stdin
    renderer = TermRenderer()
    decoder = CommentedHexDecoder()
    prev = None
    for line in f:
        rbl = decoder.decode(line)
        if prev is not None:
            rbl.ref = prev
        if (prev is None or not conf.master) and not rbl.is_empty():
            prev = rbl
        ebl = EncodedByteList(rbl)
        renderer.render(ebl)
    renderer.finalize()

if __name__ == "__main__":
    main()

