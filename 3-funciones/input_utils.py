"""
    Utilidades para leer datos por consola
"""
def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError as VE:
            print('Value Error ', VE)
        # except Error as VE:
        #     print('Value Error ', VE)
        except Exception as E:
            print('Error generico ', E.__class__)
        finally:
            print("finally")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as VE:
            print('Value Error ', VE)
        except Exception as E:
            print('Error generico ', E.__class__)
        finally:
            print("finally")        

def read_bool(prompt):
    while True:
        try:
            return bool(int(input(prompt)))
            # resp = bool(int(input(prompt)))
            # return resp.lower() in ['si', 'yes', 'sí', 0, 1]
        except ValueError as VE:
            print('Value Error ', VE)
        except Exception as E:
            print('Error generico ', E.__class__)
        finally:
            print("finally")    
                      
# edad_int = read_int('Introduce int: ')
# edad_float = read_float('Introduce float: ')
# edad_bool = read_bool('Introduce bool: ')
# print(edad_bool)