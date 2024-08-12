import random, sys, os, Cryptomath, rabinMiller


def generateKey(keySize):
    print("Generating p prime....")
    p = rabinMiller.generateLargePrime(keySize)
    print("Generating q prime...")
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if Cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print("Calculating d that is mod inverse of e...")
    d = Cryptomath.findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print(" Genrate public key: done")
    print(" Genrate private key: done ")
    print("have fun chatting with more secure ")
    return (publicKey, privateKey)