use crate::collections::HashSet;
use std::*;

fn main() {
    let input =
        fs::read_to_string("src/input_03.txt").expect("Something went wrong reading the file");
    let mut input_split: Vec<&str> = input.split("\n").collect();
    input_split.pop();

    // #1
    let line_length = input_split[0].len();
    let mut score = vec![0; line_length];

    for line in &input_split {
        for (i, char) in line.chars().enumerate() {
            if char == '1' {
                score[i] += 1;
            }
            if char == '0' {
                score[i] -= 1;
            }
        }
    }

    let mut gamma_vec = vec!['0'; line_length];
    let mut epsilon_vec = vec!['0'; line_length];

    for (i, num) in score.iter().enumerate() {
        if num > &0 {
            gamma_vec[i] = '1';
        } else {
            epsilon_vec[i] = '1';
        }
    }

    let mut gamma_str = String::from("");
    for char in gamma_vec.clone() {
        gamma_str.push(char);
    }

    let mut epsilon_str = String::from("");
    for char in epsilon_vec.clone() {
        epsilon_str.push(char);
    }

    let gamma_rate = isize::from_str_radix(&gamma_str, 2).unwrap();
    let epsilon_rate = isize::from_str_radix(&epsilon_str, 2).unwrap();

    println!("1: {}", gamma_rate * epsilon_rate);

    // #2
    let oxygen_rates: HashSet<&str> = input_split.clone().into_iter().collect();
    let co2_rates: HashSet<&str> = input_split.clone().into_iter().collect();

    fn get_rate_from_set(rates: HashSet<&str>, most_freq: bool) -> &str {
        let mut rate_set = rates.clone();
        let mut i_count = 0;
        while rate_set.len() > 1 {
            let mut str_a: HashSet<&str> = HashSet::new();
            let mut str_b: HashSet<&str> = HashSet::new();
    
            for o_num in rate_set.clone().into_iter() {
                if o_num.chars().nth(i_count).unwrap() == '0' {
                    str_a.insert(o_num);
                }
                if o_num.chars().nth(i_count).unwrap() == '1' {
                    str_b.insert(o_num);
                }
            }
    
            if str_a.len() > str_b.len() && most_freq {
                rate_set = str_a;
            } 
            else if str_a.len() <= str_b.len() && !most_freq {
                rate_set = str_a;
            } 
            else {
                rate_set = str_b;
            }
            
            i_count += 1;
        }

        return rate_set.iter().next().unwrap();
    }
   
    let oxygen_bin = get_rate_from_set(oxygen_rates, true);
    let co2_bin = get_rate_from_set(co2_rates, false);
    let oxygen_rate = isize::from_str_radix(&oxygen_bin, 2).unwrap();
    let co2_rate = isize::from_str_radix(&co2_bin, 2).unwrap();

    println!("2: {}", oxygen_rate * co2_rate);
}
