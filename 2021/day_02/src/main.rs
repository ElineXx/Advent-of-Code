use std::*;

fn main() {
    let input = fs::read_to_string("src/input_02.txt")
    .expect("Something went wrong reading the file");
    let input_split = input.split("\n");

    // #1
    let mut position = (0, 0);

    for line in input_split.clone() {
        let line_split: Vec<&str> = line.split(" ").collect();
        if line_split[0] == "forward" {
            position.0 += line_split[1].parse::<i32>().unwrap();
        }
        if line_split[0] == "down" {
            position.1 += line_split[1].parse::<i32>().unwrap();
        }
        if line_split[0] == "up" {
            position.1 -= line_split[1].parse::<i32>().unwrap();
        }
    }

    println!("1: {}", position.0 * position.1);

    // #2
    let mut position = (0, 0);
    let mut aim = 0;

    for line in input_split.clone() {
        if line == "" {
            break
        }
        let line_split: Vec<&str> = line.split(" ").collect();
        let x = line_split[1].parse::<i32>().unwrap();

        if line_split[0] == "forward" {
            position.0 += x;
            position.1 += aim * x;
        }
        if line_split[0] == "down" {
            aim += x;
        }
        if line_split[0] == "up" {
            aim -= x;
        }
    }

    println!("2: {}", position.0 * position.1);
}
