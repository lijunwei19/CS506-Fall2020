import math
def euclidean_dist(x, y):
    '''
        The Euclidean distance between points p and q is 
        the length of the line segment connecting them
    '''
    # error handling x, y have the same number of element
    # assert len(x) == len(y)

    #declear sum_square
    sum_squ = 0

    for x_i, y_i in zip(x ,y):
        sum_squ += (x_i-y_i)**2
    
    return  math.sqrt(sum_squ )

def manhattan_dist(x, y):
    '''
        Definition: The distance between two points measured
        along axes at right angles. In a plane with p1 at (x1, y1) 
        and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|
    '''
    
    # assert len(x)==len(y)
    sum = 0
    for xi, yi in zip(x ,y):
        sum += abs(xi -yi)
    return sum

def jaccard_dist(x, y):
    '''
        known as Intersection over Union. is a statistic used for gauging the similarity and diversity of sample sets
        number of different elements / unio elements of two set
    '''
      
    a = set(x) ; b =set(y)
    try:
        return 1-len(a&b) /(len(a)+len(b)-len(a&b)) 
    except ZeroDivisionError as e :
        print('cant '+str(e))
def cosine_sim(x, y):
    '''
        Cosine similarity is a measure of similarity between two non-zero vectors of an inner product space
    '''
    def norm (x):
        sum = 0
        for i in x:
            sum += i**2
        return math.sqrt(sum)
    norm_pro = norm(x)* norm(y)

    # assert norm_pro != 0

    inner_pro = 0
    for i, j in zip(x ,y):
        inner_pro += i*j

    try:
        return inner_pro / (norm_pro)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ") 

    

# Feel free to add more
def main():
    print(manhattan_dist([1,2,3],[2,3,5]))
    s1 = {}; s2 = {}
    print(jaccard_dist(s1,s2))

    print(cosine_sim([1,math.sqrt(3)], [1,0] ))

if __name__ == "__main__":
    main()