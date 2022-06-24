#Step 4: list for testing functionality of program
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

#step 5: Test traveler. 1) Name 2) Where he is right now 3) interests
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#step 8-10 : Get Destination index funnction from list provided
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

# step 11-14: Testing out the get_destination_index function
#print(get_destination_index("Los Angeles, USA"))
#print(get_destination_index("Paris, France"))
# this test returns a value error for not being in the destinations list
# print(get_destination_index("Hyderabad, India"))

# Step 15-18:get traveler location function. Pulls the destination from the test traveler information, and then plugs that destination into the function that rewturns the index of that location in our master destination list.
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# Step 19-20: Testing out the get_traveler_location function
test_destination_index = get_traveler_location(test_traveler) 
# print(test_destination_index)

#Step 24-25: creating empty list for attractions people can visit, allowing input of interesting places to visit for every destination in the destinations list.
attractions = []
for dest in destinations:
  attractions.append([])

#testing out creating an empty list using a loop. 
# print(attractions)

#step 27-32: This function will take our empty attractions list and add a destination to it in the same indexed position as where it is in our destinations list
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination

#step 33: Testing out function by adding attraction and printing result. 
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
# print(attractions)

#step 35: Adding more attractions using our new function
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

# print(attractions)

#step 38-50: Function that takes in a destination and list of interests, then pulls the attractions at that destination, and then sees if any interests the traveler has matches with the attractions at that destination and if the interest is found, that destination is appended to a new list and returned. 
def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = attraction
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

#Testing out find_atractions function
# la_arts = find_attractions("Los Angeles, USA", ['art'])
# print(la_arts)

#step 53-60: Creating a function that takes the traveler, runs ther=ir information through our other functions to find attractions based on interests, and returns the result as a string
def get_attractions_for_travelers(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi "
  interests_string = interests_string + traveler[0] + ", we think you'll like these places around " + traveler_destination + ": the "
  for attraction in traveler_attractions:
    interests_string = interests_string + attraction
  return interests_string

# Testing out the final function
smills_france = get_attractions_for_travelers(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)

