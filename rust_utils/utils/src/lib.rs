use std::env;

use std::fs;
pub fn build_path(path: &str) -> String {
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
        let input = "1x2x3
4x5x6";
        let expected = vec![vec![1, 2, 3], vec![4, 5, 6]];
        let separator = 'x';
        assert_eq!(splitter::<i32>(input, separator), expected);
    }
}
