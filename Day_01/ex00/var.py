def my_var():
    i = 42
    print (i, " est de type ", type(i))

    s = "42"
    print (s, " est de type ", type(s))

    string = "quarante-deux"
    print (string, " est de type ", type(string))

    f = 42.0
    print (f, " est de type ", type(f))

    b = True
    print (b, " est de type ", type(b))

    l = [42]
    print (l, " est de type ", type(l))

    d = {42: 42}
    print (d, " est de type ", type(d))

    t = (42,)
    print (t, " est de type ", type(t))

    my_set = set()
    print (my_set, " est de type ", type(my_set))




if __name__ == '__main__':
    my_var()