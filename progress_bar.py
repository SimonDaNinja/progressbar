def PrintProgressBar(i,n,barlength=40, final = None, postMessage = ""):
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
    print(statusString + barString + " " + postMessage, end = "\r", flush=True)
    if final is None:
        final = i>=n
    if final:
        print("Done!")

if __name__ == "__main__":
    import time
    import random
    k = 0
    d = 3
    dApprox = d
    i = 0
    tot = 5000


    k += 1

    while i<tot:
        i += d
        i = min(i,tot)
        d = max(min(d+random.uniform(-5,5),20),0)
        dApprox = dApprox*.9 + d*.1
        PrintProgressBar(i,tot, final = i==tot, postMessage = "current progress speed: " + str(round(dApprox,3)))
        time.sleep(.05)
