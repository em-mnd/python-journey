test_settings = {
    'theme': 'light',
    'volume': 'high',
    'notifications': 'enabled'
}


#Functions

def add_setting(test_settings, key, value):
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        print(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    if key not in test_settings:
        test_settings[key] = value
        print(f"Setting '{key}' added with value '{value}' successfully.")

def update_setting(test_settings, key, value):
    key = key.lower()
    value = value.lower()
    if key in test_settings:
        test_settings[key] = value
        print(f"Setting '{key}' updated to '{value}' successfully!")
    if key not in test_settings:
        print(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")

def delete_setting(test_settings, key):
    key = key.lower()
    if key in test_settings:
        del test_settings[key]
        print(f"Setting '{key}' deleted successfully!")
    if key not in test_settings:
        print(f"Setting not found")

def view_settings(test_settings):
    if test_settings:
        print("Current User Settings:")
        for key, value in test_settings.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("No settings found.")