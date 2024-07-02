from Crypto.Util.number import isPrime

class EllipticCurve(object):    #Weierstrass type
    def __init__(self,a,b,p):
        self.a = a
        self.b = b
        self.p = p
        self.O = self.identity()

        if (4*(a**3)+27*(b**2))==0:
            raise Exception("Curve is not smooth")
        if not isPrime(p):
            raise Exception(f"{p} is not prime")

    def __eq__(self,other):
        return (self.a, self.b, self.p) == (other.a, other.b, other.p)

    def __repr__(self):
        s = f"p = {self.p}, y^2 = x^3 "
        if self.a>0:
            s += f"+ {self.a}*x "
        elif self.a<0:
            s += f"- {-self.a}*x "
        if self.b>0:
            s += f"+ {self.b}"
        elif self.b<0:
            s += f"- {-self.b}"
        return s
    
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

    def point(self,x,y):
        return self.Point(self,x,y)

    class Point(object):
        def __init__(self,outer,x,y):            
            self.curve = outer
            p = self.curve.p
            self.x = x % p
            self.y = y % p
            
            if pow(self.y,2,p) != (pow(self.x,3,p) + ((self.curve.a * self.x)%p) + self.curve.b)%p:
                raise Exception(f"Point ({self.x},{self.y}) does not lie on curve")

        def __repr__(self):
            return f"({self.x},{self.y})"

        def __eq__(self,other):
            return (self.curve, self.x, self.y)==(other.curve, other.x, other.y)

        def __neg__(self):
            return self.curve.Point(self.curve,self.x, -self.y)

        def __pos__(self):
            return self

        def __add__(self,Q):
            l = 0
            p = self.curve.p
            a = self.curve.a
            if isinstance(Q,self.curve._identity):
                return self

            x1,y1,x2,y2 = self.x, self.y, Q.x, Q.y
            if (x1==x2) and (y1==p-y2):
                return self.curve.O

            if self==Q:
                l = ((((3*pow(x1,2,p))%p)+a)%p * pow((2*y1),-1,p)) % p
            else:
                ydiff = (p + y2 - y1)%p
                xdiff = (p + x2 - x1)%p
                l = (ydiff * pow(xdiff,-1,p))%p

            x3 = (pow(l,2,p) + (2*p) - x1 - x2)%p
            y3 = ((l*((p+x1-x3)%p))%p + p - y1) % p
            return self.curve.Point(self.curve,x3,y3)

        def __sub__(self,Q):
            return self+(-Q)

        def __mul__(self,n):
            Q = self
            R = self.curve.O
            while (n>0):
                if (n%2==1):
                    R = R+Q
                Q = Q+Q
                n = n//2
            return R

        def __rmul__(self,n):
            return self.__mul__(n) 


E = EllipticCurve(497,1768,9739)

X = E.point(5323,5438)
assert X*1337 == E.point(1089,6931)

P = E.point(2339,2213)
Q = P*7863

print('crypto{'+f'{Q.x},{Q.y}'+'}')
