use std::io;

fn main(){
    println!("猜数字游戏！");
    println!("请输入一个数字：");

    // 定义一个可变变量，用于存储用户输入的数字
    // 使用标准库提供的 String 创建一个新的空字符串
    let mut guess = String::new();

    io::stdin() // 从io模块调用stdin函数，这将允许我们处理用户输入
        .read_line(&mut guess) // 调用标准输入句柄上的read_line方法以获取用户的输入,将 &mut guess作为参数传递给read_line告诉它将用户输入存储在哪个字符串中
        .expect("Failed to read line"); // 处理潜在的错误

    print!("你输入的是：{}", guess);
}