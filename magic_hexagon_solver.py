#!/usr/bin/env python
import itertools

# Return combination of n element in list l whose sum is equal to s
def getFixedSumCombination(l, n, s):
    return [x for x in list(itertools.combinations(l,n)) if sum(x)==s]

# return true if at least one element of l1 is in l2
def shareElts(l1,l2):
    return len([x for x in l1 if x in l2]) != 0

# Return uniq common element between l in lists
# return None if more than one common element
def getUniqCmnElt(lists):
    cmn = None
    flatList = []
    for l in lists:
        flatList += l
    for e in flatList:
        if flatList.count(e) != 1:
            if flatList.count(e) == 3 and ((cmn == None) or (cmn == e)):
                cmn = e
            else:
                return None
    return cmn

# from list of quintuplet whose sum is 38, return all triplets of quintuplets
# who only share one element in common in each quintuplet
def getL5Triplets(c5):
    candidates = []
    for triplet in itertools.combinations(c5,3):
        if (getUniqCmnElt(triplet) != None):
            candidates.append(triplet)
    return candidates


def testTriplet(t5):
    assert(len(t5) == 3)
    assert((len(t5[0]) == len(t5[1])) and (len(t5[0]) == len(t5[2])) and
           (len(t5[0]) == 5))
    # get common element of the triplet
    cmn = getUniqCmnElt(t5)
    assert(cmn != None)

    diags = list()
    # remove common element in lists and store in diags list
    for t in t5:
        diags.append(list(t))
        diags[-1].remove(cmn)

    # create list of candidates for remaining values
    candidates = range(1,20)
    candidates.remove(cmn)
    for d in diags:
        for e in d:
            candidates.remove(e)

    # list containing all permutations for each diag
    permDiags = list()

    for d in diags:
        cd = list()
        # Create all permutation for a diagonal
        for c in itertools.permutations(d):
            l = list(c)
            # reinsert the common element in the middle of the combination
            l.insert(2,cmn)
            cd.append(l)
        # insert permutations 
        permDiags.append(cd)
    #print permDiags
    #p = [permDiags[0][0],permDiags[1][0], permDiags[2][0]]
    for d0 in permDiags[0]:
        for d1 in permDiags[1]:
            for d2 in permDiags[2]:
                perm = [d0,d1,d2]
                testPermutation(perm,candidates)

def testPermutation(p, candidates):
    cornCouples = getCornerCouples(p)
    sol = getMiddleSolution(cornCouples, candidates)
    if sol != None:
        if testTriangles(getVectBoard(p,sol)):
            print(sol)
            print(p)
            print(getVectBoard(p,sol))
            display(getVectBoard(p, sol))



def getCornerCouples(diags):
    cornerVals = []
    for d in diags:
        cornerVals.append(d[0])
    for d in diags:
        cornerVals.append(d[-1])
    couplesCorners = zip(cornerVals, cornerVals[1:] + [cornerVals[0]])
    return couplesCorners

def getMiddleSolution(listCouple, candidates):
    middles = []
    for c in listCouple:
        v = getFinalVal(c)
        if (v not in candidates) or (v in middles):
            return None
        else:
            middles.append(v)
    return middles

def testTriangles(board):
    if (board[1] + board[4] + board[8] + board[12] != 38):
        return False
    if (board[12] + board[13] + board[14] + board[15] != 38):
        return False
    if (board[15] + board[10] + board[5] + board[1] != 38):
        return False
    if (board[3] + board[8] + board[13] + board[17] != 38):
        return False
    if (board[17] + board[14] + board[10] + board[6] != 38):
        return False
    if (board[3] + board[4] + board[5] + board[6] != 38):
        return False
    return True


def getFinalVal(c):
    return 38-sum(c)

#     xx  xx  xx
#   xx  xx  xx  xx
# xx  xx  xx  xx  xx
#   xx  xx  xx  xx
#     xx  xx  xx
def display(board):
    print("    %2d  %2d  %2d" % (board[0], board[1], board[2]))
    print("  %2d  %2d  %2d  %2d" % (board[3], board[4], board[5], board[6]))
    print("%2d  %2d  %2d  %2d  %2d" % (board[7], board[8], board[9], board[10], board[11]))
    print("  %2d  %2d  %2d  %2d" % (board[12], board[13], board[14], board[15]))
    print("    %2d  %2d  %2d" % (board[16], board[17], board[18]))


def getVectBoard(diags, middles):
    vect = []
    vect.append(diags[0][0])
    vect.append(middles[0])
    vect.append(diags[1][0])
    vect.append(middles[5])
    vect.append(diags[0][1])
    vect.append(diags[1][1])
    vect.append(middles[1])
    vect.append(diags[2][4])
    vect.append(diags[2][3])
    vect.append(diags[2][2])
    vect.append(diags[2][1])
    vect.append(diags[2][0])
    vect.append(middles[4])
    vect.append(diags[1][3])
    vect.append(diags[0][3])
    vect.append(middles[2])
    vect.append(diags[1][4])
    vect.append(middles[3])
    vect.append(diags[0][4])
    return vect

def main():
    c5 = getFixedSumCombination(range(1,20), 5, 38)
    triplets = getL5Triplets(c5)
    for triplet in triplets:
        testTriplet(triplet)

if __name__ == "__main__":
    main()