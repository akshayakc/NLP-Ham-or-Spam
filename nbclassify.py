import sys
import os
import math

def main():
    global spam_prob
    global ham_prob

    inp_path = ""
    filehandler = open('nbmodel.txt','r',encoding='latin1')
    data = filehandler.readlines()
    filehandler.close()
    #print(data)
    spam_prob = float(data[0].strip())
    #print(spam_prob)

    ham_prob = float(data[1].strip())
    #print(ham_prob)

    for i in range(len(data)-2):
        dict_list = data[i+2].strip().split(" ")
     #   print(dict_list)
        spam_dict[dict_list[0]] = float(dict_list[1])
        ham_dict[dict_list[0]] = float(dict_list[2])

    #print(spam_dict)
    #print(ham_dict)
    opfilehandler = open('nboutput.txt','w',encoding='latin1')

    if len(sys.argv) > 2:
        for i in range(len(sys.argv) - 2):
            inp_path += sys.argv[i + 1] + " "
        inp_path += sys.argv[-1]
    else:
        inp_path = sys.argv[1]

    for root, dirs, files in os.walk(inp_path):
        path = os.path.split(root)
        #print(path)


        if path[-1] == 'spam' or path[-1] == 'ham':
            for file in files:
                if file.endswith(".txt"):
                    file_spam_prob = 0.0
                    file_ham_prob = 0.0
                    filereader = open(os.path.join(root,file),'r',encoding='latin1')
                    word_list = filereader.read().strip().split()
                    filereader.close()
                    #print(word_list)
                    file_spam_prob += math.log(spam_prob)
                    file_ham_prob += math.log(ham_prob)
                    for word in word_list:
                        if word in spam_dict and word in ham_dict:
                            file_spam_prob += math.log(spam_dict[word])
                            file_ham_prob += math.log(ham_dict[word])
                    # print(file_spam_prob)
                    # print(file_ham_prob)
                    if file_spam_prob >= file_ham_prob:
                        opfilehandler.write("spam "+os.path.join(root,file)+"\n")
                    else:
                        opfilehandler.write("ham " + os.path.join(root, file)+"\n")

    opfilehandler.close()


if __name__== '__main__':
    spam_dict = {}
    ham_dict = {}
    spam_prob = 0
    ham_prob = 0
    main()