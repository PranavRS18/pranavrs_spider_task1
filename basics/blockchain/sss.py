#Shamir's Secret Sharing Scheme

#Importing Modules
import random

#Largest Prime in 64-bit Computer
p = 1844674473709551557

def find_share(x, polynomial):
    
    share = 0
    for i in range(len(polynomial)):
        share += (polynomial[i] * x ** i)
        
    return (x, share % p)

#Sharing Secret
def create_shares(k, n, secret):
    global polynomial

    #Threshold k < n shares
    if k > n: return print("Less Shares than Threshold")

    #Degree of Polynomial
    degree = k - 1
    
    #Coefficients of Polynomial
    polynomial = [secret] + [random.randint(1, p - 1) for coefficient in range(k - 1)]
    
    #Return Shares
    return [find_share(x, polynomial) for x in range(1, n + 1)]

#Getting the Secret     
def get_secret(shares):
    
    #Taking just k shares
    threshold = len(polynomial)
    if len(shares) < threshold: print("Insufficient shares")
    else: shares = shares[:threshold]
    
    #Getting the Nodes
    nodes = [share[0] for share in shares]
    secret = 0
    
    #Lagrange Interpolation
    for i in range(len(nodes)):
        lagr_func = 1
        for j in range(threshold):
            if i != j:
                lagr_func *= ((-1 * nodes[j]) % p) * pow((nodes[i] - nodes[j]), -1, p)

        secret += lagr_func * shares[i][1]
        
    return secret % p

secret = int(input("Give Secret: "))
threshold = int(input("Enter Threshold: "))
total_shares = int(input("Enter Total Number of Shares: "))

shares = create_shares(threshold, total_shares, secret)
secret = get_secret(shares)
print(shares, secret)