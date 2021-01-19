import time, calendar, random
from tkinter import Tk

word_file = open("words.txt", "r")
words = word_file.read().split("\n")
word_file.close()

char_file = open("chars.txt", "r")
chars = char_file.read().split("\n")
char_file.close()

para_file = open("paragraphs.txt", "r")
paragraphs = para_file.read().split("\n")
para_file.close()

print("MultiType, the Multipurpose Typing Program")
print("Press Control-C or 9 to quit.")

while True:
    try:
        print("\n")
        print("1. Keyboard Test")
        print("2. Word Test")
        print("3. Word Practice")
        print("4. Numberpad Test")
        print("5. Numberpad Practice")
        print("6. Random Strings Test")
        print("7. Random Strings Practice")
        print("8. Paragraph Practice")
        print("9. Exit")
        
        option = input("Select an option: ")

        if option == "1":
            print("The quick brown fox jumps over the lazy dog.")
            typed = input("Type the above phrase: ")
            
            master = Tk()
            clipboard = master.clipboard_get()
            master.withdraw()

            if clipboard == "The quick brown fox jumps over the lazy dog.":
                print("Control-C Detected!")
            elif typed == "The quick brown fox jumps over the lazy dog.":
                print("Keyboard test passed.")
            else:
                print("Keyboard test failed.")
        
        if option == "2":
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

        if option == "3":
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

        if option == "4":
            words_amount = int(input("Enter the amount of strings: "))

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
                rand_str = ""
                for i in range(4):
                    if i == 3:
                        rand_str += str(random.randint(100,999))
                    else:
                        rand_str += str(random.randint(100,999))+"-"
                typed = input("Type "+rand_str+": ")
                if typed == rand_str:
                    correct_words += 1
                total_words += 1

            total_time = calendar.timegm(time.gmtime())-start_epoch
            
            print("Time: "+str(total_time)+" sec")
            print("Score: "+str(correct_words)+"/"+str(words_amount))
            
        if option == "5":
            start_epoch = calendar.timegm(time.gmtime())
            correct_words = 0
            total_words = 0

            print("Press Control-C to stop the practice.")
            while True:
                try:
                    rand_str = ""
                    for i in range(4):
                        if i == 3:
                            rand_str += str(random.randint(100,999))
                        else:
                            rand_str += str(random.randint(100,999))+"-"
                    typed = input("Type "+rand_str+": ")
                    if typed == rand_str:
                        correct_words += 1
                    total_words += 1
                except KeyboardInterrupt:
                    break
            
            total_time = calendar.timegm(time.gmtime())-start_epoch

            print("Time: "+str(total_time)+" sec")
            print("Words Typed Correctly: "+str(correct_words)+" words")
            print("Total Words Typed: "+str(total_words)+" words")

        if option == "6":
            words_amount = int(input("Enter the amount of strings: "))

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
                rand_str = ""
                for i in range(random.randint(6,12)):
                    rand_str += chars[random.randint(0,len(chars)-1)]
                typed = input("Type "+rand_str+": ")
                if typed == rand_str:
                    correct_words += 1
                total_words += 1

            total_time = calendar.timegm(time.gmtime())-start_epoch
            
            print("Time: "+str(total_time)+" sec")
            print("Score: "+str(correct_words)+"/"+str(words_amount))

        if option == "7":
            print("Press Control-C to stop the practice.")
            correct_words = 0
            total_words = 0

            start_epoch = calendar.timegm(time.gmtime())

            while True:
                try:
                    rand_str = ""
                    for i in range(random.randint(6,12)):
                        rand_str += chars[random.randint(0,len(chars)-1)]
                    typed = input("Type "+rand_str+": ")
                    if typed == rand_str:
                        correct_words += 1
                    total_words += 1
                except KeyboardInterrupt:
                    break

            total_time = calendar.timegm(time.gmtime())-start_epoch
            
            print("Time: "+str(total_time)+" sec")
            print("Words Typed Correctly: "+str(correct_words)+" words")
            print("Total Words Typed: "+str(total_words)+" words")

        if option == "8":
            on_start = input("Press the return key to start: ")

            start_delay = 3

            for i in range(start_delay):
                print("Start typing in", str(start_delay)+"...")
                time.sleep(1)
                start_delay -= 1

            print("Test started.")
            
            correct_words = 0
            total_words = 0
            para = paragraphs[random.randint(0, len(paragraphs)-1)]
            print(para)
            start_epoch = calendar.timegm(time.gmtime())
            typed = input("Type what you see: ")
            total_time = calendar.timegm(time.gmtime()) - start_epoch
            para_words = para.split(" ")
            typed_words = typed.split(" ")
            for i in range(len(para_words)-len(typed_words)-1):
                typed_words.append("á")

            for i in range(len(typed_words)-1):
                if typed_words[i] == para_words[i]:
                    correct_words += 1
                total_words += 1

            master = Tk()
            clipboard = master.clipboard_get()
            master.withdraw()
            adj_time = total_time/60
            wpm = round(len(para_words)/adj_time, 2)
            

            if clipboard == para:
                print("Control-C Detected!")
            else:
                print(str(wpm)+"WPM")
                print("Score: "+str(correct_words)+"/"+str(total_words))
                print("Time: "+str(total_time)+" seconds")

            
        if option == "9":
            break
        
    except KeyboardInterrupt:
        break
