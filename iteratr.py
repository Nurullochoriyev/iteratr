"while bilan ishlash"
a={1,2,3,4,5,6,7,8,9,12}
a_iter=iter(a)
result=0
while True:
    try:
        element=next(a_iter)
        if element%2==0:
            result+=element**2
    except StopIteration:
        break
print(result)


#
# f=range(1,100)
# f_iter=iter(f)
# for i in f_iter:
#     try:
#         print(next(f_iter))
#                     # faqat juftlarini oladi
#     except StopIteration:
#         break
#


"oop da ishlash"
# class JUFT:
#     def __init__(self,start,son):
#         self.son=son+1
#         self.srart=start-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#
#         self.srart+=1
#         if self.srart<self.son :
#             k=self.srart
#             return k
#         raise StopIteration
# for i in JUFT(1,10):
#     print(i)


# def sonlar(a,b):
#     for i in range(a,b):
#             yield i
#     # raise StopIteration
# start=1
# stop=10
# asd=sonlar(start,stop)
# for i in range(start,stop):
#     print(next(asd))








# "ananimus usuli"
# my_generatir=(i*i for i in range(1,10) if i%2==0 )
# while True:
#     try:
#         print(next(my_generatir))
#     except StopIteration:
#         break




# generatr=(i for i in range(30,1,-1) if i%2==0)
# while True:
#     try:
#         print(next(generatr))
#     except StopIteration:
#         break