import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def combination(x,n):
    return factorial(n) / (factorial(x) * factorial(n-x))

def binominal(x,n,p):
    return combination(x,n) * (p**x) * ((1-p)**(n-x))

def makegraph(n, p, i):
    global ax
    row = list(range(n))
    col = []
    for x in range(n):
        col.append(binominal(x,n,p))
    
    ax[i].plot(row, col, label = f"n = {n}")
    

fig, ax = plt.subplots(3,1)
fig.subplots_adjust(hspace=1)
for i in range(1,4):
    for j in range(10, 51, 10):
        makegraph(j, i/6, i-1)
    ax[i-1].set_title(f"p={i/6:.3}일 때의 이항분포")
    ax[i-1].legend()

plt.show()
fig.savefig("binominal graph.png")