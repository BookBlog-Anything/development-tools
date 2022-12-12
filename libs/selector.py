
class Selector():
    def __init__(self,selection_options_array, primary_heading=None) -> None:
        self.optionsArray = selection_options_array
        self.primaryHeading = primary_heading
        
    def check(self,selected_value):
        if int(len(self.optionsArray)) >= int(selected_value):
            selected_option = self.optionsArray[(int(selected_value) - 1)]
            return True
        else:
            return False

    def get(self, selected_value):
        if int(len(self.optionsArray)) >= int(selected_value):
            selected_option = self.optionsArray[int(selected_value)]
            return selected_option
        else:
            return False

    def main(self):
        if len(self.optionsArray) != 0:
            update_option_selection = ''
            for i in range(len(self.optionsArray)):
                update_option_selection += "\n%s) %s" % ((i + 1),self.optionsArray[i])

            selector_input = False
            while True:
                selector_input = input("\n%s\n\n%s (): " % (update_option_selection,self.primaryHeading))
                selector_input_check = self.check(selector_input)
                if selector_input_check == True: 
                    return (int(selector_input)-1)
                    break
                else:
                    self.primaryHeading = "Choose valid option"
                    self.main()
                
        else:
            print("WIthout Array")
                    
    #     pass
    # if selected_value or selected_value != None :
    #     # print(int(len(selection_options_array)),int(selected_value))
    #     if int(len(selection_options_array)) >= int(selected_value):
    #         selected_option = selection_options_array[(int(selected_value) - 1)]
    #         return (int(selected_value)-1)
    #     else:
    #         return False
    # else:
