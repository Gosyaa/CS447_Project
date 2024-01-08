import json

class RSA:

    def __init__(self):
        self.p = 29
        self.q = 83
        self.e = 23
        self.d = 599
        self.N = self.p * self.q
        self.x, self.y = [0], [0]
        self.dp = self.d % (self.p - 1)
        self.dq = self.d % (self.q - 1)
        self.ex_gcd(self.q, self.p, self.x, self.y)
        self.q_inv = self.x[0] % self.p

    def fast_power(self, a, p, N):
        ans = 1
        while p > 0:
            if p % 2 == 1:
                ans = (ans * a) % N
            a = (a * a) % N
            p //= 2
        return ans

    def ex_gcd(self, a, b, x, y):
        if a == 0:
            x[0] = 0
            y[0] = 1
            return b

        x1, y1 = [0], [0]
        gcd = self.ex_gcd(b % a, a, x1, y1)
        x[0] = y1[0] - (b // a) * x1[0]
        y[0] = x1[0]
        return gcd

#    p, q, e, d = 29, 83, 23, 599  # Keys and encryption module, and prime numbers p and q
#    N = p * q
#    dp, dq = d % (p - 1), d % (q - 1)
#    x, y = [0], [0]
#    ex_gcd(q, p, x, y)
#    q_inv = x[0] % p
#
    def encrypt(self, s):
        n = len(s)
        encr = [self.fast_power(ord(s[i]), self.e, self.N) for i in range(n)]
        res = json.dumps(encr)
        return res
    
    def decrypt(self, s):
        encr = json.loads(s)
        n = len(encr)
        decr = [0] * n
        str_res = ""
        for i in range(n):
            decr1 = self.fast_power(encr[i], self.dp, self.p)
            decr2 = self.fast_power(encr[i], self.dq, self.q)
            h = (self.q_inv * (decr1 - decr2)) % self.p

            if decr1 < decr2 and h != 0:
                h = self.p + h

            decr[i] = (decr2 + h * self.q) % self.N
            str_res += chr(decr[i])
        return str_res