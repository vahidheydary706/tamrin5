import os.path

def check_file(path):
    if os.path.isfile(path) == False:
        print ("File not exist")
        exit()

def init():

    f = open('translate.txt', 'r')
    big_text = f.read()
    parts = big_text.split('\n')
    f.close
    return parts

def create_dictionary(parts):
    words=[]
    i=0
    while i < len(parts):
        my_dict = {'english':parts[i], 'persian':parts[i+1]}
        words.append(my_dict)
        i += 2
    return words


def check_duplication(words, new_word, language):
    for i in range(len(words)):
        if words[i][language] == new_word:
            return True
            break
    else: 
        return False

def main():
    
    check_file("translate.txt")
    
    print("1- Add new word")
    print("2- tranlate english2persian")
    print("3- translate persian2english")
    print("4- Exit")

    while (True):
        user_choice_index = int(input("\nPlease enter option#:"))
        if user_choice_index == 4:
            print("Good bye...")
            break
        elif user_choice_index == 1:
            en_word = input('english word:')
            if check_duplication(create_dictionary(init()), en_word,'english') == False:  
                fa_word = input('farsi word:')
                f = open('translate.txt', 'a')
                f.write('\n')
                f.write(en_word)
                f.write('\n')
                f.write(fa_word)
                print('word added successfully')
                f.close()
            else:
                print('word is duplicate!!!')
        elif user_choice_index == 2:
            print('please enter your english text:')
            user_string = input()
            sentences = user_string.split('.')
            for s in sentences:
                user_words = s.split(' ')
                words = create_dictionary(init())
                for j in range(len(user_words)):
                    for i in range(len(words)):
                        if words[i]['english'] == user_words[j]:
                            print(words[i]['persian'], end=' ')
                            break
                    else: 
                        print(user_words[j], end=' ')
                print('.', end='')
        elif user_choice_index == 3:
            print('please enter your finglish text:')
            user_string = input()
            sentences = user_string.split('.')
            for s in sentences:
                user_words = s.split(' ')
                words = create_dictionary(init())
                for j in range(len(user_words)):
                    for i in range(len(words)):
                        if words[i]['persian'] == user_words[j]:
                            print(words[i]['english'], end=' ')
                            break
                    else: 
                        print(user_words[j], end=' ')
                print('.', end='')


main()