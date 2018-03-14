'''
Name : Vincent Ha
Student ID : 14788488
'''

import othello
import othello_point
import othello_spots
import tkinter


DEFAULT_FONT = ('Helvetica', 14)

class ErrorScreen:
    '''
    The ErrorScreen class has the simple job of popping up an error screen
    whenever the user inputs invalid data.
    '''
    def __init__(self : 'ErrorScreen') -> 'ErrorScreen':
        '''
        The constructor for the ErrorScreen class. This constructor creates
        a tkinter toplevel object with a simple message and a button that
        allows users to get out of the screen.
        '''
        self.error_window = tkinter.Toplevel()
        
        welcome_label = tkinter.Label(
            master = self.error_window,
            text = 'Invalid Input. Please Try Again.',
            font = DEFAULT_FONT)

        welcome_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 150, pady = 10,
            sticky = tkinter.S )

        button_frame = tkinter.Frame(master = self.error_window, width = 10)

        button_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N)

        ok_error_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_cancel_error_button)

        ok_error_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.error_window.bind('<Return>', lambda event:
                               self._on_cancel_error_button())

        self.error_window.rowconfigure(0, weight = 1)
        self.error_window.rowconfigure(1, weight = 1)
        self.error_window.columnconfigure(0, weight = 1)

    def _on_cancel_error_button(self: 'BoardDialog') -> None:
        '''
        This member function is the command connected to the ok button. It
        simpley exits out of the window.
        '''
        self.error_window.destroy()

    def show (self : 'BoardDialog') -> None:
        '''
        This member function grabs the focus from the main window and makes
        this screen appear.
        '''
        self.error_window.grab_set()
        self.error_window.wait_window()
        
class BoardDialog:
    '''
    The BoardDialog class is a screen used to get information about the Othello
    game being played. It checks for valid input internally. If the input is
    invalid, the errorscreen is shown and the entries in the entry boxes
    previously are cleared out. If valid, the screen will close and the class
    will pass its info in order to create the gameboard.
    '''
    def __init__(self : 'BoardDialog') -> 'BoardDialog':
        '''
        The constructor for the BoardDialog Class. It initiates values that are
        need to create the game of Othello and sets up the TopLevel object to
        ask the user for this information. The user is given the option to exit
        out of the program as well.
        '''
        self.rows = 0
        self.columns = 0
        self.first_turn_player = 'N/A'
        self.win_condition = 'N/A'
        
        self.dialog_window = tkinter.Toplevel()

        welcome_label = tkinter.Label(
            master = self.dialog_window, text = 'Welcome to Othello!',
            font = DEFAULT_FONT)

        welcome_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 150, pady = 10,
            sticky = tkinter.W )

        self.rows_and_columns() # creates prompt for # of rows and columns
        self.string_input()     # creates prompt for first turn player and
                                # win condition
        self.button_setup()     # creates button to exit or continue.

        self.dialog_window.bind('<Return>', lambda event: self._on_ok_button())

    def rows_and_columns(self : 'BoardDialog') -> None:
        '''
        This member function creates the prompt that asks the user for the
        number of rows and columns that will be on the Othello gameboard.
        '''
        row_label = tkinter.Label(
            master = self.dialog_window, text = 'Number of Rows:',
            font = DEFAULT_FONT)
        
        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self.row_label_entry = tkinter.Entry(
            master = self.dialog_window, width = 20, font = DEFAULT_FONT)

        self.row_label_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        column_label = tkinter.Label(
            master = self.dialog_window, text = 'Number of Columns:',
            font = DEFAULT_FONT)

        column_label.grid(
            row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self.column_label_entry = tkinter.Entry(
            master = self.dialog_window, width = 20, font = DEFAULT_FONT)

        self.column_label_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

    def string_input(self : 'BoardDialog') -> None:
        '''
        Like the function above, this member function creates the prompt for the
        first turn player and how the game is won.
        '''
        first_turn_player_label = tkinter.Label(
            master = self.dialog_window,
            text = 'First Turn Player (Enter Black or White):',
            font = DEFAULT_FONT)

        first_turn_player_label.grid(
            row = 3, column = 0, padx = 10, pady = 0, sticky = tkinter.W)

        self.first_turn_player_label_entry = tkinter.Entry(
            master = self.dialog_window, width = 20, font = DEFAULT_FONT)

        self.first_turn_player_label_entry.grid(
            row = 3, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        win_condition_label = tkinter.Label(
            master = self.dialog_window, text = 'Win Condition (Enter > or < ):',
            font = DEFAULT_FONT)

        win_condition_label.grid(
            row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self.win_condition_label_entry = tkinter.Entry(
            master = self.dialog_window, width = 20, font = DEFAULT_FONT)

        self.win_condition_label_entry.grid(
            row = 4, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

    def button_setup(self : 'BoardDialog') -> None:
        '''
        This member function creates the buttons to either to try to continue
        with the program and to exit the program entirely.
        '''
        button_frame = tkinter.Frame(
            master = self.dialog_window, width = 10)

        button_frame.grid(
            row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.S + tkinter.E)

        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'QUIT', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)
        
    def clear_entry(self : 'BoardDialog') -> None:
        '''
        This member function is used to delete the entries that the user has
        placed inside the entry boxes. This function is called when the input
        the user inputted is invalid.
        '''
        self.row_label_entry.delete(0, 'end')
        self.column_label_entry.delete(0, 'end')
        self.first_turn_player_label_entry.delete(0, 'end')
        self.win_condition_label_entry.delete(0, 'end')

        self.rows = 0
        self.columns = 0
        self.first_turn_player = 'N/A'
        self.win_condition = 'N/A'
        
    def show (self : 'BoardDialog') -> None:
        '''
        This member function is used to open and focus on this window from the
        main window.
        '''
        self.dialog_window.grab_set()
        self.dialog_window.wait_window()
        
    def _on_ok_button (self : 'BoardDialog') -> None:
        '''
        This member functionis initiated when the user clicks the ok button or
        presses the enter key. It first checks for whether the input is valid
        or not. If it is valid, it then holds the information and closes the
        window to return to the main window. Otherwise, the error screen is
        shown.
        '''
        try:
            self.rows = int(self.row_label_entry.get())
            self.columns = int(self.column_label_entry.get())
            self.first_turn_player =\
                                   self.first_turn_player_label_entry.get().\
                                   split()[0].upper()
            self.win_condition = self.win_condition_label_entry.get().split()[0]

            if (not self.first_turn_player == 'BLACK'
                and not self.first_turn_player == 'WHITE')\
                or (not self.win_condition == '>'
                    and not self.win_condition == '<'):

                self.error()

            if (self.rows >= 4 and self.rows <= 16 and self.columns >= 4
                and self.columns <= 16 and self.rows % 2 ==0 and
                self.columns % 2 == 0):
                
                self.dialog_window.destroy()
                
            else:
                self.error()
        
        except ValueError:
            self.error()
            
        except IndexError:
            self.error()
        
    def _on_cancel_button(self : 'BoardDialog') -> None:
        '''
        This member function is bind to the quit button. It simply exits out of
        window screen without entering any information beforehand.
        '''
        self.dialog_window.destroy()

    def quit_othello(self : 'BoardDialog') -> bool:
        '''
        This member function checks whether the class member variables are
        still set to their initial values. If they are, this implies that
        the user wants to quit out of the program.
        '''
        return self.rows == 0 and self.columns == 0 and \
               self.first_turn_player == 'N/A' and self.win_condition == 'N/A'

    def get_info(self : 'BoardDialog') -> (int, int, str, str):
        '''
        This member function returns the information that this class gathered
        from the user through input on the screen.
        '''
        return (self.rows, self.columns, self.first_turn_player,
                self.win_condition)

    def error(self : 'BoardDialog') -> None:
        '''
        This member function facilitates the steps that are necessary when the
        user placed invalid input. It pops up the error window and clear the
        entries in the entry boxes.
        '''
        error_screen = ErrorScreen()
        error_screen.show()
        self.clear_entry()
    
class OthelloBoard:
    '''
    The OthelloBoard class handles the main bulk of the Othello GUI. It opens
    the main window that all the other screens are rooted from. It also
    displays the gameboard and handles the user interaction with the
    gameplay.
    '''
    def __init__(self : 'OthelloBoard') -> 'OthelloBoard':
        '''
        The constructor for the OthelloBoard class primarily sets up the screen
        for the Othello gameboard.
        '''
        self.color = {
            'B' : 'Black',
            'W' : 'White'
            }

        self.not_destroyed = True
        self.home_screen()

    def home_screen(self : 'OthelloBoard') -> None:
        '''
        This member function creates the main screen to the program. It simply
        has a title and two buttons. The start game button brings up the dialog
        window to get the user's information about the Othello gameboard while
        the quit game button exits out of the window.
        '''
        self.root_window = tkinter.Tk()
        self.root_window.configure(bg = '#00ad68')
        
        self.welcome_label = tkinter.Label(
            master = self.root_window,
            text = 'Othello',
            font = ('Helvetica', 30),
            bg = '#00ad68')

        self.welcome_label.grid(row = 0, column = 0, sticky = tkinter.S)

        self.button_frame = tkinter.Frame(
            master = self.root_window, width = 10, bg = '#00ad68')

        self.button_frame.grid(
            row = 1, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N )
        
        self.start_game_button = tkinter.Button(
            master = self.button_frame,
            text = 'START',
            font = DEFAULT_FONT,
            bg = '#00ad68',
            command = self.get_specs)

        self.start_game_button.grid(row = 0, column = 0)

        self.quit_game_button = tkinter.Button(
            master = self.button_frame,
            text = 'QUIT',
            font = DEFAULT_FONT,
            bg = '#00ad68',
            command = lambda : self.destroy())

        self.quit_game_button.grid(row = 1, column = 0)
            
        self.root_window.rowconfigure(0, weight = 1)     #Allows the screen and
        self.root_window.rowconfigure(1, weight = 1)     #buttons to change when
        self.root_window.columnconfigure(0, weight = 1)  #window is configured.

    def get_specs(self : 'OthelloBoard') -> None:
        '''
        This member function obtains the information from the dialog window and
        goes to the setup phase of the program.
        '''
        self.welcome_label.destroy()
        self.start_game_button.destroy()
        self.quit_game_button.destroy()
        self.button_frame.destroy()
        self.setup_window()

        self.dialog = BoardDialog()
        self.dialog.show()

        if(self.dialog.quit_othello()):
            self.destroy()

        if (self.not_destroyed):
            self.game_info = self.dialog.get_info()
            self.turn_player = self.game_info[2]
            
            self.positions = othello_spots.CounterPositions(
                self.game_info[0], self.game_info[1], self.game_info[2],
                self.game_info[3])

            self.draw_grid()
            
            self.root_window.rowconfigure(0, weight = 1)
            self.root_window.rowconfigure(1, weight = 1)
            self.root_window.rowconfigure(2, weight = 1)
            self.root_window.columnconfigure(0, weight = 1)
            
            self.canvas.bind('<Configure>',
                             lambda event: self.draw_all_circles())

            self.setup_board()
        
    def setup_window(self : 'OthelloBoard') -> None:
        '''
        The setup_window function is called when the user successfully entered
        information about the gameboard. This function sets up the gameboard
        on the screen with the specifications given by the user. This gameboard
        is used to setup initial counters on the board.It also creates a simple
        heading and instructions on how to place and remove counters.
        '''
        self.root_window.configure(bg = 'gray')
        self.heading = tkinter.StringVar()
        self.heading.set('Welcome to Othello!')
        
        self.title = tkinter.Label(
            master = self.root_window,
            textvariable = self.heading,
            font = ('Helvetica', 20),
            bg = 'gray')

        self.title.grid(row = 0, column = 0, sticky = tkinter.S)
            
        self.canvas = tkinter.Canvas(
            master = self.root_window, width = 600, height = 600,
            highlightbackground = 'black', bg = '#00ad68')
    
        self.canvas.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

    def destroy(self : 'OthelloBoard') -> None:
        '''
        This member function is called when the user presses the quit button.
        It simply stops further processing and exits out of the program.
        '''
        self.root_window.destroy()
        self.not_destroyed = False
    
    def start(self : 'OthelloBoard') -> None:
        '''
        This member function simply starts the program by opening up the home
        screen on a window.
        '''
        self.root_window.mainloop()
        
    def draw_grid(self : 'OthelloBoard') -> None:
        '''
        This member function draws the gridlines on the Othello board. It
        deletes everything on the board before redrawing the necessary
        equidistant lines.
        '''
        self.canvas.delete(tkinter.ALL)

        width_canvas = self.canvas.winfo_width()
        height_canvas = self.canvas.winfo_height()

        for column_index in range(self.game_info[1]):
            self.canvas.create_line(
                0, ((column_index/(self.game_info[1])) * height_canvas),
                width_canvas,
                ((column_index/(self.game_info[1])) * height_canvas),
                width = 2.5)

        for row_index in range(self.game_info[0]):
                self.canvas.create_line(
                ((row_index/(self.game_info[0])) * width_canvas), 0,
                ((row_index/(self.game_info[0])) * width_canvas),
                height_canvas, width = 2.5)

    def draw_all_circles(self : 'OthelloBoard') -> None:
        '''
        This member function draws the counters that were present on the board.
        It calls the drawgrid function to redraw the Othello board and draws
        counters whose size is a fraction of the size of the box it is in.
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.draw_grid()
        
        for circle in self.positions.counter_locations:
            radius = circle[1].get_radius()
            center = circle[1].get_center()
            point = center.to_pixel(width, height)
            
            self.canvas.create_oval(point[0] - ((3 * radius * width)/4),
                                    point[1] - ((3 * radius * height)/4),
                                    point[0] + ((3 * radius * width)/4),
                                    point[1] + ((3 * radius * height)/4),
                                    fill = self.color[circle[0]])

        
    def draw_initial_counters(self : 'OthelloBoard', player : str,
                      event : tkinter.Event) -> None:
        '''
        This member function handles inputting counters during the setup phase.
        It gives the information into positions and then prints the counters
        on the board
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        self.positions.setup_placement(event.x, event.y, width, height, player)
        self.draw_all_circles()
        

    def delete_initial_counters(self : 'OthelloBoard', player : str,
                                event : tkinter.Event) -> None:
        '''
        This member function handles deleting counters during the setup phase.
        It gives the information into positions and then prints the counters
        left on the board.
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        self.positions.setup_delete(event.x, event.y, width, height, player)
        self.draw_all_circles()

    def setup(self : 'OthelloBoard', player : str) -> None:
        '''
        This member function sets up the screen in which the user inputs the
        initial gameboard for the Othello game. It consists of the
        gameboard, instructions
        '''
        command_dict = {
            0 : lambda : self.setup('W'),
            1 : lambda : self.finish_setup()
            }

        self.confirmation_button.configure(command = command_dict[self.index])

        self.index += 1
        
        self.heading.set('{0} Counters Setup'.format(self.color[player]))
        self.canvas.bind('<Button-1>',
                         lambda event: self.draw_initial_counters(player, event))
        self.canvas.bind('<Double-Button-1>',
                         lambda event: self.delete_initial_counters(player,
                                                                    event))

        self.instruction_text = tkinter.StringVar()
        self.instruction_text.set(
            'Please Left Click to Place Counters and Double Left Click to '+
            'Remove Them')

        if(player == 'B'):
            self.instructions_label = tkinter.Label(
                master = self.root_window,
                textvariable = self.instruction_text,
                font = DEFAULT_FONT, bg = 'gray')

            self.instructions_label.grid(row = 3, column = 0, sticky = tkinter.S)


    def finish_setup(self : 'OthelloBoard') -> None:
        '''
        This member function finishes up the setup process and begins the
        acutal gameplay. It removes a button used to progress through the
        program and adds a heading to indicate the current player's turn.
        It also changes the instructions to indicate how to place counters.
        '''
        self.positions.finish_setup()
        self.confirmation_button.destroy()
        
        self.instruction_text.set(
            'Please Left Click on the Place You Want to Place Your Counter')

        self.instructions_label.configure(textvariable = self.instruction_text)

        self.heading.set('{0} Turn'.format((
            self.turn_player[0] + self.turn_player[1:].lower())))
                         
        self.play_game()

        
    def setup_board(self : 'OthelloBoard') -> None:
        '''
        This member function handles the progression of the setup phase. A
        button is created here to help in this progression.
        '''
        self.index = 0
        self.confirmation_button = tkinter.Button(
            master = self.root_window, text = 'OK', font = DEFAULT_FONT,
            bg = 'gray', command = lambda : self.setup('W'))
            
        self.confirmation_button.grid(
            row = 3, column = 0, sticky = tkinter.E)

        self.setup('B')
        

    def draw_counters(self : 'OthelloBoard', event : tkinter.Event) -> None:
        '''
        This member function places counters from a player during gameplay.
        It also updates the score when a placement is made.
        '''
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        made_placement = self.positions.place_counter(
            event.x, event.y, width, height, self.turn_player[0])

        if (made_placement):
            if (self.positions.any_valid_moves(
                self.next_player_dict[self.turn_player])):
                self.turn_player = self.next_player_dict[self.turn_player]

        self.draw_all_circles()
        self.score.set('Black : {0}   White : {1}'.format(
            str(self.positions.count('B')), str(self.positions.count('W'))))
        
        if not(self.positions.game_over()):
            self.heading.set('{0} Turn'.format((
                self.turn_player[0] + self.turn_player[1:].lower())))
        else:
            self.finish_game()

        
    def play_game(self : 'OthelloBoard') -> None:
        '''
        This member function handles the program when the users are playing
        Othello. It creates a score heading to indicate the current state of
        the game. It also binds the left mouse click to another function and
        unbinds the double mouse click.
        '''
        self.next_player_dict = {
            'BLACK' : 'WHITE',
            'WHITE' : 'BLACK'
            }

        self.score = tkinter.StringVar()
        self.score.set('Black : {0}   White : {1}'.format(
            str(self.positions.count('B')), str(self.positions.count('W'))))
        
        self.score_label = tkinter.Label(
            master = self.root_window,
            textvariable = self.score,
            font = ('Helvetica', 20),
            bg = 'gray')

        self.score_label.grid(row = 1, column = 0, sticky = tkinter.S)
        
        if not (self.positions.any_valid_moves(self.turn_player)):
            self.turn_player = self.next_player_dict[self.turn_player]
            self.heading.set('{0} Turn'.format((
                self.turn_player[0] + self.turn_player[1:].lower())))
            
        if (self.positions.game_over()):
            self.finish_game()
            
        self.canvas.bind('<Button-1>', self.draw_counters)
        self.canvas.unbind('<Double-Button-1>')

    def finish_game(self : 'OthelloBoard') -> None:
        '''
        This member function displays the final screen when the game is over.
        It displays who won the game and gets rid of the instructions on the
        bottom of the screen.
        '''
        winner = self.positions.calculate_winner()
        
        if (winner == 'NONE'):
            self.heading.set('It\'s a Tie!')
        else:
            self.heading.set('{0} is the Winner!'.format(self.color[winner]))

        self.instructions_label.destroy()

'''
Main Function
'''
if __name__ == '__main__':
    OthelloBoard().start()


        
