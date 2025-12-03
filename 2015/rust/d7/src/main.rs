#![allow(unused)]
use regex::Regex;
use std::collections::HashMap;
use std::env;
use std::time::Instant;
use utils;
use std::collections::HashMap;

fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    utils::tester("p1", p1, &input, 10);
    utils::tester("p2", p2, &input, 10);
}
// We need some sort of structure that allows us to go from wire a
// and trace its operations back to the start
// and do them all.

//OR we do some topological sorting, calculate everything and then get value a
//but in that case it is possible we're calculting more stuff than needed

struct Instruction {
    source: (&str, &str),
    target: char,
    op: Gate
}

impl From<&str> for HashMap {
    fn from(s: &str) -> Instruction {
        let mut instruction = Instruction::new();
        let (source, target) = s.split_once(" -> ").unwrap();
        instruction::target = target;



        instruction
    }
}

enum Gate {
    AND(char, char),
    OR(char, char),
    LSHIFT(char, u16),
    RSHIFT(char, u16),
    NOT(char),
    IN(u16),
}

impl Gate {
    fn do_op(&self) -> u16 {


}

fn p1(input: &str) -> i32 {
    let wires: HashMap<(char, Gate)> = HashMap::new();
    let instructions: Vec<Instruction> = Vec::new();
    for instrunction in instructions {
            wires.insert(
        }
}

fn p2(input: &str) -> i32 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = "123 -> a
456 -> y
a AND y -> d
a OR y -> e
a LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT a -> h
NOT y -> i";
        let answer = 123;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "123 -> x
456 -> a
x AND a -> d
x OR a -> e
x LSHIFT 2 -> f
a RSHIFT 2 -> g
NOT x -> h
NOT a -> i";
        let answer = 456;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_3() {
        let input = "123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> a";
        let answer = 65079;
        assert_eq!(p1(input), answer);
    }
}
