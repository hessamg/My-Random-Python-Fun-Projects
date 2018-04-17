#   Sam Ganjian
#   3 April 2018

def plan_journey(trip_list):
    """Plans the Journey starting from your location.

    Args:
        trip_list: It is a list of places with [starting position, destination].

    Returns:
        the trip_list orginized.
    """
    index = 1 
    start = trip_list[0][0] 
    destination = trip_list[0][1] 

    
    while start != "YourPlace": #make sure that "YourPlace" is the starting index
        for trips in range(len(trip_list)): # go through the list
            if trip_list[trips][0] == "YourPlace":  #once "YourPlace" found
                start = trip_list[trips][0]         #stop the while loop
                destination = trip_list[trips][1]   #This is the new destionatin
                trip_list[0],trip_list[trips] = trip_list[trips],trip_list[0]   #put it on the first index
    
    for trips in range(len(trip_list)): 
        if trip_list[trips][0] == destination:  #if this is our next destination
            destination = trip_list[trips][1]   #update the destination
            trip_list[trips],trip_list[index] = trip_list[index],trip_list[trips] #swap with the next index
            index += 1        
                    
    return trip_list


trips = [["Cologne","Berlin"],["Berlin","Paris"],["Paris","London"],["Munich","Cologne"],["YourPlace","Munich"]]

print(plan_journey(trips))

