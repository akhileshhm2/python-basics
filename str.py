# str1="akhilesh"
# print(str1[2])


# str2="akhilesh hm "
# # print(str2[0:4])
# # print(str2[9:11])
# print(str2[-3:-1])
# print(str2[-8:-5])

txt="Akhilesh"
print(txt.upper())

txt2="Captain"
print(txt2.lower())

txt3=" hello,world "
print(txt3.strip())

txt4="hello, world"
print(txt4.replace("world","boy"))

txt5="my name is akhilesh"
print(txt5.split(" "))

a="akhilesh"
b="hm"
c=a+b
print(c)

d="akhilesh"
e="hm"
c=d + " " +e
print(c)



num=18
txt=f"the number of virat is {num}"
print(txt)

price=20.190
txt=f"for rupees {price:.2f} u get 4 tomatoes"
print(txt)

txt=f"for 2kg the price is {20*2} "
print(txt)

txt="go back home"
res=txt.count("g")
print(res)

txt="I love apples, apple are my favorite fruit"
res=txt.count("apple",0,24)
print(res)

txt="I love apples, apple are my favorite fruit"
res=txt.endswith("t")
print(res)