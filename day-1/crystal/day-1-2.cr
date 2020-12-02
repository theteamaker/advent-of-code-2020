numbers = Array(Int32).new
desired_sum = 2020
complete = false

STDIN.each_line do |line|
    numbers.push(line.to_i)
end

numbers.each do |num1|
    numbers.each do |num2|
        num3 = desired_sum - (num1 + num2)
        if numbers.index(num1) == numbers.index(num2)
            next
        elsif numbers.includes?(num3)
            puts "The three numbers which add to get " + desired_sum.to_s + " are " + num1.to_s + ", " + num2.to_s + ", and " + num3.to_s + "."
            puts "The product of these three numbers is " + (num1 * num2 * num3).to_s + "."
            complete = true
            break
        end
        break if complete == true
    end
end