use std::fs;

fn main() {
    // #1
    let input = fs::read_to_string("src/input_01.txt")
    .expect("Something went wrong reading the file");
    let input_split = input.split("\n");
    
    let mut depths: Vec<&str> = input_split.collect();
    depths.remove(depths.len() - 1);
    
    let mut depth_nums: Vec<i32> = Vec::new();
    for depth in depths{
        depth_nums.push(depth.parse::<i32>().unwrap());
    }

    let mut deeper_counter = 0;
    for i in 0..depth_nums.len() {
        if i > 0 && depth_nums[i] > depth_nums[i - 1] {
            deeper_counter = deeper_counter + 1;
        }
    }
    println!("1: {}", deeper_counter);

    // #2
    let mut deeper_counter_2 = 0;
    for i in 0.. depth_nums.len() {
        if  i >= 3 && depth_nums[i] > depth_nums[i - 3] {
            deeper_counter_2 = deeper_counter_2 + 1;
        }
    }
    println!("2: {}", deeper_counter_2);
}

