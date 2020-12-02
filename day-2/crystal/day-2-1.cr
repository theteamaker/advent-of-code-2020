valid = 0

STDIN.each_line do |line|
    items = line.split(" ")

    min, max = items[0].split("-").map { |x| x.to_i }
    letter = items[1].strip(":")
    password = items[2]

    letter_count = password.count(letter)
    if min <= letter_count <= max
        valid += 1
    end
end

puts valid