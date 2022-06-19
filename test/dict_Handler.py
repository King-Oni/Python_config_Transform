import yaml,json,configparser

class Dict_Handler():
    def __init__(self,file:str):
        self.__dict = {}
        self.__file = file
        self.__config = configparser.ConfigParser()
        self.__Check()

    def __Check(self):
        file = self.__file
        if (file.lower().endswith(('.yml','yaml'))):
            self.__read_yml()
        if (file.lower().endswith('.ini')):
            self.__read_ini()
        if (file.lower().endswith('.json')):
            self.__read_json()
        self.__deType()

    def __deType(self):
        types = [".yml",".yaml",".json",".ini"]
        de_Typed=list(self.__file.replace(fType,'')
            for fType in types
            if fType in self.__file
        )
        self.__file = ''.join(de_Typed)

    def __read_yml(self):
        file = open(self.__file,"r")#Safer than "with open as:"
        self.__dict = yaml.safe_load(file)
        file.close

    def __read_json(self):
        file = open(self.__file,'r')
        self.__dict = json.load(file)
        file.close()
    
    def __read_ini(self):
        config = self.__config
        config.read(self.__file)
        for section in config.sections():
            self.__dict[section] = {}
            for name,value in config.items(section):
                self.__dict[section].update({name:value})

    def to_yaml(self, mk_file=True):
        fileName= self.__file+(".yaml")
        if not(mk_file):
            return yaml.dump(self.__dict)
        with open(fileName,'w') as file:
            yaml.dump(self.__dict, file)
            file.close()

    def to_json(self, mk_file=True):
        fileName= self.__file+(".json")
        if not(mk_file):
            return json.dumps(self.__dict)

        with open(fileName,'w') as file:
            data = json.dumps(self.__dict,indent=True)
            file.writelines(data)
            file.close

    def to_ini(self, mk_file=True):
        fileName= self.__file+(".ini")
        config = self.__config
        config.read_dict(self.__dict)
        if not(mk_file):
            return config

        with open(fileName,'w') as file:
            config.write(file)
            file.close

dh = Dict_Handler(test.ini)
dh.to_json()
dh.to_yaml()
