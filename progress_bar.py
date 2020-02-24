def PrintProgressBar(i,n,barlength=40, final = False):
    iInt = int(i)
    print(f"{(100*iInt)//n} %" + (4-len(str((100*iInt)//n)))*' ' +  " [" +\
            "="*((barlength*iInt)//n) + (">" if ((barlength*iInt)//n)<barlength\
            else "") + "."*(barlength-(barlength*iInt)//n-1) + "]",
            end="\r",
            flush=True)
    if final:
        print("Done!")

if __name__ == "__main__":
    import time
    import random
    d = 3
    i = 0
    tot = 5000

    while i<tot:
        i += d
        i = min(i,tot)
        d = max(min(d+random.uniform(-5,5),20),0)
        PrintProgressBar(i,tot, final = i==tot)
        time.sleep(.05)
