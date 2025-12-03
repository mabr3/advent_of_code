#![allow(unused)]
use regex::Regex;
use std::collections::HashMap;
use std::env;
use std::time::Instant;

fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    utils::tester("p1", p1, &input, 10);
    utils::tester("p2", p2, &input, 10);
}

fn apply_regex(line: &'h str, pattern: &str) -> (&'h str, (&'h str, &'h str), (&'h str, &'h str)) {
    //TODO: make this a general function for utils
    let re = Regex::new(pattern).unwrap();
    //TODO: above and below unwraps!
    let contents = re.captures(line).unwrap();
    let (action, (x1, y1), (x2, y2)) = contents.extract();
    println!("Contents are: {contents:?}");
    (action, (x1, y1), (x2, y2))
}

fn p1(input: &str) -> i32 {
    let grid = vec![vec![0; 1000]; 1000];
    for line in input.lines() {
        let pattern = r"^(?P<action>.*)\s(?P<x1>\d{1,3}),(?P<y1>\d{1,3})\sthrough\s(?P<x2>\d{1,3}),(?P<y2>\d{1,3})$";
        let (action, (x1, y1), (x2, y2)) = apply_regex(line, pattern);
        // action, start, end = apply_reges(line, pattern);
        // match action {
        //     "toggle" => {
        //
        //     },
        //     "turn on" => {
        //
        //     },
        //     "turn off"
        // }
        continue;
    }

    0
}

fn p2(input: &str) -> i32 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = "turn on 0,0 through 999,999";
        println!("IN THETEST");
        let answer = 1000 * 1000;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "turn on 0,0 through 999,999 \
            turn off 499,499 through 500,500";
        let answer = 1000 * 1000 - 4;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_3() {
        let input = "turn on 0,0, through 999,999 \
            toggle 0,0 through 999,0";
        let answer = 1000 * 1000 - 1000;
        assert_eq!(p1(input), answer);
    }
}
