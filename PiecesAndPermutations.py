def fat(n):
    k = n
    r = 1
    while k>0:
        r*=k
        k-=1
    return r

def nxnpieces(n):
    return 6*n**2 - 12*n + 8

def nxnperms(n):
    if n%2==1:
        return fat(7) * 3**6 * fat(12) * 2**10 * fat(24)**((n-3)/2) * (fat(24)/(fat(4)**6))**(((n-2)**2 - 1)/4) * 24
    else:
        return fat(7) * 3**6 * fat(24)**((n-2)/2) * (fat(24)/(fat(4)**6))**((n-2)**2/4)

def minxpieces(n):
    if n%2==1:
        return 15*n**2 - 30*n + 17
    else:
        return 15*n**2 - 30*n + 20

def minxperms(n):
    if n%2==1:
        return fat(19) * 3**18 * 60 * fat(30) * 2**(27-(n-3)/2) * fat(60)**((n-3)/2) * (fat(60)/(fat(5)**12))**((n**2 -4*n + 3)/4)
    else:
        return fat(19) * 3**18 * 2**(-1 - (n-2)/2) * fat(60)**((n-2)/2) * (fat(60)/(fat(5)**12))**((n**2 - 4*n + 4)/4)

def pyrapieces(n):
    return 4*n**2 - 12*n + 14

def pyraexp(n):
    if (n**2)%3 == 1:
        return (n**2 - 6*n + 8)/3
    else:
        return (n**2 - 6*n + 9)/3

def pyraperms(n):
    return 3**4 * 3**4 * 12**((n**2)%3) * fat(12)**(n-3) * fat(6) * 2**(7 - n) * (fat(12)/(fat(3)**4))**(pyraexp(n))

def skewbpieces(n):
    return 12*n**2 - 24*n + 14

def skewbperms(n):
    return fat(6) * fat(4) * 3**6 * 2**(-n) * fat(12)**(n-2) * (fat(12)/(fat(2)**6))**(n**2 - 3*n + 2)

def ftopieces(n):
    return 8*n**2 -12*n + 6

def ftoperms(n):
    return fat(5) * 2**(5 - n) * (144)**((n**2)%3) * fat(12)**(n-2) * (fat(12)/(fat(3)**4))**(2*(((n**2 - 3*n + 3)//3)))
