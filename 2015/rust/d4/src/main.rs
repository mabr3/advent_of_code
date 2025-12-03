use hex_literal::hex;
use md5::{Digest, *};
use std::env;
use utils;

fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    utils::tester("p1", p1, &input, 10);
    utils::tester("p2", p2, &input, 10);
}

fn p1(input: &str) -> &str {
    " "
}

fn p2(input: &str) -> &str {
    " "
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = "abcdef";
        let answer = "609043";
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "pqrstuv";
        let answer = "1048970";
        assert_eq!(p1(input), answer);
    }
}
