'''
Python Program to Check Weather Forecast
'''

# Import the necessary modules!
import requests

# Input the city name
city = input('Enter City name: ')

# Or you can also hard-code the value
# city = 'Irkutsk'

# Display the message
print('Displaying Weater report for: ' + city)

# Fetch the weater details
url = 'https://wttr.in/{}'.format(city) # Use of format to pass city as a parameter here
res = requests.get(url)                 # Make use of the requests module

# Display the result
# Resultant data is stored in res. 
# Use of the text method to extract our desired weather details to display the result
print(res.text)