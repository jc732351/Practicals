"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""
# Create your main program in this file, using the TravelTrackerApp class

import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import copy
from place import Place
from placecollection import PlaceCollection


class HomeScreen(GridLayout):
    """Create kivy panel"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        """The entire GUI only needs two columns"""
        self.cols = 2

        #Set the first column

        """Add sort label and button"""
        self.layout_1 = GridLayout(cols=1,size_hint=(0.3, 1))
        self.layout_1.add_widget(Label(text='Sort by:'))

        self.layout_1.add_widget(Button(text='sort'))
        self.layout_1.add_widget(Label(text='Add New Place'))

        """Add name label and input"""
        self.layout_1.add_widget(Label(text='Name:'))
        name_input=TextInput()
        self.layout_1.add_widget(name_input)

        """Add country label and input"""
        self.layout_1.add_widget(Label(text='Country:'))
        country_input=TextInput()
        self.layout_1.add_widget(country_input)

        """Add priority label and input"""
        self.layout_1.add_widget(Label(text='Priority:'))
        priority_input=TextInput()
        self.layout_1.add_widget(priority_input)

        """Add button of add place"""
        self.layout_1.add_widget(Button(text='Add Place',on_press=lambda *args: self.add_input(name_input.text,country_input.text
                                                                                          ,priority_input.text)))
        """clear the input"""
        def clear(event):
            name_input.text=""
            country_input.text=""
            priority_input.text=""
        self.layout_1.add_widget(Button(text='Clear',on_press=clear))

        self.add_widget(self.layout_1)




        self.places = PlaceCollection()
        #Set the second column
        self.layout_2 = GridLayout(cols=1, )

        #Set the first label
        self.label_up=Label(text='Place to visited :'+str(self.places.get_num()),size_hint_y=0.25)
        self.layout_2.add_widget(self.label_up)
        # Add the place button
        for i in self.places.placeList:
            btn=self.get_button(i)
            self.button_list.append(btn)
            self.layout_2.add_widget(btn)

        self.label_down=Label(text='Welcome to Travel Tracker',size_hint_y=0.25)
        self.layout_2.add_widget(self.label_down)



        self.add_widget(self.layout_2)


    #generate place button
    def get_button(self,a):
        if a.visited_status=='(visited)':
            background_color=(0,0.3,0.3,1)
        else:
            background_color=(0, 0.5, 0.5, 1)
        btn=Button(text=a.__str__(), font_size=20,background_color =background_color)
        btn.bind(on_press=lambda *args: self.press_visit(a,btn, *args))
        return btn

    #the press function,set the nonvisited to visited
    def press_visit(self,p,btn,event):
        p.is_visited('v')
        btn.text=p.__str__()
        btn.background_color=(0,0.3,0.3,1)
        self.label_up.text='Place to visited :'+str(self.places.get_num())
        self.label_down.text='You visited '+p.name
        if self.places.get_num()==0:
            self.label_down.text='All fields are completed!'

    #set the add place to the second column
    def add_input(self,name,country,priority):
        self.places.add_place(name,country,priority)
        self.layout_2.add_widget(self.get_button(self.places.placeList[-1]),index=1)
        self.label_up.text = 'Place to visited :' + str(self.places.get_num())
        self.places.save_places()



class TravelTrackerApp(App):
    """..."""
    def build(self):
        return HomeScreen()

if __name__ == '__main__':
    TravelTrackerApp().run()
