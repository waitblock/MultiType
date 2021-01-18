import time, calendar, random

word_file = open("words.txt", "r")
words = word_file.read().split("\n")
word_file.close()

print("MultiType, the Multipurpose Typing Program")
print("Press Control-C to quit.")

while True:
    try:
        print("\n")
        print("1. Word Test")
        print("2. Word Practice")
        option = input("Select an option: ")

        if option == "1":
            words_amount = int(input("Enter the amount of words: "))

            on_start = input("Press the return key to start: ")

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

            total_time = calendar.timegm(time.gmtime())-start_epoch
            
            print("Time: "+str(total_time)+" sec")
            print("Score: "+str(correct_words)+"/"+str(words_amount))

        if option == "2":
            print("Press Control-C to stop the practice.")
            start_epoch = calendar.timegm(time.gmtime())
            correct_words = 0
            total_words = 0
            while True:
                try:
                    index = random.randint(0,len(words))
                    typed = input("Type "+words[index]+": ")
                    if typed == words[index]:
                        correct_words += 1
                    total_words += 1
                except KeyboardInterrupt:
                    break
            total_time = calendar.timegm(time.gmtime())-start_epoch

            print("Time Spent Practicing: "+str(total_time)+" sec")
            print("Words Typed Correctly: "+str(correct_words)+" words")
            print("Total Words Typed: "+str(total_words)+" words")
        
    except KeyboardInterrupt:
        print("Exiting...")
        break
