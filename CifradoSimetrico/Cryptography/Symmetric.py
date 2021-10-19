from typing import ValuesView


class Symmetric : 
    __pathEnv = ''
    __simetryKeys = {}
    __simetryValues = {}

    def __init__ (self, pathEnv = '') :
        self.__pathEnv = pathEnv
        self.__createDictionary(self.__getKeysAndValues())
    
    # Getters and setters
    @property
    def pathEnv (self) :
        return self.__pathEnv

    @pathEnv.setter
    def pathEnv (self, pathEnv) :
        self.__pathEnv = pathEnv

    # Private functions
    def __getKeysAndValues (self) :        
        """
        Explora el archivo .env para obtener las claves y valores.
        """
        keysAndValues = []

        try:
            # Abre el archivo .env para obtener las llaves y los valores
            lines = open(self.pathEnv + '.env', 'r')
            # Obtiene las llaves y los valores cumpliendo con las reglas descritas en el archivo .env
            for line in lines :
                isKeysOrValues = True
                # Trim String
                line = line.strip()

                isKeysOrValues &= not(line.startswith('##'))
                isKeysOrValues &= len(line) > 0

                if isKeysOrValues :
                    keysAndValues.append(line)
            
            if (len(keysAndValues[0]) == 0 or len(keysAndValues[1]) == 0):
                print('Error: No existen los strings o hace falta un string para realizar el cifrado')
                keysAndValues = []
            elif len(keysAndValues[0]) != len(keysAndValues[1]):
                print('Error: Los strings en el archivo .env no cuentan con el mismo número de caracteres')
                keysAndValues = []
        except:
            print('Error: Error al abrir el archivo .env')
            keysAndValues = []

        return keysAndValues
        
    def __createDictionary (self, keysAndValues) :
        """
        Crea el diccionario que representará el cifrado simétrico
        """ 
        if len(keysAndValues) > 1 :
            keys = keysAndValues[0]
            values = keysAndValues[1] 
            dictionaryKeys = {}
            dictionaryValues = {}

            # Verifica que no existan posiciones repetidas 
            for index, key in enumerate(keys):
                if dictionaryKeys.get(key, None) == None:
                    value = values[index]
                    dictionaryKeys[key] = value
                    dictionaryValues[value] = key
                else: 
                    print('Error: En uno de tus strings hay caracteres repetidos.')
                    dictionaryKeys = {}
                    dictionaryValues = {}
                    break
            
            self.__simetryKeys = dictionaryKeys
            self.__simetryValues = dictionaryValues
        else :
            print('Error al crear el diccionario')


    # Public functions
    def allItsFine (self): 
        """
        Verifica que no le falte nada
        """
        flag = True
        flag &= len(self.__simetryKeys) > 0
        flag &= len(self.__simetryValues) > 0 
        
        return flag

    def encode (self, message): 
        """
        Codifica el mensaje
        """ 
        encodeMessage = ''

        for car in message:
            encodeMessage += self.__simetryValues[car]
        
        return encodeMessage
    
    def decode (self, message):
        """
        Decodifica el mensaje
        """

        decodeMessage = ''

        for car in message:
            decodeMessage += self.__simetryKeys[car]
        
        return decodeMessage
      

