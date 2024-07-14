import os
import tkinter as tk
from tkinter import messagebox, filedialog
import shutil


def create_input_directory(variable_prefix):
    program_name = "hoi4variableprogram"
    input_dir = os.path.join(os.path.expanduser("~"), "Documents", program_name)

    # Create the template directory and subdirectories
    template_dir = os.path.join(input_dir, "template")
    os.makedirs(os.path.join(template_dir, "common", "on_actions"), exist_ok=True)
    os.makedirs(os.path.join(template_dir, "common", "scripted_effects"), exist_ok=True)
    os.makedirs(os.path.join(template_dir, "common", "scripted_localisation"), exist_ok=True)
    os.makedirs(os.path.join(template_dir, "localisation"), exist_ok=True)

    # Create the var_l_english.yml file
    yml_path = os.path.join(template_dir, "localisation", "var_l_english.yml")
    with open(yml_path, 'w', encoding='utf-8-sig') as file:
        file.write("l_english:\n")
        file.write(f"  {variable_prefix}loc_positive: \"§G+[{variable_prefix}overflow_value]§!\"\n")
        file.write(f"  {variable_prefix}loc_negative: \"§R-[{variable_prefix}overflow_value]§!\"\n")

    # Create the var_scripted_effects.txt file
    effects_path = os.path.join(template_dir, "common", "scripted_effects", "var_scripted_effects.txt")
    with open(effects_path, 'w', encoding='utf-8-sig') as file:
        file.write(f"{variable_prefix}add_to_total = {{\n")
        file.write(f"    add_to_variable = {{ {variable_prefix}source = THIS.{variable_prefix}add_to_total }}\n #you must specify {variable_prefix}source as a temp variable")
        file.write(f"\n")
        file.write(f"    if = {{ \n")
        file.write(f"        limit = {{ \n")
        file.write(f"            has_country_flag = {variable_prefix}overflow_check_is_negative \n")
        file.write(f"        }}\n")
        file.write(f"        multiply_variable = {{ THIS.{variable_prefix}add_to_total = -1 }} #forces digit to be positive\n")
        file.write(f"    }}\n")
        file.write(f"}}\n\n")
        file.write(f"{variable_prefix}initialize_overflow_value = {{\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 10 }}\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 100 }}\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 1000 }}\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 10000 }}\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 100000 }}\n")
        file.write(f"    add_to_temp_array = {{ divide_by_values = 1000000 }}\n")
        file.write(f"\n")
        file.write(f"    set_variable = {{ THIS.{variable_prefix}add_to_total_digit = 0 }}\n")
        file.write(f"\n")
        file.write(f"    for_each_loop = {{\n")
        file.write(f"        array = divide_by_values\n")
        file.write(f"        value = v\n")
        file.write(f"        if = {{\n")
        file.write(f"            limit = {{ THIS.{variable_prefix}add_to_total > v }}\n")
        file.write(f"            subtract_from_variable = {{ THIS.{variable_prefix}add_to_total = v }}\n")
        file.write(f"        }}\n")
        file.write(f"        add_to_variable = {{ THIS.{variable_prefix}add_to_total_digit = 1 }}\n")
        file.write(f"        add_to_variable = {{ THIS.{variable_prefix}overflow_check^{variable_prefix}add_to_total_digit = 1 }}\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

    scripted_loc_path = os.path.join(template_dir, "common", "scripted_localisation", "var_scripted_localisation.txt")
    with open(scripted_loc_path, 'w', encoding='utf-8-sig') as file:
        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_zero\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^0 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^0 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^0]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_ten\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^1 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^1 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^1]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_hundred\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^2 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^2 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^2]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_thousand\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^3 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^3 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^3]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_ten_thousand\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^4 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^4 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^4]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_hundred_thousand\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^5 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^5 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^5]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_million\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^6 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^6 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^6]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_ten_million\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^7 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^7 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^7]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_hundred_million\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^8 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^8 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^8]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_billion\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^9 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^9 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^9]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_ten_billion\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^10 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^10 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^10]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

        file.write(f"defined_text = {{\n")
        file.write(f"    name = {variable_prefix}digit_hundred_billion\n")
        file.write(f"    text = {{\n")
        file.write(f"        trigger = {{\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^11 > -1 }}\n")
        file.write(f"            check_variable = {{ THIS.{variable_prefix}overflow_check^11 < 10 }}\n")
        file.write(f"        }}\n")
        file.write(f"        localization_key = \"[?ROOT.{variable_prefix}overflow_check^11]\"\n")
        file.write(f"    }}\n")
        file.write(f"    text = {{\n")
        file.write(f"        localization_key = \"\"\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

    # Create the var_on_actions.txt file
    on_actions_path = os.path.join(template_dir, "common", "on_actions", "var_on_actions.txt")
    with open(on_actions_path, 'w', encoding='utf-8-sig') as file:
        file.write(f"on_actions = {{\n")
        file.write(f"    on_daily = {{\n")
        file.write(f"        effect = {{\n")
        file.write(f"            every_country = {{\n")
        file.write(f"                #limit = {{ is_ai = no }}\n")
        file.write(f"                if = {{\n")
        file.write(f"                    limit = {{ NOT = {{ has_country_flag = {variable_prefix}overflow_check_yes }} }}\n")

        for index, var in enumerate([
            "var", "var_ten", "var_hundred", "var_thousand",
            "var_ten_thousand", "var_hundred_thousand", "var_million",
            "var_ten_million", "var_hundred_million", "var_billion",
            "var_ten_billion", "var_hundred_billion", "var_trillion",
            "var_ten_trillion", "var_hundred_trillion", "var_imaginary_number"
        ]):
            file.write(f"                    add_to_array = {{\n")
            file.write(f"                        array = THIS.{variable_prefix}overflow_check\n")
            file.write(f"                        value = THIS.{variable_prefix}{var}\n")
            file.write(f"                        index = {index}\n")
            file.write(f"                    }}\n")

        file.write(f"                    set_variable = {{ THIS.{variable_prefix}overflow_check^0 = 999 }}\n")
        file.write(f"                    set_country_flag = {variable_prefix}overflow_check_yes\n")
        file.write(f"                    set_country_flag = {variable_prefix}overflow_check_is_positive\n")
        file.write(f"                    for_each_loop = {{\n")
        file.write(f"                        array = THIS.{variable_prefix}overflow_check\n")
        file.write(f"                        value = v\n")
        file.write(f"                        log = \"[?v] added to array.\"\n")
        file.write(f"                    }}\n")
        file.write(f"                }}\n")

        file.write(f"                for_loop_effect = {{\n")
        file.write(f"                    start = 0\n")
        file.write(f"                    end = 14\n")
        file.write(f"                    add = 1\n")
        file.write(f"                    value = v\n")
        file.write(f"                    round_variable = THIS.{variable_prefix}overflow_check^v\n")
        file.write(f"                    set_temp_variable = {{ next_digit = v }}\n")
        file.write(f"                    add_to_temp_variable = {{ next_digit = 1 }}\n")
        file.write(f"                    set_temp_variable = {{ this_digit = v }}\n")
        file.write(f"                    set_temp_variable = {{ last_digit = v }}\n")
        file.write(f"                    add_to_temp_variable = {{ last_digit = -1 }}\n")

        file.write(f"                    if = {{\n")
        file.write(f"                        limit = {{ check_variable = {{ THIS.{variable_prefix}overflow_check^this_digit > 9 }} }}\n")
        file.write(f"                        add_to_variable = {{ THIS.{variable_prefix}overflow_check^next_digit = 1 }}\n")
        file.write(f"                        add_to_variable = {{ THIS.{variable_prefix}overflow_check^this_digit = -10 }}\n")
        file.write(f"                        log = \"var_overflow_check: Digit overflow found!\"\n")
        file.write(f"                        log = \"var_overflow_check: New total is [?THIS.{variable_prefix}overflow_check^6][?THIS.{variable_prefix}overflow_check^5][?THIS.{variable_prefix}overflow_check^4][?THIS.{variable_prefix}overflow_check^3][?THIS.{variable_prefix}overflow_check^2][?THIS.{variable_prefix}overflow_check^1][?THIS.{variable_prefix}overflow_check^0]\"\n")
        file.write(f"                    }}\n")

        file.write(f"                    if = {{\n")
        file.write(f"                        limit = {{ check_variable = {{ THIS.{variable_prefix}overflow_check^this_digit < 0 }} }}\n")
        file.write(f"                        log = \"Found negative digit in THIS.{variable_prefix}overflow_check^[?this_digit!]\"\n")

        file.write(f"                        for_loop_effect = {{\n")
        file.write(f"                            start = 0\n")
        file.write(f"                            add = 1\n")
        file.write(f"                            end = 14\n")
        file.write(f"                            value = y\n")
        file.write(f"                            break = can_borrow_digit\n")
        file.write(f"                            set_temp_variable = {{ borrowable_digit = y }}\n")

        file.write(f"                            if = {{\n")
        file.write(f"                                limit = {{\n")
        file.write(f"                                    check_variable = {{ borrowable_digit > this_digit }}\n")
        file.write(f"                                    check_variable = {{ THIS.{variable_prefix}overflow_check^y > 0 }}\n")
        file.write(f"                                }}\n")

        file.write(f"                                set_country_flag = {variable_prefix}overflow_check_borrowable_digit\n")
        file.write(f"                                set_variable = {{ THIS.{variable_prefix}overflow_check_borrowed_digit = y }}\n")
        file.write(f"                                log = \"var_overflow_check: Found borrowable digit!\"\n")
        file.write(f"                                clear_variable = THIS.{variable_prefix}overflow_check_borrowed_digit\n")

        file.write(f"                                set_temp_variable = {{ borrowed_digit = y }}\n")
        file.write(f"                                set_temp_variable = {{ borrowed_digit_last_digit = borrowed_digit }}\n")
        file.write(f"                                add_to_temp_variable = {{ borrowed_digit_last_digit = -1 }}\n")

        file.write(f"                                add_to_variable = {{ THIS.{variable_prefix}overflow_check^borrowed_digit = -1 }}\n")
        file.write(f"                                add_to_variable = {{ THIS.{variable_prefix}overflow_check^borrowed_digit_last_digit = 10 }}\n")
        file.write(f"                                log = \"var_overflow_check: New total is [?THIS.{variable_prefix}overflow_check^6][?THIS.{variable_prefix}overflow_check^5][?THIS.{variable_prefix}overflow_check^4][?THIS.{variable_prefix}overflow_check^3][?THIS.{variable_prefix}overflow_check^2][?THIS.{variable_prefix}overflow_check^1][?THIS.{variable_prefix}overflow_check^0]\"\n")

        file.write(f"                                set_temp_variable = {{ can_borrow_digit = 1 }}\n")
        file.write(f"                            }}\n")

        file.write(f"                        }}\n")

        file.write(f"                        if = {{\n")
        file.write(f"                            limit = {{ NOT = {{ has_country_flag = {variable_prefix}overflow_check_borrowable_digit }} }}\n")
        file.write(f"                            if = {{\n")
        file.write(f"                                limit = {{ NOT = {{ check_variable = {{ this_digit = 0 }} }} }}\n")

        file.write(f"                                add_to_variable = {{ THIS.{variable_prefix}overflow_check^last_digit = -10 }}\n")
        file.write(f"                                add_to_variable = {{ THIS.{variable_prefix}overflow_check^this_digit = 1 }}\n")
        file.write(f"                                log = \"var_overflow_check: No digit to borrow from. You're getting poorer. Whoops.\"\n")
        file.write(f"                                log = \"var_overflow_check: New total is [?THIS.{variable_prefix}overflow_check^6][?THIS.{variable_prefix}overflow_check^5][?THIS.{variable_prefix}overflow_check^4][?THIS.{variable_prefix}overflow_check^3][?THIS.{variable_prefix}overflow_check^2][?THIS.{variable_prefix}overflow_check^1][?THIS.{variable_prefix}overflow_check^0]\"\n")

        file.write(f"                            }}\n")

        file.write(f"                            if = {{\n")
        file.write(f"                                limit = {{ check_variable = {{ this_digit = 0 }}\n")
        file.write(f"                                check_variable = {{ THIS.{variable_prefix}overflow_check^this_digit < 0 }} }}\n")

        file.write(f"                                if = {{\n")
        file.write(f"                                    limit = {{ has_country_flag = {variable_prefix}overflow_check_is_positive }}\n")

        file.write(f"                                    set_country_flag = {variable_prefix}overflow_check_is_negative\n")
        file.write(f"                                    clr_country_flag = {variable_prefix}overflow_check_is_positive\n")

        file.write(f"                                    multiply_variable = {{ THIS.{variable_prefix}overflow_check^0 = -1 }}\n")
        file.write(f"                                    log = \"var_overflow_check has gone negative!\"\n")
        file.write(f"                                }}\n")

        file.write(f"                                else_if = {{\n")
        file.write(f"                                    set_country_flag = {variable_prefix}overflow_check_is_positive\n")
        file.write( f"                                    clr_country_flag = {variable_prefix}overflow_check_is_negative\n")

        file.write(f"                                    multiply_variable = {{ THIS.{variable_prefix}overflow_check^0 = -1 }}\n")
        file.write(f"                                    log = \"var_overflow_check has gone positive!\"\n")
        file.write(f"                                }}\n")

        file.write(f"                            }}\n")

        file.write(f"                        }}\n")

        file.write(f"                    }}\n")

        file.write(f"                }}\n")
        file.write(f"            }}\n")
        file.write(f"        }}\n")
        file.write(f"    }}\n")
        file.write(f"}}\n")

    return input_dir


def duplicate_and_modify_files(input_dir, output_dir, variable_prefix):
    os.makedirs(output_dir, exist_ok=True)

    # Append underscore to variable prefix
    variable_prefix_with_underscore = f"{variable_prefix}_"

    for root, _, files in os.walk(input_dir):
        for filename in files:
            input_path = os.path.join(root, filename)

            with open(input_path, 'r', encoding='utf-8-sig') as file:
                content = file.read()

            modified_content = content.replace(f"{variable_prefix}", variable_prefix_with_underscore)

            # Rename the file
            new_filename = filename.replace("var_", f"{variable_prefix}_")
            output_subdir = os.path.join(output_dir, os.path.relpath(root, input_dir))
            os.makedirs(output_subdir, exist_ok=True)

            output_path = os.path.join(output_subdir, new_filename)

            with open(output_path, 'w', encoding='utf-8-sig') as file:
                file.write(modified_content)

            print(f"Duplicated and modified {filename} -> {output_path}")


def run_program(variable_prefix):
    input_directory = create_input_directory(variable_prefix)

    # Create output directory named "output" containing the variable prefix folder
    output_directory = os.path.join(input_directory, "output", variable_prefix)

    # Duplicate and modify files
    duplicate_and_modify_files(os.path.join(input_directory, "template"), output_directory, variable_prefix)

    messagebox.showinfo("Success", f"Files created in: {output_directory}")

    shutil.rmtree(os.path.join(input_directory, "template"))

    messagebox.showinfo("Success", f"Files created in: {output_directory}")

def on_submit():
    variable_prefix = entry_prefix.get()
    if variable_prefix.strip():
        run_program(variable_prefix)
    else:
        messagebox.showwarning("Input Error", "Please enter a valid variable prefix.")


# Create a simple GUI
root = tk.Tk()
root.title("HOI4 Variable Program Creator")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

label_prefix = tk.Label(frame, text="Enter Variable Name:")
label_prefix.pack()

entry_prefix = tk.Entry(frame)
entry_prefix.pack(pady=5)

submit_button = tk.Button(frame, text="Create Files", command=on_submit)
submit_button.pack(pady=10)

root.mainloop()