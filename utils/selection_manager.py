#Create Object Selection Manager

class SelectionManager:

    def __init__(self):

        self.selected_box = None

    def select_box(
        self,
        box
    ):

        self.selected_box = box

    def clear_selection(
        self
    ):

        self.selected_box = None

    def get_selected_box(
        self
    ):

        return self.selected_box
