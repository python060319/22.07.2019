
d = { 'b' : 2, 'a' : 1, 'hello' : True, 'c' : 5 }

def tryGetValue(d, k):
    '''
    check if k (key) exist in d (dictionary)
    :param d: dictionary
    :param k: key
    :return: value in dictionary for k
    '''
    # return d.get(k) -- does the same
    if k in d.keys():
        return d[k]
    else:
        return None


def getSortedKeys(d):
    '''
    returnr sorted keys
    :param d: dictionary
    :return: sorted keys
    '''
    return sorted(d.keys())

def mergeDictionary(d1, d2):
    '''
    merges two dictionaries
    :param d1: dictonary 1
    :param d2: dictonary 2
    :return: d1 merged with d2
    '''
    result = d1.copy()
    for k,v in d2.items():
        if result.get(k) != None:
            result[k] = [result[k], v]
        else:
            result[k] = v
    return result

print(getSortedKeys(d))
d1 = { 1:'a', 2:'b', 5:'d', 8:'aa'}
d2 = { 1:'t', 2:'3', 7:'d', 11:'aa'}
print(mergeDictionary(d1, d2))

# dictionary comprehension
d3 = {f'{n}^3':n**3 for n in range(1, 5)}

print(d3)

print( [10**n for n in range(1, 9)])

def getData():
    id = int(input("Please enter ID: "))
    persons = { }
    while id != -1:
        if persons.get(id):
            print(f'{id} already exist!')
        else:
            name = input("Please enter your name: ")
            persons[id] = name
        id = int(input("Please enter ID: "))
    print(persons)

#getData()
'''
0 .כיצד אפשר לקבל את כל הערכים הקיימים ב dictionary?
:כדי List Comprehension ב השתמש ”. I love to eat ice cream in the beach” המשפט נתון. 11
• לייצר רשימה של המילים באותיות גדולות
• לייצר רשימה של אותיות- מהאות הראשונה בכל מילה
• לייצר רשימה של אותיות- מהאות השלישית בכל מילה )היכן שאפשר(
• לייצר רשימה של מספרים אשר מייצגים אורך של כל מילה ומילה
'''
sent = "I love to eat ice cream in the beach"
print([ word.upper() for word in sent.split() ])
print([ word[0] for word in sent.split() ])
print([ word[2] for word in sent.split() if len(word)>2 ])
print([ word[2:] for word in sent.split() if len(word)>2 ])
print([ len(word) for word in sent.split()  ])




