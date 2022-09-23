#!/usr/bin/python

import numpy as np
import codecs, json 


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return {    'matrix':
                        {   
                            'array': np.reshape(obj,-1,order='F').tolist(),
                            'nlin' : obj.shape[0],
                            'ncol' : obj.shape[1]
                        }
                    }
        return json.JSONEncoder.default(self, obj)


def numpy_to_json_file(Label,a,filepath):
    ''' 
    Esta función crea un archivo `filepath` en formato json con el contenido 
    del arreglo numpy `a`, usando la etiqueta `Label`.
    
    :param Label: Etiqueta del elemento Json para el arreglo `a`.
    :type Label: string
    :param a: Array numpy.
    :type a: Numpy.Array
    :param filepath: Path del archivo en formato json.
    :type filepath: string
    '''
    json_dump = json.dumps({Label: a}, cls=NumpyEncoder,indent=4)
    # Writing to sample.json
    with open(filepath, "w") as outfile:
        outfile.write(json_dump )

def json_file_to_numpy(filepath,Label):
    '''
    Lee un archivo json y retorna un arreglo numpy.
    
    :param filepath: Path del archivo en formato json.
    :type filepath: string
    :param Label: Etiqueta del objeto Json a buscar en la raiz de filepath.
    :type Label: string
    :return: Retorna un array de numpy.
    :rtype: Numpy.Array
    '''
    # Opening JSON file
    with open(filepath, 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
        try:
            nlin=json_object[Label]['matrix']['nlin'];
            ncol=json_object[Label]['matrix']['ncol'];
            return np.asarray(json_object[Label]['matrix']['array']).reshape(nlin,ncol,order='F')
        except:
            return np.asarray([])
            

'''

a = np.arange(10).reshape(2,5) # a 2 by 5 array

print(a)
numpy_to_json_file("a",a,"matrix.json");

data=json_file_to_numpy("matrix.json","a");
print(data)
'''
