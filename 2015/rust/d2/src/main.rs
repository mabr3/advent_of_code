use std::env;
use std::time::Instant;
use utils;

fn main() {
    let fullpath: String = env::args().next().unwrap();
    let input = utils::read_file(fullpath, true);
    let start1 = Instant::now();
    let r1 = p1(&input);
    let t1 = Instant::now() - start1;
    println!(
        "P1 result is {} - took {} milliseconds",
        r1,
        t1.as_secs_f64() * 1000 as f64
    );
    let start2 = Instant::now();
    let r2 = p2(&input);
    let t2 = Instant::now() - start2;
    println!(
        "P2 result is {} - took {} milliseconds",
        r2,
        t2.as_secs_f64() * 1000 as f64
    );
}

fn p1(input: &str) -> i32 {
    let entries = utils::splitter::<i32>(input, 'x');
    let mut sum = 0;

    for entry in entries {
        let sides = vec![
            entry[0] * entry[1],
            entry[1] * entry[2],
            entry[2] * entry[0],
        ];
        sum += 2 * sides[0] + 2 * sides[1] + 2 * sides[2] + sides.iter().min().unwrap();
    }
    sum
}

fn p2(input: &str) -> i32 {
    let entries = utils::splitter::<i32>(input, 'x');
    let mut sum: i32 = 0;
    for mut entry in entries {
        entry.sort();
        sum += 2 * entry[..2].iter().fold(0, |acc, x| acc + x)
            + entry.iter().fold(1, |acc, x| acc * x);
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = "2x3x4";
        let answer = 58;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "1x1x10";
        let answer = 43;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p2_1() {
        let input = "2x3x4";
        let answer = 34;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_2() {
        let input = "1x1x10";
        let answer = 14;
        assert_eq!(p2(input), answer);
    }
}
