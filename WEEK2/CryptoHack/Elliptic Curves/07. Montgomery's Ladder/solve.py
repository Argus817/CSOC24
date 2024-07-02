from Crypto.Util.number import isPrime
from sage.all import sage,Mod

class finiteField(object):
    def __init__(self,p: int):
        self.p = p

        if not isPrime(p):
            raise Exception(f"{p} is not Prime")

    def __repr__(self):
        return f"Finite Field mod prime {self.p}"

    def __eq__(self, other):
        return self.p==other.p

    def num(self, n):
        return self.Element(self,n)

    class Element(object):
        def __init__(self,outer,n):
            self.field = outer
            p = self.field.p
            self.n = n % p

        def __repr__(self):
            return f'{self.n} mod {self.field.p}'

        def __int__(self):
            return self.n

        def __eq__(self, other):
            return (self.n, self.field) == (other.n, other.field)

        def __neg__(self):
            num = self.field.p - self.n
            return self.field.Element(self.field, num)

        def __pos__(self):
            return self

        def __add__(self, other):
            if self.field != other.field:
                raise Exception(f"Fields don't match for {self.n} and {other.n}")

            p = self.field.p
            num = (self.n + other.n) % p
            return self.field.Element(self.field, num)

        def __sub__(self,other):
            if self.field != other.field:
                raise Exception(f"Fields don't match for {self.n} and {other.n}")

            return self + (-other)

        def __mul__(self, other):
            if self.field != other.field:
                raise Exception(f"Fields don't match for {self.n} and {other.n}")

            p = self.field.p
            num = (self.n * other.n) % p
            return self.field.Element(self.field, num)
        
        def __pow__(self, power: int):
            p = self.field.p
            if power == -1:
                num = pow(self.n, -1, p)
                return self.field.Element(self.field, num)

            if power < 0:
                return (self**(-1))**(-power)

            if power >=0:
                return self.field.Element(self.field, pow(self.n, power, self.field.p))

        def __truediv__(self, other):
            if self.field != other.field:
                raise Exception(f"Fields don't match for {self.n} and {other.n}")

            return self * (other**-1)

        def __floordiv__(self,other):
            return self/other

class MontgomeryCurve(object):
    def __init__(self, a,b,p):
        self.field = finiteField(p)
        self.a = self.field.num(a)
        self.b = self.field.num(b)
        self.O = self.identity()
    
    def __eq__(self,other):
        return (self.a, self.b, self.field)==(other.a, other.b, other.field)

    def __repr__(self):
        s = ""
        if self.b.n == 0:
            s += '0 = x^3 '
        elif self.b.n == 1:
            s += 'y^2 = x^3 '
        else:
            s += f'{self.b.n}*y^2 = x^3 '
        if self.a.n == 0:
            s += f'+ x'
        elif self.a.n == 1:
            s += '+ x^2 + x'
        else:
            s += f'+ {self.a.n}*x^2 + x'
        return s+f', p = {self.field.p}'

    def identity(self):
        return self._identity(self)

    class _identity(object):
        def __init__(self,outer):
            self.curve = outer

        def __repr__(self):
            return f"Identity"

        def __pos__(self):
            return self

        def __neg__(self):
            return self

        def __add__(self,Q):
            return Q

        def __sub__(self,Q):
            return -Q

    def point(self,x,y=None):
        if y==None:
            X = self.field.num(x)
            a = self.a
            b = self.b
            y_squared = (X**3 + a*(X**2) + X)/b
            y = int(sage.rings.finite_rings.integer_mod.square_root_mod_prime(Mod(y_squared.n,self.field.p)))
        return self.Point(self,x,y)

    class Point(object):
        def __init__(self,outer,x,y):
            self.curve = outer
            self.field = outer.field
            self.x = self.field.num(int(x))
            self.y = self.field.num(int(y))

            a = self.curve.a
            b = self.curve.b
            X = self.x
            Y = self.y
            if b*(Y**2) != X**3 + a*(X**2) + X:
                raise Exception(f'Point ({X.n},{Y.n}) does not lie on curve')

        def __repr__(self):
            return f'({self.x.n},{self.y.n})'

        def __eq__(self,other):
            return (self.curve, self.x, self.y)==(other.curve, other.x, other.y)

        def __neg__(self):
            return self.curve.Point(self.curve, self.x, -self.y)

        def __pos__(self):
            return self

        def __add__(self, Q):
            if self.curve != Q.curve:
                raise Exception("Curves don't match in addition")

            if isinstance(Q,self.curve._identity):
                return self

            A,B = self.curve.a, self.curve.b
            x1, y1, x2, y2 = self.x, self.y, Q.x, Q.y
            f3, f2, f1 = self.field.num(3), self.field.num(2), self.field.num(1)
            if self==Q:
                a = (f3*(x1**2) + f2*A*x1 + f1)/(f2*B*y1)
                x3 = B*(a**2) - A - f2*x1
                y3 = a*(x1-x3) - y1
            else:
                a = (y2-y1)/(x2-x1)
                x3 = B*a*a - A - x1 - x2
                y3 = a*(x1-x3) - y1
            return self.curve.Point(self.curve, x3, y3)

        def __sub__(self,Q):
            if self.curve != Q.curve:
                raise Exception("Curves don't match in subtraction")

            return self+(-Q)

        def __mul__(self, k: int):
            P = self
            if k==2:
                return self+self
            
            R0, R1 = P, P+P
            k = bin(k)[2:][::-1]
            l = len(k)
            for i in range(l-2,-1,-1):
                if k[i] == '0':
                    R0, R1 = R0+R0, R0+R1
                else:
                    R0, R1 = R0+R1, R1+R1
            return R0

        def __rmul__(self, k: int):
            return self.__mul__(k)

C = MontgomeryCurve(486662,1,pow(2,255)-19)
G = -C.point(9)
n = int('0x1337c0decafe', base=16)

assert G+G+G+G+G+G+G+G+G == 9*G
Q = n*G

print('crypto{',int(Q.x),'}',sep='')
