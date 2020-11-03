# Hungarian-Cardinal-Numerals
My answer to a small python training exercise made on CodeWars

The exercise can be found here : https://www.codewars.com/kata/58008f9897917feeec000a3e

____________________

A quick resume of the exercise : Write a function called hungarian_numeral() which takes a non-negative integer n and returns the corresponding Hungarian numeral to it. 0 <= n < 1000000

____________________

A quick resume of the defining design choices of my algorithm :

-Since n< 1000000 I split the logic into two groups of three numbers because we repeat the same wording logic for what's above the thousands and what's under it.

-I also reversed the reading direction of n because it seems to me that it's easier and more efficent to work on it that way with python.

-For both groups of three numbers I start by adjusting the "first" "second" and "third" variables' values which are initially set at the most common cases to the exact case of "n" and then I add those to the result.

____________________

Added comments about my algorithm :

-I would've liked to completely rid the function of magic constants (mostly for all the edge cases) but I couldn't think of a way to do it that wouldn't make the algorithm very confusing to read, my best guess would've been to use an object to store the edge cases, but it would've brought the same issues magic constants would.

-At the time I made it I hadn't learned about list comprehension but I if I ever remake it I would defninitely use it at many points in my algorithm, but at the moment I am very focused on JavaScript
