import os
import sys


def main():
    global ham_count
    global spam_count
    global spam_file
    global ham_file
    inp_path = ""
    if len(sys.argv)>2:
        for i in range(len(sys.argv)-2):
            inp_path += sys.argv[i+1]+" "
        inp_path += sys.argv[-1]
    else:
        inp_path = sys.argv[1]
        print(inp_path)
    for root, dirs, files in os.walk(inp_path):

        path = os.path.split(root)
        #print(path[-1])
        if path[-1] == 'spam':
            for file in files:
                if file.endswith(".txt"):
                    spam_file += 1
                    f = open(os.path.join(root,file), 'r',encoding='latin1')
                    data = f.read().strip().split()
                        #print(data)
                    for token in data:
                        if token in spam_dict:
                            val = spam_dict[token]
                            val = val + 1
                            spam_count = spam_count + 1
                            spam_dict[token] = val
                        else:
                            ham_dict[token] = 1
                            spam_dict[token] = 2
                            spam_count = spam_count + 2
                            ham_count = ham_count + 1

                    f.close()

        if path[-1] == 'ham':
            for file in files:
                if file.endswith(".txt"):
                    ham_file += 1
                    f = open(os.path.join(root, file), 'r',encoding='latin1')
                    data = f.read().strip().split()
                    #print(data)
                    for token in data:
                        if token in ham_dict:
                            val = ham_dict[token]
                            val = val + 1
                            ham_count = ham_count + 1
                            ham_dict[token] = val
                        else:
                            ham_dict[token] = 2
                            ham_count = ham_count + 2
                            spam_dict[token] = 1
                            spam_count = spam_count + 1
                    f.close()

    print(spam_count)
    print(ham_count)
    for key in spam_dict:
        val = spam_dict[key]
        val = float(val)/float(spam_count)
        spam_dict[key] = float(val)

    for key in ham_dict:
        val = ham_dict[key]
        val = float(val)/float(ham_count)
        ham_dict[key] = float(val)

    spam_prob = float(spam_file)/float(spam_file+ham_file)
    ham_prob = float(ham_file) / float(spam_file + ham_file)

    filehandler = open("nbmodel.txt",'w',encoding='latin1')
    filehandler.write(str(spam_prob)+"\n")
    filehandler.write(str(ham_prob)+"\n")
    for key in spam_dict:
        filehandler.write(key+" "+str(spam_dict[key])+" "+str(ham_dict[key])+"\n")
    filehandler.close()


if __name__ == '__main__':
    spam_dict = {}
    spam_count = 0
    ham_dict = {}
    ham_count = 0
    spam_file = 0
    ham_file = 0
    unique_dict = {}
    #print(sys.argv)
    main()
