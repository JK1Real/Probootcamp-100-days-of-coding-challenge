def add(*argss):
    su = sum(argss)
    print(su)

add(1,2)


def strings(**st):
    su=st.values()
    print(sum(su))

strings(a=1,b=2)