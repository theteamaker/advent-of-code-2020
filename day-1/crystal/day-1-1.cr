numbers = Array(Int32).new
desired_sum = 2020

STDIN.each_line do |line|
    numbers.push(line.to_i)
end

numbers.each do |num1|
    num2 = desired_sum - num1
    if numbers.includes?(desired_sum - num1)
        puts "The two numbers which add to get " + desired_sum.to_s + " are " + num1.to_s + " and " + num2.to_s + "."
        puts "The product of these two numbers is " + (num1 * num2).to_s + "."
        break
    end
end