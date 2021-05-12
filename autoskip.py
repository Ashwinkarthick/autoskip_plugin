import util, cadnano

def skipExtraBp(part, settings):
    tbp = settings.get('targetBpbetweenSkip')
    noi = settings.get('numOfSkip')
    initOffset = settings.get('initialPosition')
    incr = 1
    if part != None:
        initPos = -1
        offset = initOffset 
        for vh in part.getVirtualHelices():
            scafSS = vh.scaffoldStrandSet()
            y = 0
            for strand in scafSS:
                lo, hi = strand.idxs()
                if strand.hasInsertion():
                    for ins in strand.insertionsOnStrand():
                        if ins.isSkip():
                            strand.removeInsertion(ins.idx())
                if initPos == -1:
                    initPos = lo + offset
                numOfBp = ((hi - lo) // tbp) + noi
                for x in range(0, numOfBp):
                    rangeOffset = initPos + (y * tbp)
                    if (rangeOffset <= hi):
                        strand.addInsertion(rangeOffset, -1)
                        if noi > 1:
                            strand.addInsertion((rangeOffset+1), -1)    
                        y += 1
                    incr += 1
# end def


cadnano.app().skipExtraBp = skipExtraBp
