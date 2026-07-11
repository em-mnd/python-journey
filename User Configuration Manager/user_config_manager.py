test_settings = {
    'theme': 'light',
    'notifications': 'enabled'
}


#Functions

def add_setting(test_settings, setting):
    key, value = setting 
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    elif key not in test_settings:
        test_settings[key] = value
        return(f"Setting '{key}' added with value '{value}' successfully.")

def update_setting(test_settings, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key] = value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    elif key not in test_settings:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        return(f"Setting '{key}' deleted successfully!")
    elif key not in test_settings:
        return(f"Setting not found!")

def view_settings(test_settings):
    if test_settings:
        result = "Current User Settings:"
        for key, value in test_settings.items():
            result += f"\n{key.capitalize()}: {value}"
        return result+'\n'
    else:
        return("No settings available.")

#Using the functions

add_setting({'theme': 'light'}, ('THEME', 'dark'))
add_setting({'theme': 'light'}, ('volume', 'high'))
update_setting({'theme': 'light'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))
delete_setting({'theme': 'light'}, 'theme')
delete_setting(test_settings, 'theme')
view_settings(test_settings)