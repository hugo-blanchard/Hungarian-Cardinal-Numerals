# Hungarian-Cardinal-Numerals
My answer to a small python training exercise made on CodeWars

The exercise can be found here : https://www.codewars.com/kata/58008f9897917feeec000a3e

A quick resume of the exercise : Write a function called hungarian_numeral() which takes a non-negative integer n and returns the corresponding Hungarian numeral to it. 0 <= n < 1000000

A quick resume of the defining design choices of my algorithm : Since n< 1000000 I split the logic into two groups of three numbers because we repeat the same wording logic for what's above the thousands and what's under it.
I also reversed the reading direction of n because it seems to me that it's easier and more efficent to work on it that way with python.
For both groups of three numbers I start by adjusting the "first" "second" and "third" variables' values which are initially set at the most common cases to the exact case of "n" and then i add those to the result.
