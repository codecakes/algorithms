def lo_hi(a, lo, hi):
    mid = (lo+hi)/2
    #print lo, mid, hi
    if mid>0 and lo<hi and mid!=lo:
        lo_hi(a, lo, mid)
        lo_hi(a, mid, hi)
    else:
        print a[lo:hi]
    return

a = range(6)

lo_hi(a, 0, len(a))