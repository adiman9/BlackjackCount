blackjackdata = fopen('blackjack data.txt', 'r');

start = [];
startcount = 1;

handcount = [];
win = [];
hand = 1;

line = fgetl(blackjackdata);

while ischar(line)
    if strcmp(line, 'start count')
        line = fgetl(blackjackdata);
        start(startcount) = str2num(line);
        startcount = startcount + 1;
    elseif strcmp(line, 'count')
        line = fgetl(blackjackdata);
        handcount(hand) = str2num(line);
        line = fgetl(blackjackdata);
        win(hand) = str2num(line);
        hand = hand + 1;
    end
    line = fgetl(blackjackdata);
end
fclose(blackjackdata);

total = 0;
totwins = 0;
accumwin = 0;

for x = 1:length(win)
    if handcount(x) > 1
        total = total + 1;
        accumwin = accumwin + win(x);
        if win(x) > 0
           totwins = totwins + 1;
        end
    end
end

percenwin = totwins / total;
