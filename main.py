import time, calendar, random

word_file = open("words.txt", "r")
words = word_file.read().split("\n")
word_file.close()

times = []

start_delay = 3



for i in range(start_delay):
    print("The test will start in", (start_delay))
    time.sleep(1)
    start_delay -= 1

print("Test started.")

correct_words = 0
total_words = 0

start_epoch = calendar.timegm(time.gmtime())
for i in range(30):
    index = random.randint(0, len(words))
    start_epoch = calendar.timegm(time.gmtime())
    typed = input("Type "+words[index]+": ")
    times.append(calendar.timegm(time.gmtime())-start_epoch)
    if typed == words[index]:
        correct_words += 1
    total_words += 1

sum = 0
for i in range(len(times)):
    sum += times[i]

avg = sum/len(times)

print("Average time per word: "+str(avg)+"sec")
print("WPM: "+str(avg*60))
print("Total words typed correctly: "+str(correct_words))
print("Total words typed: "+str(total_words))