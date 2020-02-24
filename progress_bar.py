def PrintProgressBar(i,n,barlength=40, final = False):
    iInt = int(i)
    progressUnits = (barlength*iInt)//n
    # for portability, I avoid f-strings
    statusString = str((100*iInt)//n)
    statusString += " %" + (4-len(statusString))*' '
    barChars = list(barlength*'.')
    barChars[:progressUnits] = ['=' for i in range(progressUnits)]
    barChars[progressUnits-1] = '>'
    barChars.insert(0,'[')
    barChars[barlength] = ']'
    barString = ''.join(barChars)
    print(statusString + barString, end = "\r", flush=True)
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
