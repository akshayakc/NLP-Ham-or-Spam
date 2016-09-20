import os
import sys
import glob



def main():
    global ham_count
    global spam_count
    for root, dirs, files in os.walk(sys.argv[1]):
        path = root.split('\\')
        #print(path[-1])
        if path[-1] == 'spam':
            for file in files:
                if file.endswith(".txt"):
                    f = open(os.path.join(root,file), 'r')
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
                    f = open(os.path.join(root, file), 'r')
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
    print(spam_dict)
    print(ham_dict)
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

    print(spam_dict)
    print(ham_dict)
    

if __name__ == '__main__':
    spam_dict = {}
    spam_count = 0
    ham_dict = {}
    ham_count = 0
    unique_dict = {}
    main()
