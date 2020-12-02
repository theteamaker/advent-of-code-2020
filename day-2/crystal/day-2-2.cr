valid = 0

STDIN.each_line do |line|
    items = line.split(" ")

    pos1, pos2 = items[0].split("-").map { |x| x.to_i }
    letter = items[1].strip(":")
    password = items[2]

    if [password[pos1 - 1], password[pos2 - 1]].join("").count(letter) == 1
        valid += 1
    end
end

puts valid