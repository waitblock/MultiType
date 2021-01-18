import time, calendar, random

word_file = open("words.txt", "r")
words = word_file.read().split("\n")
word_file.close()

print("MultiType, the Multipurpose Typing Program")
print("Press Control-C to quit.")
print("\n")

while True:
    try:

        words_amount = input("Enter the amount of words: ")

        on_start = input("Press the return key to start: ")

        delays = []

        start_delay = 3



        for i in range(start_delay):
            print("The test will start in", str(start_delay)+"...")
            time.sleep(1)
            start_delay -= 1

        print("Test started.")

        correct_words = 0
        total_words = 0

        start_epoch = calendar.timegm(time.gmtime())

        for i in range(words_amount):
            index = random.randint(0, len(words))
            typed = input("Type "+words[index]+": ")
            if typed == words[index]:
                correct_words += 1
            total_words += 1

        sum_delays = 0
        for i in range(len(delays)):
            sum_delays += delays[i]

        raw_time = calendar.timegm(time.gmtime())-start_epoch
        time = calendar.timegm(time.gmtime())-start_epoch - sum_delays

        print("Raw time: "+str(raw_time)+" sec")
        print("Adjusted time: "+str(time)+" sec")
        print("Score: "+str(correct_words)+"/30")
    except KeyboardInterrupt:
        exit()