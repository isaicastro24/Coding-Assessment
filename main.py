
restaurant_tables = [
        {"table_ID": 1, "amount_of_people": 2, "x": False},
        {"table_ID": 2, "amount_of_people": 4, "x": True},
        {"table_ID": 3, "amount_of_people": 2, "x": False},
        {"table_ID": 4, "amount_of_people": 6, "x": False},
        {"table_ID": 5, "amount_of_people": 4, "x": True},
        {"table_ID": 6, "amount_of_people": 8, "x": True},
        {"table_ID": 7, "amount_of_people": 8, "x": False}
]

# array of tables to choose from to sit different people

def list_free_tables(all_tables): # functions lists all free tables available 
    not_occupied_tables = [] # empty array so we can store our "free table" value
    for table in all_tables: # traverse our array of all tables to find singular tables
        occupied = table.get("x",True) # boolean value that check if table is occupied, if it is, returns true
        if occupied is False: # checks for false boolean of occupied, or not occupied
            not_occupied_tables.append(table.get("table_ID")) # adds not occupied tables to our empty array
    return not_occupied_tables # returns an array with only empty tables or not occupied 

def number_specific_table(all_tables,party): # returns only one table that does meet requirements (party size/avalibility)
    for table in all_tables: #traverses array of all tables to single out tables
        occupied = table.get("x",True) #boolean value that check if table is occupied, if it is, returns true
        if occupied is False and table["amount_of_people"] >= party: # checks if table is avaliable and can fit the party
            return table.get("table_ID") #returns first table that meets those requirements


#this function works the same as the previous one, but returns multiple tables
def number_specific_all_tables(all_tables, party):
    available_tables = [] # empty array to return multiple tables
    for table in all_tables:
        occupied = table.get("x",True)
        if occupied is False and table["amount_of_people"] >= party:
            available_tables.append(table.get("table_ID"))
    return available_tables #return ALL tables available

print("The available tables are tables:",list_free_tables(restaurant_tables))
print("A table that can sit a party of 2 is :", number_specific_table(restaurant_tables, 2))
print("Tables that can sit a party of 6 are :", number_specific_all_tables(restaurant_tables, 6))