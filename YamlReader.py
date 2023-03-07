import yaml

def read(yamlFilePath):
    try:
        yamlFile = open(yamlFilePath, "r", encoding = 'UTF-8')
        return yaml.load(yamlFile, Loader=yaml.Loader)
    except Exception as e:
        return None
