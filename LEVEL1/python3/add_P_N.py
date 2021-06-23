def solution(absolutes, signs):
    signs = [1 if a else -1 for a in signs]
    return sum([a*s for a, s in zip(absolutes, signs)])

def othersolution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))