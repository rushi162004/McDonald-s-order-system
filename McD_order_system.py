#!/usr/bin/env python
# coding: utf-8

# In[32]:


get_ipython().system('pip install emoji')
import emoji
items = {"Burger" : 50,"Fries":30,"Coke":20,"McFlurry":60}


# In[33]:


# place a new a new order
def order_val_cal(dic, num, num1):
    """
    dic: dictionary of menu items and their prices
    num: index number of the item chosen
    num1: number of items ordered
    Returns: total cost for the item if valid, otherwise prompts the user to choose a valid option.
    """
    item_list = list(dic.keys())
    
    # Validate if the selected item number is within the range of available items
    if num < 1 or num > len(item_list):
        return emoji.emojize(":warning: Invalid item number! Please choose a valid option.", language='alias')
    
    # Calculate the total cost of the chosen item
    return dic[item_list[num-1]] * num1


# In[34]:


def order_item_val(dic,num):
    '''here dic takes the argument of items dict of menu 
    num takes the argument given by user the order he would like to receive '''
    item_list = list(dic.keys())
    return item_list[num-1]


# In[35]:


def order_items(dic,order_item,num_item):
    st ={}
    st[order_item_val(dic,order_item)] = [num_item,order_val_cal(dic,order_item,num_item)]
    return st


# In[36]:


def initiate_order_id(num=0,**kwargs):
    num+=1
    return num


# In[37]:


def display_information(lst,num):
    total = 0
    x = " "
    print("="*40)
    print(emoji.emojize(f":page_with_curl: Order Summary for Order ID: {num}".center(40), language='alias'))
    print("="*40)
    
    for ind, elm in enumerate(lst):
        item = list(elm.keys())[0]
        quantity = elm[item][0]
        price = elm[item][1]
        total += price
        print(f"{x*5}{ind+1}. {item.ljust(25, '.')} x {quantity} = ₹{price}")

    print("="*40)
    print(f"{x*5}Total Amount: ₹{total}".rjust(40))
    print("="*40)


# In[ ]:





# In[38]:


def full_order(dic, ord_dic, order_id, **kwargs):
    print("="*40)
    print(emoji.emojize(f":shopping_cart: Starting New Order: {order_id}".center(40), language='alias'))
    print("="*40)
    
    item_list = list(dic.keys())
    order_item = int(input(emoji.emojize("\n :hamburger: Enter the item number to add (or 0 to finish): ", language='alias')))
    lis = []

    while order_item != 0:
        # Validation check: ensure order_item is within valid range
        if order_item < 1 or order_item > len(item_list):
            print(emoji.emojize(":warning: Invalid item number! Please choose a valid option from the menu.", language='alias'))
        else:
            num_item = int(input(emoji.emojize(":input_numbers: How many of this item would you like to order? ", language='alias')))
            
            # Add or update the item in the order list
            y = order_items(dic, order_item, num_item)
            item_added = False
            
            # Checking if the item is already in the order and update quantities/prices if needed
            for elm in lis:
                if list(y.keys())[0] == list(elm.keys())[0]:
                    elm[list(elm.keys())[0]][0] += y[list(y.keys())[0]][0]  # Update quantity
                    elm[list(elm.keys())[0]][1] += y[list(y.keys())[0]][1]  # Update total price
                    item_added = True
                    break
            
            # If the item wasn't found in the list, add it as a new entry
            if not item_added:
                lis.append(y)

            # Display updated order information
            print(emoji.emojize("\n :receipt: Updated Order Summary:\n", language='alias'))
            display_information(lis, order_id)
        
        # Prompt for the next item
        order_item = int(input(emoji.emojize("\n :hamburger: Enter the item number to add (or 0 to finish): ", language='alias')))

    # Checking if the list is not empty before saving the order
    if lis:
        ord_dic[order_id] = lis
        print(emoji.emojize("\n :white_check_mark: Order saved successfully!\n", language='alias'))
        return ord_dic
    else:
        print(emoji.emojize("\n :cross_mark: No items were added to the order.\n", language='alias'))
        return ord_dic


# In[39]:


main_order_id = {}
items = {"Burger" : 50,"Fries":30,"Coke":20,"McFlurry":60}


# In[40]:


def placing_order(dic,menu):
    try:
        last_order_id = list(dic)[-1]
    except:
        last_order_id = 0
    order_id = initiate_order_id(last_order_id)
    x = full_order(menu,dic,order_id)
    dic.update(x)
#     else:
#         dic.update(x)
    return display_information(dic[order_id],order_id)


# In[41]:


def all_information(dic):
    print("="*40)
    print(emoji.emojize(":star2: Welcome to McDonald's :star2:".center(60),language='alias'))
    print("="*40)
    print("\nToday's Menu:\n")
    for ind, elm in enumerate(dic):
        print(f" {ind+1}. {elm.ljust(30, '.')} ₹{dic[elm]}")
    print("="*40)


# In[ ]:





# In[42]:


def update_order(dic, menu):
    print("=" * 40)
    print(emoji.emojize(":arrows_counterclockwise: Update Existing Order".center(40), language='alias'))
    print("=" * 40)
    
    # Code for Order ID to update
    update_id = int(input(emoji.emojize("\n:id: Enter the Order ID you would like to update: ", language='alias')))
    display_information(dic[update_id], update_id)

    change_item = int(input(emoji.emojize("\n:pencil2: Choose the item number you would like to change (or type 0 to exit): ", language='alias')))

    while change_item != 0:
        try:
            print(emoji.emojize("\n:clipboard: Current Order Summary:", language='alias'))
            display_information(dic[update_id], update_id)

            # Get item to change
            item_name = list(dic[update_id][change_item - 1].keys())[0]
            change_position = dic[update_id][change_item - 1][item_name]

            # Code for updated quantity
            num_item = int(input(emoji.emojize(f"\n:1234: How many '{item_name}' would you like to order? (Current: {change_position[0]}): ", language='alias')))
            change_position[0] = num_item
            change_position[1] = num_item * menu[item_name]

            print(emoji.emojize("\n:white_check_mark: Item updated successfully!", language='alias'))
            display_information(dic[update_id], update_id)

            change_item = int(input(emoji.emojize("\n:pencil2: Choose another item to update or type 0 to exit: ", language='alias')))
        
        except:
            print(emoji.emojize("\n:warning: Invalid choice! Please select a valid item from the menu.", language='alias'))
            all_information(menu)
            new_item = int(input(emoji.emojize("\n:hamburger: Enter the number of the new item you would like to order: ", language='alias')))
            num_item = int(input(emoji.emojize(f"\n:1234: How many '{list(menu.keys())[new_item - 1]}' would you like to order? ", language='alias')))

            dic[update_id].append(order_items(menu, new_item, num_item))
            print(emoji.emojize("\n:white_check_mark: New item added successfully!", language='alias'))
            display_information(dic[update_id], update_id)

            change_item = int(input(emoji.emojize("\n:pencil2: Choose another item to update or type 0 to exit: ", language='alias')))

    print(emoji.emojize("\n:floppy_disk: Final Updated Order:", language='alias'))
    return display_information(dic[update_id], update_id)


# In[ ]:





# In[43]:


def search_order(dic):
    print("=" * 40)
    print(emoji.emojize(":mag_right: Search Order".center(40), language='alias'))
    print("=" * 40)
    
    num = int(input(emoji.emojize("\n:id: Enter the Order ID number: ", language='alias')))
    
    try:
        print(emoji.emojize(f"\n:page_with_curl: Displaying Order ID: {num}", language='alias'))
        return display_information(dic[num], num)
    except KeyError:
        return emoji.emojize(f"\n:warning: Order ID {num} does not exist", language='alias')


# In[44]:


def all_order(dic):
    for _id in dic:
        x = display_information(dic[_id],_id)
        if x:
            print(x)
        else:
            pass


# In[ ]:





# In[ ]:





# In[45]:


def delete_order(dic):
    print("=" * 40)
    print(emoji.emojize(":wastebasket: Delete Item from Order".center(40), language='alias'))
    print("=" * 40)

    delete_id = int(input(emoji.emojize("\n:id: Enter the Order ID from which you would like to delete an item: ", language='alias')))
    
    # Display current order details before deleting items
    display_information(dic[delete_id], delete_id)

    delete_item = int(input(emoji.emojize("\n:cross_mark: Enter the item number you would like to remove (or type 0 to exit): ", language='alias')))
    
    while delete_item != 0:
        try:
            # Remove the item based on the index provided by the user
            dic[delete_id].remove(dic[delete_id][delete_item - 1])
            print(emoji.emojize(f"\n:white_check_mark: Item {delete_item} removed successfully!", language='alias'))
            
            # Show updated order
            display_information(dic[delete_id], delete_id)
            
            # Prompt again to either remove more items or exit
            delete_item = int(input(emoji.emojize("\n:cross_mark: Enter another item number to remove (or type 0 to exit): ", language='alias')))
        
        except IndexError:
            print(emoji.emojize("\n:warning: Invalid item number! Please select a valid item.", language='alias'))
            delete_item = int(input(emoji.emojize("\n:cross_mark: Enter the item number you would like to remove (or type 0 to exit): ", language='alias')))

    print(emoji.emojize("\n:floppy_disk: Final Updated Order:", language='alias'))
    return display_information(dic[delete_id], delete_id)


# In[ ]:





# In[46]:


main_order_id = {}
items = {"Burger": 50, "Fries": 30, "Coke": 20, "McFlurry": 60}

def main(main_order_id, items):
    print("=" * 40)
    print(emoji.emojize(":house: Welcome to McDonald's Ordering System".center(40), language='alias'))
    print("=" * 40)
    
    all_information(items)
    
    action_id = int(input(emoji.emojize("\n:arrow_forward: Choose an action:\n"
                                        ":one: Place a new order\n"
                                        ":two: Update an existing order\n"
                                        ":three: Search for an order\n"
                                        ":four: Delete an order\n"
                                        ":five: Show all orders\n"
                                        ":six: Exit\n"
                                        ":question: Enter the number of your choice: ", language='alias')))
    
    while action_id != 6:
        if action_id == 1:
            placing_order(main_order_id, items)
        elif action_id == 2:
            update_order(main_order_id, items)
        elif action_id == 3:
            search_order(main_order_id)
        elif action_id == 4:
            delete_order(main_order_id)
        elif action_id == 5:
            all_order(main_order_id)
        else:
            print(emoji.emojize("\n:warning: Invalid choice! Please choose a valid action.", language='alias'))
        
        # Prompt for next action after completing the previous one
        action_id = int(input(emoji.emojize("\n:arrow_forward: Choose an action:\n"
                                            ":one: Place a new order\n"
                                            ":two: Update an existing order\n"
                                            ":three: Search for an order\n"
                                            ":four: Delete an order\n"
                                            ":five: Show all orders\n"
                                            ":six: Exit\n"
                                            ":question: Enter the number of your choice: ", language='alias')))
    
    print(emoji.emojize("\n:wave: Thank you for using McDonald's Ordering System! Have a great day!", language='alias'))

    


# In[47]:


main(main_order_id,items)


# In[ ]:




