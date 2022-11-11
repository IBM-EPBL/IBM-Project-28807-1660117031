# Python program to find PNR
# status using RAILWAY API

# import required modules
import requests, json

# Enter API key here
api_key = "Your_API_key"

# base_url variable to store url
base_url = "https://api.railwayapi.com/v2/pnr-status/pnr/"

# Enter valid pnr_number
pnr_number = "6515483790"

# Stores complete url address
complete_url = base_url + pnr_number + "/apikey/" + api_key + "/"

# get method of requests module
# return response object
response_ob = requests.get(complete_url)

# json method of response object convert
# json format data into python format data
result = response_ob.json()

# now result contains list
# of nested dictionaries
if result["response_code"] == 200:

	# train name is extracting
	# from the result variable data
	train_name = result["train"]["name"]

	# train number is extracting from
	# the result variable data
	train_number = result["train"]["number"]

	# from station name is extracting
	# from the result variable data
	from_station = result["from_station"]["name"]

	# to_station name is extracting from
	# the result variable data
	to_station = result["to_station"]["name"]

	# boarding point station name is
	# extracting from the result variable data
	boarding_point = result["boarding_point"]["name"]

	# reservation upto station name is
	# extracting from the result variable data
	reservation_upto = result["reservation_upto"]["name"]

	# store the value or data of "pnr"
	# key in pnr_num variable
	pnr_num = result["pnr"]

	# store the value or data of "doj" key
	# in variable date_of_journey variable
	date_of_journey = result["doj"]

	# store the value or data of
	# "total_passengers" key in variable
	total_passengers = result["total_passengers"]

	# store the value or data of "passengers"
	# key in variable passengers_list
	passengers_list = result["passengers"]

	# store the value or data of
	# "chart_prepared" key in variable
	chart_prepared = result["chart_prepared"]

	# print following values
	print(" train name : " + str(train_name)
		+ "\n train number : " + str(train_number)
		+ "\n from station : " + str(from_station)
		+ "\n to station : " + str(to_station)
		+ "\n boarding point : " + str(boarding_point)
		+ "\n reservation upto : " + str(reservation_upto)
		+ "\n pnr number : " + str(pnr_num)
		+ "\n date of journey : " + str(date_of_journey)
		+ "\n total no. of passengers: " + str(total_passengers)
		+ "\n chart prepared : " + str(chart_prepared))

	# looping through passenger list
	for passenger in passengers_list:
		
		# store the value or data
		# of "no" key in variable
		passenger_num = passenger["no"]

		# store the value or data of
		# "current_status" key in variable
		current_status = passenger["current_status"]

		# store the value or data of
		# "booking_status" key in variable
		booking_status = passenger["booking_status"]

		# print following values
		print(" passenger number : " + str(passenger_num)
			+ "\n current status : " + str(current_status)
			+ "\n booking_status : " + str(booking_status))

else:
	print("Record Not Found")
