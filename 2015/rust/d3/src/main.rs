use std::collections::HashMap;
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
    let mut sum: i32 = 0;
    let mut coords: (i32, i32) = (0, 0);
    let mut visits: HashMap<(i32, i32), bool> = HashMap::new();
    visits.entry(coords).or_insert_with(|| {
        sum += 1;
        true
    });
    for ch in input.chars() {
        match ch {
            'v' => coords.1 -= 1,
            '<' => coords.0 -= 1,
            '^' => coords.1 += 1,
            '>' => coords.0 += 1,
            _ => (),
        }
        visits.entry(coords).or_insert_with(|| {
            sum += 1;
            true
        });
    }
    sum
}

fn p2(input: &str) -> i32 {
    let mut sum: i32 = 0;
    let mut santa_coords: (i32, i32) = (0, 0);
    let mut robo_coords: (i32, i32) = (0, 0);
    let mut visits: HashMap<(i32, i32), bool> = HashMap::new();
    visits.entry(santa_coords).or_insert_with(|| {
        sum += 1;
        true
    });
    for (i, ch) in input.chars().enumerate() {
        let coords = if i % 2 == 0 {
            &mut santa_coords
        } else {
            &mut robo_coords
        };
        match ch {
            'v' => coords.1 -= 1,
            '<' => coords.0 -= 1,
            '^' => coords.1 += 1,
            '>' => coords.0 += 1,
            _ => (),
        }
        visits.entry(*coords).or_insert_with(|| {
            sum += 1;
            true
        });
    }
    sum
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_p1_1() {
        let input = ">";
        let answer = 2;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_2() {
        let input = "^>v<";
        let answer = 4;
        assert_eq!(p1(input), answer);
    }

    #[test]
    fn test_p1_3() {
        let input = "^v^v^v^v^v";
        let answer = 2;
        assert_eq!(p1(input), answer);
    }
    #[test]
    fn test_p2_1() {
        let input = "^v";
        let answer = 3;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_2() {
        let input = "^>v<";
        let answer = 3;
        assert_eq!(p2(input), answer);
    }

    #[test]
    fn test_p2_3() {
        let input = "^v^v^v^v^v";
        let answer = 11;
        assert_eq!(p2(input), answer);
    }
}
