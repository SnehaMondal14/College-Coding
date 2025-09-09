info = {
    "key":"value",
    "name" : "sneha",
    "age" : 20,
    "is_adult": True,
    "marks": 95.6
    }
print(info)




#nested dictionary

students = {
    "name" : "sneha",
    "roll": 233,
    "subjects" : {
        "physics" : 98,
        "chemistry" :95,
        "biology" : 84
    }
} 
print(students ["subjects"] ["physics"])





#mydict.keys


students = {
    "name" : "sneha",
    "roll": 233,
    "subjects" : {
        "physics" : 98,
        "chemistry" :95,
        "biology" : 84
    }
} 
print(students.keys())





#list 


students = {
    "name" : "sneha",
    "roll": 233,
    "subjects" : {
        "physics" : 98,
        "chemistry" :95,
        "biology" : 84
    }
} 
print(list(students.keys()))




#value 




students = {
    "name" : "sneha",
    "roll": 233,
    "subjects" : {
        "physics" : 98,
        "chemistry" :95,
        "biology" : 84
    }
} 
print(list(students.values()))



