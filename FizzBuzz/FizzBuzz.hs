{-|
Module      : FizzBuzz
Description : Module with the solution to the FizzBuzz problem.
              The FizzBuzz problem involves returning a list where numbers that are multiples of 3 are replaced with "Fizz",
              numbers that are multiples of 5 are replaced with "Buzz", and if a number is a multiple of both, it's replaced with "FizzBuzz".
Maintainer  : Shikitimiau
Date: 07-08-2023
-}

module FizzBuzz where

-- | FizzBuzz. Function that solves the FizzBuzz problem by generating a list of size n.
fizzbuzz :: Int -> [String]
fizzbuzz 0 = []
fizzbuzz n
    | n < 0 = []
    | n `mod` 3 == 0 && n `mod` 5 == 0 = (fizzbuzz (n-1)) ++ ["FizzBuzz"]
    | n `mod` 3 == 0 = (fizzbuzz (n-1))  ++ ["Fizz"]
    | n `mod` 5 == 0 = (fizzbuzz (n-1)) ++ ["Buzz"]
    | otherwise = (fizzbuzz (n-1)) ++ [show n]
