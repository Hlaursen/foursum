from __future__ import print_function
import sys
import time

# Record experiment timing here
outfile = open("pythonSimpleRuntimes.txt", "a")

N = int(sys.stdin.readline())
vals = list(map(int, sys.stdin.readlines()))

# Timing experiments
time1 = time.time()

for i in range(0, N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            for l in range(k+1,N):
                if vals[i]+vals[j]+vals[k]+vals[l] == 0:
                    print(i,j,k,l,file=sys.stderr)
                    print(True)

                    # Code for timing experiments
                    time2 = time.time()
                    timediff = time2-time1
                    print("Time to process: {0}", timediff)
                    outfile.write("True {0} {1} {2} {3} {4}\n".format(vals[i], vals[j], vals[k], vals[l], timediff))
                    outfile.close()

                    sys.exit()
print(False)

# Code for timing experiments
time2 = time.time()
timediff = time2-time1
outfile.write("False {0}\n".format(timediff))
outfile.close()
