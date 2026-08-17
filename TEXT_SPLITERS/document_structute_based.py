
# from langchain.text_spliter import RecursiveCharacterTextSplitter , Language

# text = """ # Parent Class
# class Animal:
#     def speak(self):
#         print("Animals can make sounds")

# # Child Class 1
# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# # Child Class 2
# class Cat(Animal):
#     def meow(self):
#         print("Cat meows")

# # Child Class 3
# class Cow(Animal):
#     def moo(self):
#         print("Cow moos")

# # Creating objects
# d = Dog()
# c = Cat()
# cw = Cow()

# # Calling methods
# d.speak()
# d.bark()

# c.speak()
# c.meow()

# cw.speak()
# cw.moo()"""

# # initializing the spliter 
# splitter = RecursiveCharacterTextSplitter.format_language(
#     language = Lnaguage.PYTHON,
#     chunk_overlap = 0
# )

# # perform the split

# chunks = splitter.split_text(text)

# print(len(chunks))
# print(chunks[1])