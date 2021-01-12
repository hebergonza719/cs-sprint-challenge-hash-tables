#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    route = [None] * length

    for i in range(length):
        hash_table[tickets[i].source] = tickets[i].destination

    source = "NONE"
    location = "HOME"
    idx = 0
    while location != "NONE":
        route[idx] = hash_table[source]
        # update source to new airport
        source = hash_table[source]
        location = hash_table[source]
        idx = idx + 1


    route[idx] = location
    
    return route

ticket_1 = Ticket("DCA", "NONE")
ticket_2 = Ticket("NONE", "PDX")
ticket_3 = Ticket("PDX", "DCA")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))