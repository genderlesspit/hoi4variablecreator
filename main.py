import os
import tkinter as tk
from tkinter import messagebox

def create_folders_and_write(variable):
    # Define folder structure
    base_folder = "common"
    on_actions_folder = os.path.join(base_folder, "on_actions")
    scripted_effects_folder = os.path.join(base_folder, "scripted_effects")

    # Create the folders
    os.makedirs(on_actions_folder, exist_ok=True)
    os.makedirs(scripted_effects_folder, exist_ok=True)

    # Write to var_on_actions.txt in on_actions
    with open(os.path.join(on_actions_folder, f"var_{variable}_on_actions.txt"), 'w') as f:
        f.write(f"# On Actions: {variable}\n")

    # Code blocks with user-defined variable
    code_blocks = f"""{variable}_add_to_total = {{

    add_to_variable = {{ THIS.{variable} = THIS.{variable}_add_to_total }}

    if = {{ 
        limit = {{ 
            has_country_flag = {variable}_overflow_check_is_negative 
        }}
        multiply_variable = {{ THIS.{variable}_add_to_total = -1 }} #forces digit to be positive
    }}
}}

{variable}_initialize_overflow_value = {{

    add_to_temp_array = {{ divide_by_values = 10 }}
    add_to_temp_array = {{ divide_by_values = 100 }}
    add_to_temp_array = {{ divide_by_values = 1000 }}
    add_to_temp_array = {{ divide_by_values = 10000 }}
    add_to_temp_array = {{ divide_by_values = 100000 }}
    add_to_temp_array = {{ divide_by_values = 1000000 }}

    set_variable = {{ THIS.{variable}_add_to_total_digit = 0 }}

    for_each_loop = {{
        array = divide_by_values
        value = v
        if = {{
            limit = {{ THIS.{variable}_add_to_total > v }}
            subtract_from_var = {{ THIS.{variable}_add_to_total = v }}
        }}
        add_to_variable = {{ THIS.{variable}_add_to_total_digit = 1 }}
        add_to_variable = {{ THIS.{variable}_overflow_check^{variable}_add_to_total_digit = 1 }}
    }}
}}"""

    with open(os.path.join(scripted_effects_folder, f"var_{variable}_scripted_effects.txt"), 'w') as f:
        f.write(f"# Scripted Effects: {variable}\n\n")
        f.write(code_blocks)

    # Create the on_actions code
    on_actions_code = f"""on_actions = {{
    on_daily = {{
        effect = {{
            every_country = {{
                limit = {{ is_ai = no }} 
                if = {{
                    limit = {{ NOT = {{ has_country_flag = {variable}_overflow_check_yes }} }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.var
                        index = 0
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_ten
                        index = 1
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_hundred
                        index = 2
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_thousand
                        index = 3
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_ten_thousand
                        index = 4
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_hundred_thousand
                        index = 5
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_million
                        index = 6
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_ten_million
                        index = 7
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_hundred_million
                        index = 8
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_billion
                        index = 9
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_ten_billion
                        index = 10
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_hundred_billion
                        index = 11
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_trillion
                        index = 12
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_ten_trillion
                        index = 13
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_hundred_trillion
                        index = 14
                    }}
                    add_to_array = {{ 
                        array = THIS.{variable}_overflow_check
                        value = THIS.{variable}_imaginary_number
                        index = 15
                    }}
                    set_variable = {{ THIS.{variable}_overflow_check^0 = 999 }}
                    set_country_flag = {variable}_overflow_check_yes
                    set_country_flag = {variable}_overflow_check_is_positive
                    for_each_loop = {{
                        array = THIS.{variable}_overflow_check
                        value = v
                        log = "[?v] added to array."
                    }}
                }}    

                for_loop_effect = {{
                    start = 0
                    end = 14
                    add = 1
                    value = v

                    round_variable = THIS.{variable}_overflow_check^v

                    set_temp_variable = {{ next_digit = v }}
                    add_to_temp_variable = {{ next_digit = 1 }}
                    set_temp_variable = {{ this_digit = v }}
                    set_temp_variable = {{ last_digit = v }}
                    add_to_temp_variable = {{ last_digit = -1 }}

                    if = {{ 
                        limit = {{ check_variable = {{ THIS.{variable}_overflow_check^this_digit > 9 }} }} 
                        add_to_variable = {{ THIS.{variable}_overflow_check^next_digit = 1 }} 
                        add_to_variable = {{ THIS.{variable}_overflow_check^this_digit = -10 }} 
                        log = "{variable}_overflow_check: Digit overflow found!"
                        log = "{variable}_overflow_check: New total is [?THIS.{variable}_overflow_check^6][?THIS.{variable}_overflow_check^5][?THIS.{variable}_overflow_check^4][?THIS.{variable}_overflow_check^3][?THIS.{variable}_overflow_check^2][?THIS.{variable}_overflow_check^1][?THIS.{variable}_overflow_check^0]"
                    }}
                    if = {{
                        limit = {{ 
                            check_variable = {{ THIS.{variable}_overflow_check^this_digit < 0 }} 
                        }}
                        log = "Found negative digit in THIS.{variable}_overflow_check^[?this_digit!]"
                        for_loop_effect = {{
                            start = 0
                            add = 1 
                            end = 14  
                            value = y
                            break = can_borrow_digit

                            set_temp_variable = {{ borrowable_digit = y }}

                            if = {{
                                limit = {{ 
                                    check_variable = {{ borrowable_digit > this_digit }}
                                    check_variable = {{ THIS.{variable}_overflow_check^y > 0 }}
                                }}

                                set_country_flag = {variable}_overflow_check_borrowable_digit

                                set_variable = {{ THIS.{variable}_overflow_check_borrowed_digit = y }}
                                log = "{variable}_overflow_check: Found borrowable digit!"
                                clear_variable = THIS.{variable}_overflow_check_borrowed_digit

                                set_temp_variable = {{ borrowed_digit = y }}
                                set_temp_variable = {{ borrowed_digit_last_digit = borrowed_digit }}
                                add_to_temp_variable = {{ borrowed_digit_last_digit = -1 }}

                                add_to_variable = {{ THIS.{variable}_overflow_check^borrowed_digit = -1 }} 
                                add_to_variable = {{ THIS.{variable}_overflow_check^borrowed_digit_last_digit = 10 }} 
                                log = "{variable}_overflow_check: New total is [?THIS.{variable}_overflow_check^6][?THIS.{variable}_overflow_check^5][?THIS.{variable}_overflow_check^4][?THIS.{variable}_overflow_check^3][?THIS.{variable}_overflow_check^2][?THIS.{variable}_overflow_check^1][?THIS.{variable}_overflow_check^0]"

                                set_temp_variable = {{ can_borrow_digit = 1 }} 
                            }}
                        }}
                        if = {{ 
                            limit = {{ NOT = {{ has_country_flag = {variable}_overflow_check_borrowable_digit }} }}
                            if = {{
                                limit = {{ 
                                    NOT = {{ check_variable = {{ this_digit = 0 }} }}
                                }}

                                add_to_variable = {{ THIS.{variable}_overflow_check^last_digit = -10 }} 
                                add_to_variable = {{ THIS.{variable}_overflow_check^this_digit = 1 }} 
                                log = "{variable}_overflow_check: No digit to borrow from. You're getting poorer. Whoops."
                                log = "{variable}_overflow_check: New total is [?THIS.{variable}_overflow_check^6][?THIS.{variable}_overflow_check^5][?THIS.{variable}_overflow_check^4][?THIS.{variable}_overflow_check^3][?THIS.{variable}_overflow_check^2][?THIS.{variable}_overflow_check^1][?THIS.{variable}_overflow_check^0]"
                            }}
                            if = {{
                                limit = {{ 
                                    check_variable = {{ this_digit = 0 }}
                                    check_variable = {{ THIS.{variable}_overflow_check^this_digit < 0 }}
                                }}
                                if = {{ 
                                    limit = {{ has_country_flag = {variable}_overflow_check_is_positive }}

                                    set_country_flag = {variable}_overflow_check_is_negative
                                    clr_country_flag = {variable}_overflow_check_is_positive

                                    multiply_variable = {{ THIS.{variable}_overflow_check^0 = -1 }}
                                    log = "{variable}_overflow_check has gone negative!"
                                }}
                                else_if = {{
                                    set_country_flag = {variable}_overflow_check_is_positive
                                    clr_country_flag = {variable}_overflow_check_is_negative

                                    multiply_variable = {{ THIS.{variable}_overflow_check^0 = -1 }}
                                    log = "{variable}_overflow_check has gone positive!"
                                }}
                            }}
                        }}
                        clr_country_flag = {variable}_overflow_check_borrowable_digit
                    }}
                }}
            }}
        }}
    }}
}}"""

    # Write the on_actions code block to the appropriate file
    with open(os.path.join(on_actions_folder, f"var_{variable}_on_actions.txt"), 'a') as f:
        f.write(on_actions_code)

def generate_files():
    user_variable = entry.get()
    if user_variable:
        create_folders_and_write(user_variable)
        messagebox.showinfo("Success", "Folders and files created successfully.")
    else:
        messagebox.showwarning("Input Error", "Please enter a variable.")

from tkinter import filedialog

def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory(initialdir=r"C:\Users\{}\Documents\Paradox Interactive\Hearts of Iron IV\mod".format(os.getlogin()), title="Select Output Folder")
    folder_label.config(text=f"Selected Folder: {folder_path}")

# Set up the GUI
root = tk.Tk()
root.title("Variable File Generator")
root.geometry("500x250")

# Create and place a label and entry
label = tk.Label(root, text="Enter a variable:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create and place the select folder button
select_folder_button = tk.Button(root, text="Select Mod Folder", command=select_folder)
select_folder_button.pack(pady=5)

folder_label = tk.Label(root, text="No folder selected")
folder_label.pack(pady=5)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Files", command=generate_files)
generate_button.pack(pady=20)

# Initialize folder_path variable
folder_path = ""

# Run the application
root.mainloop()