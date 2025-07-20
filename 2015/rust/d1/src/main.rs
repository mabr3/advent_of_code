use std::env;
use std::time::Instant;
use utils;
fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    let start1 = Instant::now();
    let r1 = p1(&input);
    let t1 = Instant::now() - start1;
    println!("P1 result is {} - took {} seconds", r1, t1.as_secs_f64());
    let start2 = Instant::now();
    let r2 = p2(&input);
    let t2 = Instant::now() - start2;
    println!("P2 result is {} - took {} seconds", r2, t2.as_secs_f64());
}

fn p1(input: &str) -> i32 {
    // string into list
    // reduce with acc=0
    // case when ( then +1
    // case when ) then -1
    // return acc

    input
        .chars()
        .fold(0, |acc, c| if c == '(' { acc + 1 } else { acc - 1 })
}

fn p2(input: &str) -> i32 {
    // string into list
    // iterate over and keep track of floor
    // break if floor == -1
    // return iterator value
    let mut floor: i32 = 0;
    for (i, el) in input.chars().enumerate() {
        if el == '(' {
            floor = floor + 1;
        } else {
            floor = floor - 1;
        }
        if floor == -1 {
            return i as i32 + 1;
        }
    }
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_0() {
        let input = ["(())", "()()"];
        let answer = [0, 0];
        assert_eq!(vec![p1(input[0]), p1(input[1])], answer);
    }

    #[test]
    fn test_p1_3() {
        let input = vec!["(((", "(()(()(", "))((((("];
        let answer = vec![3, 3, 3];
        assert_eq!(vec![p1(input[0]), p1(input[1]), p1(input[2])], answer);
    }

    #[test]
    fn test_p1_m1() {
        let input = vec!["())", "))("];
        let answer = vec![-1, -1];
        assert_eq!(vec![p1(input[0]), p1(input[1])], answer);
    }

    #[test]
    fn test_p1_m3() {
        let input = vec![")))", ")())())"];
        let answer = vec![-3, -3];

        assert_eq!(vec![p1(input[0]), p1(input[1])], answer);
    }

    #[test]
    fn test_p2_1() {
        let input = ")";
        let answer = 1;

        assert_eq!(p2(input), answer);
    }
    #[test]
    fn test_p2_5() {
        let input = "()())";
        let answer = 5;

        assert_eq!(p2(input), answer);
    }
}
