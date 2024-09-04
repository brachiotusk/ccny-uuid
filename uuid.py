import hashlib
import hmac
import numpy as np
import math
import operator
from random import seed
from random import randint

class DRBG(object):
        def __init__(self, key, seed):
            self.key = key
            self.val = b'\x01' * 64
            self.reseed(seed)
            self.byte_index = 0
            self.bit_index = 0

        def hmac(self, key, val):
            return hmac.new(key, val, hashlib.sha512).digest()

        def reseed(self, data=b''):
            self.key = self.hmac(self.key, self.val + b'\x00' + data)
            self.val = self.hmac(self.key, self.val)

            if data:
                self.key = self.hmac(self.key, self.val + b'\x01' + data)
                self.val = self.hmac(self.key, self.val)

        def generate_bits(self, n):
            xs = np.zeros(n, dtype=bool)
            for i in range(0,n):
                xs[i] = (self.val[self.byte_index] >> (7 - self.bit_index)) & 1

                self.bit_index += 1
                if self.bit_index >= 8:
                    self.bit_index = 0
                    self.byte_index += 1

                if self.byte_index >= 8:
                    self.byte_index = 0
                    self.val = self.hmac(self.key, self.val)

            self.reseed()
            return xs
class Generate(object):
    def __init__ (self,key,seed):
        self.Buffer = b''
        self.counter = 0
        self.DRBG = DRBG(self,key,seed)
        self.KeyBuffer = b''
    def store(self):
        xc = b''
        l = len(self)
        closePower = 2 ** math.ceil(math.log2(l))
        HMACEncoded = self.DRBG.generate_bits(self, closePower)
        return (self.val >> self) & closePower
    def XOR(self, n):
        ll = Generate.store(self)
        final = b''
        for x in range(0,n):
            enc = operator.xor(self, self.val)
            final = final + enc
        return final

    def addBuffer(self):
        am = Generate.store(self)
        if(len(self.Buffer) > 0):
            for x in range(0, self.Buffer):
                a = self.DRBG.reseed(self, 1)
                self.DRBG.generate_bits(self, 1)
                c = bin((self.val >> x) & 1)
                xc = xc + c
                self.counter = self.counter + 1
                return xc
    def KeyXC(self)
        for y in range(0, len(self.val)):
            while(self.counter < self.Buffer)
                a = Generate.XOR(self, (Generate.addBuffer(self) >> y) & 1)
                self.val[y] = a
            b = Generate.XOR(self, self.val >> (y + self.counter) & 1)
            self.val[y+self.counter] = b
class UUID(object):
    def __init__(self, key, seed):
        uuid = Generate(key, seed)
        self.uuid4 = b''
    def randA(self):
        x = 0
        while(x<48):
            a = (self.val >> x) & 1
            self.uuid4 = self.uuid4 + a
    def randB(self):
        x = 48
        while(x<60):
            a = (self.val >> x) & 1
            self.uuid4 = self.uuid4 + a
    def randC(self):
        x = 60
        while(x<102):
            a = (self.val >> x) & 1
            self.uuid4 = self.uuid4 + a
    def format(self):
        ver = b'0b0100'
        var = b'0b10'
        UUID.randA()
        self.uuid4 + ver
        UUID.randB()
        self.uuid4 + var
        UUID.randC()
        return self.uuid4
class uuid(object):
    def __init__(self):
        seed(1)
        rand = b'' 
    def a(rand):
        a = 0
        while(a < 48):
            x = randint(0, 10)
            rand[a] = x
    def ver(self, rand):
        self.rand + b'0b0100'
    def b(rand):
        b = 52
        while(b < 64):
            y = randint(0, 10)
            rand[b] = y
    def var(self, rand):
        self.rand + b'0b10'
    def c(rand):
        c = 64
        while(c < 128):
            z = randint(0, 10)
            rand[c] = z
    def out(rand):
        return rand
class XOR(object):
    def __init__(self):
        one = UUID()
        two = uuid()
        three = b'' * 128
    def xor(one, two, three):
        n = len(one)
        for x in range(0,n):
            a = operator.xor(one[n], two[n])
            three[n] = a
    def final(three):
        ver = b'0b0100'
        var = b'0b10'
        three[48] = b'0b'
        three[49] = b'01'
        three[50] = b'0'
        three[51] = b'0'
        three[64] = b'0b'
        three[65] = b'10'
        return three











