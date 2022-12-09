
def selector(selection_options_array,selected_value=None):
    if selected_value != None:
        print(int(len(selection_options_array)),int(selected_value))
        if int(len(selection_options_array)) >= int(selected_value):
            selected_option = selection_options_array[(int(selected_value) - 1)]
            print(selected_option)
        else:
            print("dont exist")    
    else:
        return_selection_option = ''
        for i in range(len(selection_options_array)):
            return_selection_option += "\n%s) %s" % ((i + 1),selection_options_array[i])
        
        return return_selection_option
