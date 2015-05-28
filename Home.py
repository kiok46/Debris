from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView

Builder.load_file('poe.kv')
Builder.load_file('add_debris_select.kv')
Builder.load_file('delete_debris.kv')
Builder.load_file('map_data.kv')
Builder.load_file('create_database.kv')
Builder.load_file('select_database.kv')
Builder.load_file('display_database.kv')
Builder.load_file('initials_database.kv')

#----------------------------------------------------------------------------------------#

class Home(BoxLayout):
    sm = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Home,self).__init__(**kwargs)
        #self.sm.transition = 'SwapTransition'

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#                ''' Create the database part ''' 

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

class Create_database(BoxLayout):
    def __init__(self,**kwargs):
        super(Create_database,self).__init__(**kwargs)
        
    def on_release(self):
        self.parent.parent.current = 'home'
        self.parent.parent.transition.direction = 'down'
        
    def on_back(self):
        self.parent.parent.transition.direction = 'up'
        self.parent.parent.current = 'initials_database'


class Initials_database(FloatLayout):
    def __init__(self,**kwargs):
        super(Initials_database,self).__init__(**kwargs)
        
    def on_release(self):
        self.parent.parent.current = 'display_database'
        
    def on_back(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'create_database'
    
    def on_poe(self):
        self.parent.parent.current = 'poe'
        self.parent.parent.transition.direction = 'up'
        

#----------------------------------------------------------------------------------------#


class POE(BoxLayout):
    def __init__(self,**kwargs):
        super(POE,self).__init__(**kwargs)
        
    def on_back(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'initials_database'


#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#                ''' Select the database part ''' 

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

class Select_database(BoxLayout):
    select_database = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Select_database,self).__init__(**kwargs)
        self.orientation = 'vertical'

    def on_release(self):
        self.parent.parent.current = 'display_database'
        
    def on_back(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'home'
        



class Display_database(FloatLayout):
    def __init__(self,**kwargs):
        super(Display_database,self).__init__(**kwargs)
        
        
    def on_release(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'select_database'
        
    def on_add_debris(self):
        self.parent.parent.current = 'add_debris_select'
        self.parent.parent.transition.direction = 'right'

#----------------------------------------------------------------------------------------#


class Add_debris_select(BoxLayout):
    def __init__(self,**kwargs):
        super(Add_debris_select,self).__init__(**kwargs)
        
    def on_back(self):
        self.parent.parent.transition.direction = 'left'
        self.parent.parent.current = 'display_database'


#----------------------------------------------------------------------------------------#


class Delete_Debris(BoxLayout):
    def __init__(self,**kwargs):
        super(Delete_Debris,self).__init__(**kwargs)



#----------------------------------------------------------------------------------------#


class Map_Data(BoxLayout):
    def __init__(self,**kwargs):
        super(Map_Data,self).__init__(**kwargs)



#----------------------------------------------------------------------------------------#


class HomeApp(App):
    def build(self):
        self.title = "Debris Collection Software"
        return Home()

if __name__=='__main__':
    HomeApp().run()