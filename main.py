from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout

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
    
    get_name_of_entry = ObjectProperty(None)
    get_place_of_explosion = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(Create_database,self).__init__(**kwargs)
        
    def on_release(self):
        self.parent.parent.current = 'home'
        self.parent.parent.transition.direction = 'down'
        
    def on_back(self):
        self.parent.parent.transition.direction = 'up'
        self.parent.parent.current = 'initials_database'


class Initials_database(BoxLayout):
    def __init__(self,**kwargs):
        super(Initials_database,self).__init__(**kwargs)
        self.orientation = 'vertical'
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
    
    poe_id = ObjectProperty(None)
    get_poe_id = ObjectProperty(None)
    poe_long = ObjectProperty(None)
    get_poe_long = ObjectProperty(None)
    poe_lat = ObjectProperty(None)
    get_poe_lat = ObjectProperty(None)
    poe_charge_weight = ObjectProperty(None)
    get_poe_charge_weight = ObjectProperty(None)
    poe_diameter = ObjectProperty(None)
    get_poe_diameter = ObjectProperty(None)
    poe_depth = ObjectProperty(None)
    get_poe_depth = ObjectProperty(None)
    poe_remark = ObjectProperty(None)
    get_poe_remark = ObjectProperty(None)
    
    def __init__(self,**kwargs):
        super(POE,self).__init__(**kwargs)
        
    def on_back(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'initials_database'



#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#                ''' Select the database part ''' 

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

class Select_database(BoxLayout):
    select_database = ObjectProperty(None)
    carousel = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Select_database,self).__init__(**kwargs)
        self.orientation = 'vertical'

    def on_release(self):
        self.parent.parent.current = 'display_database'
        
    def on_back(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'home'
        



class Display_database(GridLayout):
    def __init__(self,**kwargs):
        super(Display_database,self).__init__(**kwargs)
        self.cols = 2
        
    def on_release(self):
        self.parent.parent.transition.direction = 'down'
        self.parent.parent.current = 'select_database'
        
    def on_add_debris(self):
        self.parent.parent.current = 'add_debris_select'
        self.parent.parent.transition.direction = 'right'
    
    def on_map_data(self):
        self.parent.parent.current = 'map_data'
        self.parent.parent.transition.direction = 'left'
    

#----------------------------------------------------------------------------------------#


class Add_debris_select(BoxLayout):
    debris_id = ObjectProperty(None)
    get_debris_id = ObjectProperty(None)
    debris_type = ObjectProperty(None)
    get_debris_type = ObjectProperty(None)
    debris_weight = ObjectProperty(None)
    get_debris_weight = ObjectProperty(None)
    debris_lat = ObjectProperty(None)
    get_debris_lat = ObjectProperty(None)
    debris_long = ObjectProperty(None)
    get_debris_long = ObjectProperty(None)
    add_debris_to_db = ObjectProperty(None) 

    def __init__(self,**kwargs):
        super(Add_debris_select,self).__init__(**kwargs)
        
    def on_back(self):
        self.parent.parent.transition.direction = 'left'
        self.parent.parent.current = 'display_database'
        
    def on_dismiss(self, arg):
        pass

    def not_full_info(self,event):
        self.popup = Popup(title= "Information",
        content = Info_Pop(),
        size_hint=(None, None), size=(self.width/2, self.height/2))
        self.popup.bind(on_dismiss = self.on_dismiss)
        self.popup.open() 
#----------------------------------------------------------------------------------------#


class Delete_Debris(BoxLayout):
    def __init__(self,**kwargs):
        super(Delete_Debris,self).__init__(**kwargs)



#----------------------------------------------------------------------------------------#


class Map_Data(BoxLayout):
    def __init__(self,**kwargs):
        super(Map_Data,self).__init__(**kwargs)

    def on_back(self):
        self.parent.parent.transition.direction = 'right'
        self.parent.parent.current = 'display_database'

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

#---------------------Additionals ------------------------------------------------#

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#

class Info_Pop(GridLayout):
    info_1='''* Some entry might be wrong '''
    info_2='''* Use the camera to take debris's picture. '''
    info_3='''* Remember to select the type of charge. '''

    def __init__(self,**kwargs):
        super(Info_Pop,self).__init__(**kwargs)
        self.cols = 1
        #self.orientation = 'tb-lr'
        #self.size_hint_y=.3
        self.add_widget(Button(text = self.info_1))
        self.add_widget(Button(text = self.info_2))
        self.add_widget(Button(text = self.info_3))


class MainApp(App):
    def build(self):
        self.title = "Debris Collection Software"
        return Home()

if __name__=='__main__':
    MainApp().run()