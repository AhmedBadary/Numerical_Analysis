import simpson as simp

def quad(f, a, b, n):
    first = simp.simpson(f, a, (a+b)/2, n)
    second = simp.simpson(f, (a+b)/2, b, n)
    print(first)
    print(second)
    return first + second

n = 2
def f(x):
    return 2 / (x**2 - 4)
a, b =  0,0.35

print(quad(simp.f, simp.a, simp.b, simp.n))