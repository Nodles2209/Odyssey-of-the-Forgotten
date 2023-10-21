
entrance = {
		#Name of room (String)
		"id":"Entrance"
		#Shortened name for displaying map, might add a map legend to the display map function later (String)
		"map_id":"En"
		#Type of room (eg "riddle", "puzzle", "event") (String)
		"roomtype":"event"
		#visited (Only the rooms you want to appear immediatly should this be set to True) (Boolean)
		"visited":True
		#required room. 0 if optional room. 1-2-3-4.. for the order after that for required rooms(enterance begins as 1), necessary for map creation (Int)
		"required":1
		#score given to player upon completion of room (Int)
		"complete_room_score":1000
		# List of items in room as "id" of the item (List[item_id])
		"item_list":["temporary"]
		#The first promt that appears when the player enters the room for the first time, things like what the room is and what it looks like (String)
		"first_prompt":"You wake up and you are in an unfamilair place...."
		# The prompt that appears when the player enters the room for all times after the first time (String)
		"enter_promt":"You are back in the first room...."
		#Hint (doesnt always apply) (String)
		"hint":"Find all the parts for the plane in other places around the map"
		# prompt for when the player completes the room (String)
		"win_prompt":"You completed this room...."
		}