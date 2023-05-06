programing_dictionary = {"Bug" : "An error." , "Function" : "A piece. " , "loop ": "The action"}

programing_dictionary["loop "] = "over again"

print(programing_dictionary["Bug"])

empty_dictionary = {}

programing_dictionary = {}

programing_dictionary["Bug"] = "A moth"
print(programing_dictionary)

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])

student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

capitals = {
    "France": "Paris",
    "Germany" : "Berlin"
}

travel_log = {
    "France" : {"cities_visited " : ["Paris" , "Lille" , "Dijon"],"total_visits" : 12},
    "Germany" :{"cities_visited " : ["Berlin" , "Hamburg" , "Stuttgart"],"total_visits" : 5}
}

travel_log = [
    {
    "Country ": "France",
    "cities_visited " : ["Paris" , "Lille" , "Dijon"],
    "total_visits" : 12
    },

    {
    "Country ": "Germany",
    "cities_visited " : ["Berlin" , "Hamburg" , "Stuttgart"],
    "total_visits" : 5
    }
]

def add_new_country(country_visited , times_visited , cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
 
add_new_country("Russia" , 2 , ["Moscow" , "Saint Petersburg"])

print(travel_log)