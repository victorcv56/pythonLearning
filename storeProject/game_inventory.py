import storeClass as store
name_of_file = input("Enter name of file: \n")
filename = name_of_file + '.json'


#initialize store object
store_front = store.gameInventory(filename)
store_front.see_inventory()
