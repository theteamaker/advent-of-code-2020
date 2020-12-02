numbers = Array(Int32).new
desired_sum = 2020

STDIN.each_line do |line|
    numbers.push(line.to_i)
end

numbers.each do |num1|
    num2 = desired_sum - num1
    if numbers.includes?(desired_sum - num1)
        puts "The two numbers which add to get %d are %d and %d." % [desired_sum, num1, num2]
        puts "The product of these two numbers is %d." % [num1 * num2]
        break
    end
end