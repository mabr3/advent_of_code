use std::fs;
pub fn build_path(path: &str) -> String {
    // TODO: there should be a way to get input location from the args
    // HACK: Also, this looks like a hacky way to do this!
    let fullpath_split: Vec<&str> = path.split('/').collect();
    let day = &fullpath_split[fullpath_split.len() - 1][1..];
    let inputpath =
        fullpath_split[..fullpath_split.len() - 5].join("/") + "/inputs/" + day + ".txt";
    // println!("Running! {:?}", fullpath_split);
    // println!("AKA this is day {}", day);
    // println!("AKA the input file is in: {}", inputpath);
    inputpath
}

pub fn read_file(code_path: String, _build_path_flag: bool) -> String {
    let input_path = build_path(&code_path);
    let contents = fs::read_to_string(&input_path).unwrap();
    // println!("I've read {} and I've got {}", input_path, contents);
    contents
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_path() {
        let fullpath = "/Users/mike/Desktop/advent_of_code/2015/rust/d1/debug/target/d1";
        assert_eq!(
            "/Users/mike/Desktop/advent_of_code/2015/inputs/1.txt",
            build_path(fullpath)
        );
    }
}
