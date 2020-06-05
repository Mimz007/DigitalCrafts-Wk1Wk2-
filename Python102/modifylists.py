falcon_parts = ["Toplex", "V-5", "YT"]
print(falcon_parts)

hans_modifications = ["L3 + V-5 Nav", "SSP05 Hyperdrive"]
print(falcon_parts[1:3])

print(falcon_parts[1:3])

#How To #Append, Delete, Extend & Insert
del falcon_parts[len(falcon_parts)-1]    #HOW TO DELET AN ITEM FROM A LIST
print(falcon_parts)

#APPEND FUNCTION adds an item to the index
falcon_parts.append("AG-2G Laser Cannon")

#EXTEND allows you to add a list to the list
falcon_parts.extend("[sensor proof", "Aurodium-Plated]")
print(falcon_parts)

#INSERT puts an item where you want it to be, moving whats originally there to the next index
falcon_parts.insert(3, "Dejarik Board")
print(falcon_parts)

removed_part = falcon_parts.pop(0)
removed_part = falcon_parts.pop() #An empty argument pop removes the last item




