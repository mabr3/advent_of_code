#![allow(unused)]
use std::collections::HashMap;
use std::env;
use std::time::Instant;

fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    utils::tester("p1", p1, &input, 10);
    utils::tester("p2", p2, &input, 10);
}

fn p1(input: &str) -> i32 {
    // rules to be nice:
    // contains >= 3 vowels
    // contains at least 1 letter that appears twice in a row
    // does not contain ab, cd, pq, or xy
    // even if they are part of the other reqs
    let mut sum = 0;
    // TODO: Make it better/prettier
    for line in input.lines() {
        let mut prev: char = ' ';
        let mut vowel_counter: HashMap<char, u32> = HashMap::new();
        let mut conditions = (false, false, true);
        for ch in line.chars() {
            match (prev.to_string() + &ch.to_string()).as_str() {
                "ab" | "cd" | "pq" | "xy" => {
                    conditions.2 = false;
                    break;
                }
                _ => (),
            };

            if ch == prev {
                conditions.1 = true;
            }

            match ch {
                'a' | 'e' | 'i' | 'o' | 'u' => {
                    let vc = vowel_counter
                        .entry(ch)
                        .and_modify(|vc| *vc += 1)
                        .or_insert(1);
                }
                _ => (),
            };
            if vowel_counter.values().sum::<u32>() >= 3 {
                conditions.0 = true;
            }
            prev = ch;
        }
        sum += if conditions.0 & conditions.1 & conditions.2 {
            1
        } else {
            0
        };
    }
    sum
}

fn p2(input: &str) -> i32 {
    //a nicestring follows both:
    //contains a pair that appears at least twice but it doesn't overlap
    //contains one letter that repeats itself with one in the middle at least once
    let mut sum = 0;
    for line in input.lines() {
        let mut cond_1: bool = false;
        let mut cond_2: bool = false;
        let mut prev: char = ' ';
        let mut ant_prev: char = ' ';
        let mut pair_counter: HashMap<String, Vec<(usize, usize)>> = HashMap::new();
        for (i, ch) in line.chars().enumerate() {
            if i > 0 && !cond_1 {
                let pair = (prev.to_string() + &ch.to_string());
                let pc = pair_counter
                    .entry(pair)
                    .and_modify(|vc| vc.push((i - 1, i)))
                    .or_insert(vec![(i - 1, i)]);
                cond_1 = pc.iter().any(|v| v.1 < i - 1);
            }

            if !cond_2 && prev != ant_prev && ch == ant_prev {
                cond_2 = true;
            }

            if cond_1 && cond_2 {
                sum += 1;
                break;
            }
            ant_prev = prev;
            prev = ch;
        }
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = "ugknbfddgicrmopn";
        let answer = 1;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "aaa";
        let answer = 1;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_3() {
        let input = "jchzalrnumimnmhp";
        let answer = 0;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_4() {
        let input = "haegwjzuvuyypxyu";
        let answer = 0;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_5() {
        let input = "dvszwmarrgswjxmb";
        let answer = 0;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p2_1() {
        let input = "qjhvhtzxzqqjkmpb";
        let answer = 1;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_2() {
        let input = "xxyxx";
        let answer = 1;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_3() {
        let input = "uurcxstgmygtbstg";
        let answer = 0;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_4() {
        let input = "ieodomkazucvgmuy";
        let answer = 0;
        assert_eq!(p2(input), answer);
    }
}
