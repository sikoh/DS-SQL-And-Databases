import sqlite3
# Step 1 - Connect to the Database
connection = sqlite3.connect("Introduction-To-SQL/rpg_db.sqlite3")

# Step 2 - Make the "cursor"
cursor = connection.cursor()

# Step 3 - Write your query
#`TOTAL_CHARACTERS`: How many total Characters are there?
TOTAL_CHARACTERS = "SELECT COUNT(*) FROM charactercreator_character AS cc_char"
TOTAL_SUBCLASS = "SELECT * FROM charactercreator_necromancer"
TOTAL_ITEMS = "SELECT COUNT(*) FROM armory_item"
WEAPONS = "SELECT COUNT(*) FROM armory_weapon"
NON_WEAPONS = "SELECT COUNT(*) FROM armory_item as item LEFT JOIN armory_weapon as weapon ON weapon.item_ptr_id = item.item_id WHERE item_ptr_id IS NULL"
CHARACTER_ITEMS = "SELECT character_id, COUNT(item_id) FROM charactercreator_character_inventory GROUP BY character_id"
CHARACTER_WEAPONS = "SELECT character_id, COUNT(item_ptr_id) as number_of_weapons FROM armory_weapon as weapon LEFT JOIN charactercreator_character_inventory as cc_char_inv ON weapon.item_ptr_id = cc_char_inv.item_id GROUP BY character_id"
AVG_CHARACTER_ITEMS = "SELECT AVG(number_of_items) FROM(SELECT COUNT(item_id) as number_of_items FROM charactercreator_character_inventory GROUP BY character_id)"
AVG_CHARACTER_WEAPONS = "SELECT AVG(number_of_weapons) FROM(SELECT COUNT(item_ptr_id) as number_of_weapons FROM armory_weapon as weapon LEFT JOIN charactercreator_character_inventory as cc_char_inv ON weapon.item_ptr_id = cc_char_inv.item_id GROUP BY character_id)"

# Step 4 - Execute your query on the cursor
# Step 5 - Pull the results from the cursor
def execute_query(some_query):
    cursor.execute(some_query)
    result = cursor.fetchall()
    return result


# print(execute_query(TOTAL_CHARACTERS)[0][0], 'TOTAL_CHARACTERS')
# print(execute_query(TOTAL_SUBCLASS))
# print(execute_query(TOTAL_ITEMS)[0][0], 'TOTAL_ITEMS')
# print(execute_query(WEAPONS)[0][0], 'WEAPONS')
# print(execute_query(NON_WEAPONS)[0][0])
# print(execute_query(CHARACTER_ITEMS))
# print(execute_query(CHARACTER_WEAPONS))
# print(execute_query(AVG_CHARACTER_ITEMS)[0][0])
# print(execute_query(AVG_CHARACTER_WEAPONS)[0][0])
