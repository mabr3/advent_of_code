use std::env;
use std::fs;
use std::time::Instant;

fn build_path(path: &str) -> String {
    // TODO: there should be a way to get input location from the args
    // HACK: Also, this looks like a hacky way to do this!
    let path_split: Vec<&str> = path.split('/').collect();
    // println!("Running! {:?}", path_split);
    let cwd: String = env::current_dir().unwrap().display().to_string();
    let cwd_split: Vec<&str> = cwd.split('/').collect();
    // println!("cwd: {:?}", cwd_split);
    let day = &path_split[path_split.len() - 1][1..];
    // println!("AKA this is day {}", day);
    let inputpath = cwd_split[..cwd_split.len() - 2].join("/") + "/inputs/" + day + ".txt";
    // println!("AKA the input file is in: {}", inputpath);
    inputpath
}

pub fn read_file(code_path: String, _build_path_flag: bool) -> String {
    let input_path = build_path(&code_path);
    let contents = fs::read_to_string(&input_path).unwrap();
    // println!("I've read {} and I've got {}", input_path, contents);
    contents
}

pub fn splitter<T: std::str::FromStr>(contents: &str, separator: char) -> Vec<Vec<T>> {
    let mut splits: Vec<Vec<T>> = Vec::new();
    for line in contents.lines() {
        let split: Vec<T> = line
            .split(separator)
            .filter_map(|x| x.parse::<T>().ok())
            .collect();
        splits.push(split);
    }
    splits
}

pub fn tester(name: &str, f: fn(&str) -> i32, arg: &str, tries: usize) {
    let mut results: [(i32, f32); 10] = [(0, 0.0); 10];

    for i in 0..tries {
        let start = Instant::now();
        let r = f(arg);
        let time = Instant::now() - start;
        results[i] = (r, time.as_secs_f32());
    }

    let equal_results: bool = results.iter().all(|(c, _)| *c == results[0].0);
    if !equal_results {
        println!("Results aren't equal: {:?}", results.iter().map(|(c, _)| c))
    }
    let min_t = results
        .iter()
        .map(|(_, t)| *t)
        .into_iter()
        .reduce(f32::min)
        .unwrap_or(0.);
    let max_t: f32 = results
        .iter()
        .map(|(_, t)| *t)
        .reduce(f32::max)
        .unwrap_or(0.);
    let avg_t: f32 = results.iter().map(|(_, t)| t).sum::<f32>() / tries as f32;
    println!(
        "{:^15} {:^15} {:^15} {:^15} {:^15}",
        "Part", "Result", "Min", "Max", "Avg"
    );
    println!(
        "{:^15} {:^15} {:^15} {:^15} {:^15}",
        name, results[0].0, min_t, max_t, avg_t
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_path() {
        let fullpath = "taget/debug/d1";
        assert_eq!(
            "/Users/mike/Desktop/advent_of_code/2015/inputs/1.txt",
            build_path(fullpath)
        );
    }

    #[test]
    fn test_spliiter_1() {
        let input = "1x2x3";
        let expected = vec![vec![1, 2, 3]];
        let separator = 'x';
        assert_eq!(splitter::<i32>(input, separator), expected);
    }

    #[test]
    fn test_spliiter_2() {
        let input = "1x2x3 \
            4x5x6";
        let expected = vec![vec![1, 2, 3], vec![4, 5, 6]];
        let separator = 'x';
        assert_eq!(splitter::<i32>(input, separator), expected);
    }
}
