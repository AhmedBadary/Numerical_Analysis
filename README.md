# Numerical_Analysis
Implementations of various algorithms and methods in Numerical Analaysis

## 1. Newtons Method

## 2. The Bisection Method

## 3. Newton-Bisection Method
   Implements a function, **newton_bisection**, with signature\\
   function [p] = newton_bisection(f,df,a,b,tol)\\
   that attempts to approximate a root **p** ∈ **[a, b]**, with **|f(p)| < ε**.\\
   **df** is a function that returns **f′(x)**, and **ε = tol**.\\

    Using the following strategy:   
        1.  Set p = a.
        2.  Attempt one step of Newton’s method:
                p = p − f(p)/f′(p).
        3.  If p does not lie in the interval [a, b], 
                set p = 0.5*(a+b)  [according to the bisection method].
        4.  If sgn(f(a)) * sgn(f(p)) < 0, 
                set b = p,
            Else,
                set a = p.
        5.  If |f(p)| < ε,
                Terminate
            Else,
                return to step 2.

## 4. Find-Interval(Bracket) Method.
   Implements a function **find_bracket** with signature\\
   function [a,b] = find_bracket(f,x0,dx)\\
   which  finds  an  interval  **[a, b]**  with  **sgn(f(a)) sgn(f(b)) < 0**\\  
   (i.e.f (a)  and f(b)  have opposite signs)\\ 

    According to the following method:
        1.  Set a = b = x0.
        2.  Set a = a − ∆x.
            If sgn(f(a)) sgn(f(b)) < 0,
                Terminate.
        3.  Set b = b + ∆x.
            If sgn(f(a)) sgn(f(b)) < 0,
                Terminate.
        4.  Set ∆x = 2*∆x and return to step 2.