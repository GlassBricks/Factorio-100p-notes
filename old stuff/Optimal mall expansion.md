
Suppose you have $T$ units of time to produce as much of some resource as possible.
We have a mall, and at any point, the resources produced by the mall can _all_ go to expanding the mall, or _all_ go towards creating the target resource. Our strategy will be: expand the mall until time $x$, then spend the remaining $T-x$ time producing the target resource.
The goal is to find the optimal value of $x$ (how long we should switch from expansion to production).

We will assume that the mall expands exponentially. Skipping the differential equation stuff, the mall size (in amount of resources) can be modeling as is `$f(t)=Pe^(rt)$`, producing `$f'(t)=Pre^(rt)$` resources per unit time.
After $x$ units of time, we stop expansion and put all the mall into the target resources for the remaining $T-x$ time, yielding `$g(x)=f'(x)(T-x)=Pre^(rt)(T-x)$` resources.

Now, maximizing $g(x)$:
```am
g(x)&=Pre^(rx)T-xe^(rx)

g'(x)&=Pr(Tre^(rx)-xre^(rx)-e^(rx))

	 &=Pre^(rx)(Tr-xr-1)


g'(x)=0 => Tr-xr-1=0

x=(Tr-1)/r = T-1/r
```
This means it's optimal to stop expanding at `$1/r$` before time T.
Here's how we can interpret this:
If we stop expansion at any given time, it will take $1/r$ more units of time to produce the current factory value in quantity.

So, in conclusion, the optimal time to stop expansion is at the point when the factory can produce its own value in buildings in the remaining time.

Intuition: if you graph it, the this strategy makes a "square" on an exponential curve, which has maximum area