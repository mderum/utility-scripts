import xml.etree.ElementTree as ET

xml_file_path = r'C:\Program Files\Mantra\RDService\MFS100\Config.xml'

def toggle_env(xml_path):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Find the Settings element and toggle the env attribute
    current_env = root.get('env')
    print(current_env)

    # Toggle between "PP" and "P"
    new_env = 'P' if current_env == 'PP' else 'PP'
    print(new_env)
    root.set('env',new_env)

    # Save the modified XML file
    tree.write(xml_file_path)

if __name__ == "__main__":
    toggle_env(xml_file_path)
