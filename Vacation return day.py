#Michael Graham
#02/08/2026
#this program find the return date for a vacation
vacationStart=int(input('What day does your vacation start? (Enter 0 for Sunday, 1 for Monday, 2 for Tuesday, 3 for Wednesday, 4 for Thursday, 5 for Friday, 6 for Saturday) '))
vacationLength=int(input('How many days will your vacation be? ')) #ask user for start day
returnDay=(vacationLength+vacationStart)%7 #function to calculate day of return
print(f"You will return on day {returnDay}.") #output provided
