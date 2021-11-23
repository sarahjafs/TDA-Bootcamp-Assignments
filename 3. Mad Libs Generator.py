def madlib():
    location = input ('Enter a location (eg, park, restaurant etc): ')
    name1 = input ('Enter name: ')
    position = input ('Enter a position (eg, out, in etc): ')
    name2 = input ('Enter another name: ')
    animal1 = input ('Enter an animal: ')
    length = input ('Enter a length of time (eg, one hour, thirty seconds etc): ')
    name3= input ('Enter a third name: ')
    animal2= input ('Enter another animal: ')
    sauce= input ('Enter name of a sauce you like (eg, ketchup etc): ')
    
    print('In this '+ location +' ' + name1 + ' looked ' + position + ' for ' + name2 + ', the pet ' + animal1 + '. ' + name1 + ' knew ' + name2 + ' would not be far. It had only been ' + length + ' since ' + name1 + ' had seen ' + name2 + '. How wonderful to be reunited with this most awesome ' + animal1 + '. Alas, who arrived was, ' + name3 + ', the ' + animal2 + '. ' + name3 + ', the ' + animal2 + ' had engulfed ' + name2 + ' and was bloodied from the massacre. Or so it seemed. On closer inspection, '+ name1 + ' was relieved to find it was a load of '+ sauce + ' that had spluttered all over. So where was '+ name2 + ', '+ name1 + 's pet '+ animal1 + '!')
    
    return 
# return is the ending
madlib()
# this step enables the function to run