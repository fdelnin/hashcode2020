import numpy

class Library:
    def __init__(self, id, n_books, signup, n_ship, all_books,books_dicts):
        self.id = (id)
        self.n_books = (n_books)
        self.signup = (signup)
        self.n_ship = (n_ship)
        self.all_books = all_books

        #self.my_points=self.signup+ self.n_books/self.n_ship
        totpoints=0
        for b in all_books:
            totpoints+= books_dicts[b]
            #print(books_dicts[b], b)
        #print("tot points",totpoints, n_books)
        self.my_points= totpoints

    def __repr__(self):
        return "ID: {}, N_BOoks: {}, signup: {}, shiprate: {}".format(self.id, self.n_books, self.signup,self.n_ship)

    def update_points(self,booktoremove):
       # print(self.all_books)
        for b in self.all_books:
            if b in booktoremove:
                self.all_books.remove(b)
        self.n_books=len(self.all_books)
        totpoints=0
        for b in self.all_books:
            totpoints+= books_dicts[b]
            #print(books_dicts[b], b)
       # print("tot points",totpoints, self.n_books)
        self.my_points= totpoints
        self.my_points=totpoints

def check_books(already_sent, new_books):
    #print("called check books")
    to_send =[]
    for b in new_books:
        if b not in already_sent:
            to_send.append(b)

    return to_send

def used_days(total_days, libs):
   # print("called used days")
    remaining = total_days
    books_sent = []
    libs_considered = []
    all=0
    while all< len(libs) and remaining>0:
        l=libs[0]
        if l.signup <= remaining:
           
            books_to_send = check_books(books_sent, l.all_books)
            if books_to_send !=[]:
                remaining-=l.signup
                libs_considered.append((l.id, books_to_send))
                books_sent.extend(books_to_send)
                libs.remove(l)
                for i in libs:
                    i.update_points(books_sent)
                libs.sort(key=lambda x: x.my_points, reverse=True)
                    
        all+=1
            

    return libs_considered

#f = open('../input/a_example.txt', 'r')
all_files= ['a_example','b_read_on', 'c_incunabula', 'd_tough_choices','e_so_many_books','f_libraries_of_the_world']
for a in all_files:
    filename = '../input/'+a+'.txt'
    print(filename)
    with open(filename) as f:
        input_f = f.read().splitlines() 

    input_n = []

    for l in input_f:
        l = [int(i) for i in l.split()]
        input_n.append(l)

    tot_libraries = input_n[0][0]
    tot_libs = input_n[0][1]
    tot_days = input_n[0][2]

    books_scores = input_n[1]
    #print(input_n)

    print("num of books %d, numbers of libs %d and numbers of days %d" % (tot_libraries,tot_libs,tot_days))
    #print("scores", books_scores)

    input_n = input_n[2:]
    #print(len(input_n))


    books_dicts = {}
    for i, b in enumerate(books_scores):
        books_dicts[i]=b
    #print(books_dicts)
    #order by value of the book
    #books_dicts = sorted(books_dicts, key=books_dicts.get, reverse=True)
   # print(books_dicts)

    libs = []
    count = 0
    #print(len(input_n))
    for i  in range(0, len(input_n)-1, 2):
    #  print(i, input_n[i])
        lib = Library(count, input_n[i][0], input_n[i][1], input_n[i][2], input_n[i+1],books_dicts)
        libs.append(lib)
        count+=1
    

    #print(libs)
    #sort libraries by sign up time or n ship?
    libs.sort(key=lambda x: x.my_points, reverse=True)
    print(libs[0], "last: ", libs[-1])
    #print(libs)
    libs_output = used_days(tot_days, libs)

    #print(libs_output)

    output_file = "../outputs/"+filename[9:-4]+'_output'

    o = open(output_file, 'w+')
    o.write(str(len(libs_output))+"\n")

    for l in libs_output:
        o.write(str(l[0])+" "+str(len(l[1]))+"\n")
        for single_book in l[1]:
            o.write(str(single_book)+" ")
        
        if l[1]==[]:
            print("EMPTY")
        o.write("\n")

    o.close()