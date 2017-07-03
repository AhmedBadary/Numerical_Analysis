# Numerical_Analysis
Implementations of various algorithms and methods in Numerical Analaysis

## 1. Newtons Method
   Implements a function, **newton**, with signature\\
   function [p] = newton(f,df,p0,tol)\\
   that attempts to approximate a root **p**, where **|p_N - p_(N-1)| < ε**.\\
   **df** is a function that returns **f′(x)**, and **ε = tol**.\\

    Using the following strategy:   
        1. Set i = 1.
        2. While i ≤ N0 do Steps 3–6.
            3. Set p = p0 − f(p0)/f'(p0). (Compute p_i.)
            4. If | p − p0| < TOL then,
                    OUTPUT (p); (The procedure was successful.)
                    STOP.
            5. Set i = i + 1.
            6. Set p0 = p. (Update p0.)
        7. OUTPUT (‘The method failed after N0 iterations, N0 =’, N0);
            (The procedure was unsuccessful.)
            STOP.

## 2. The Bisection Method
   Implements a function, **bisection**, with signature\\
   function [p] = bisection(f,a,b,tol,)\\
   that attempts to approximate a root **p**, where **|p_N - p_(N-1)| < ε**.\\
   **df** is a function that returns **f′(x)**, and **ε = tol**.\\

    Using the following strategy:   
        1. Set i = 1; 
                FA = f(a).
        2. While not converged do Steps 3–6.
            3. Set p = a + (b − a)/2; (Compute pi.)
                    FP = f ( p).
            4. If FP = 0 or (b − a)/2 < TOL then
                    OUTPUT (p); (Procedure completed successfully.)
                    STOP.
            5. Set i = i + 1.
            6. If FA · FP > 0 then set a = p; (Compute ai, bi.)
                    FA = FP
               else set b = p. (FA is unchanged.)
        7. OUTPUT (‘Method failed after N0 iterations, N0 =’, N0);
                (The procedure was unsuccessful.)
                STOP.

## 3. Newton-Bisection Method
   Implements a function, **newton_bisection**, with  
   signature: function [p] = newton_bisection(f,df,a,b,tol)  
   that attempts to approximate a root **p** ∈ **[a, b]**, with **|f(p)| < ε**.  
   **df** is a function that returns **f′(x)**, and **ε = tol**.  

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
   Implements a function **find_bracket** with   
   signature: function [a,b] = find_bracket(f,x0,dx)  
   which  finds  an  interval  **[a, b]**  with  **sgn(f(a)) sgn(f(b)) < 0**  
   (i.e. f(a)  and f(b)  have opposite signs)  

    According to the following method:
        1.  Set a = b = x0.
        2.  Set a = a − ∆x.
            If sgn(f(a)) sgn(f(b)) < 0,
                Terminate.
        3.  Set b = b + ∆x.
            If sgn(f(a)) sgn(f(b)) < 0,
                Terminate.
        4.  Set ∆x = 2*∆x and return to step 2.
