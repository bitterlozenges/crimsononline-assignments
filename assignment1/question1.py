"""
Question 1

objectives
    - get more comfortable with Python
    - learn how to handle exceptions
    - work with the file system
"""

def common_words(filename):
    """question 1a

    Write a function that takes a path to a text file as input. The function
    should open the file, count the number of occurrences of each word, and
    return a sorted list of the most common words
    """
    try:
        f = open(filename)
        str = f.read()
        f.close
    except IOError:
        print ("File missing!")
    else:
        arr = str.split()
        d = dict()
        for word in arr:
            if word in d:
                d[word] +=1
            else:
                d[word] = 1
        sorted = []
        greatest  = arr[0]
        for a in d:
            for key in d:
                if d[key]>d[greatest]:
                    greatest = key
            sorted.append(greatest)
            d[greatest]= -1
        return sorted

    finally:
        pass


def common_words_min(filename, min_chars):
    """question 1b

    Modify this function to take a second argument that specifies the
    minimum number of characters long a word can be to be counted.
    """
    try:
        f = open(filename)
        str = f.read()
        f.close
    except IOError:
        print ("File missing!")
    else:
        arr = str.split()
        d = dict()
        isempty = True
        for word in arr:
            if len(word) >min_chars:
                if word in d:
                    d[word] +=1
                else:
                    d[word] = 1
                    isempty = False
        sorted = []
        if isempty:
            return ["no words are over that num of chars"]
        else:
            greatest  = d.iterkeys().next()
            for a in d:
                for key in d:
                    if d[key]>d[greatest]:
                        greatest = key
                sorted.append(greatest)
                d[greatest]= -1
            
        return sorted

    finally:
        pass
    

def common_words_tuple(filename, min_chars):
    """question 1c

    Modify this function to return a list of tuples rather than just a list
    of strings. Each tuple should be of the format
        (word, number of occurrences)
    Of course, the list of tuples should still be sorted as in part a.
    """
    try:
        f = open(filename)
        str = f.read()
        f.close
    except IOError:
        print ("File missing!")
    else:
        arr = str.split()
        d = dict()
        for word in arr:
            if len(word) >min_chars:
                if word in d:
                    d[word] +=1
                else:
                    d[word] = 1
        sorted = []
        greatest  = arr[0]
        for a in d:
            for key in d:
                if d[key]>d[greatest]:
                    greatest = key
            sorted.append("("+greatest + ", " + d[greatest].__str__()+")")
            d[greatest]= -1
        return sorted

    finally:
        pass

def common_words_safe(filename, min_chars):
    """question 1d

    Modify your function so that it catches the IOError exception and prints
    a friendly error message.
    """
    try:
        f = open(filename)
        str = f.read()
        f.close
    except IOError:
        print ("File missing!")
    else:
        arr = str.split()
        d = dict()
        for word in arr:
            if len(word) >min_chars:
                if word in d:
                    d[word] +=1
                else:
                    d[word] = 1
        sorted = []
        greatest  = arr[0]
        for a in d:
            for key in d:
                if d[key]>d[greatest]:
                    greatest = key
            sorted.append("("+greatest + ", " + d[greatest].__str__()+")")
            d[greatest]= -1
        return sorted

    finally:
        pass
