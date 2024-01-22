class Convertir:

    @staticmethod
    def f_a_c(f,format=True):
        result = (f -32)*5/9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result
    
    @staticmethod
    def k_a_c(k,format=True):
        result = k-273.15
        if format:
            return f'{k} Kelvin ={result:.2f} Celsius'
        return result
    
    @staticmethod
    def c_a_f(c,format=True):
        result = c * 9/ 5 +32
        if format:
            return f'{c} Celsius ={result:.2f} Fahrenheit'
        return result
    
    @staticmethod
    def k_a_f(k,format=True):
        result = (k-273.15)*9/ 5+32
        if format:
            return f'{k} Kelvin ={result:.2f} Fahrenheit'
        return result
    
    @staticmethod
    def c_a_k(c,format=True):
        result = c + 273.15
        if format:
            return f'{c} Celsius ={result:.2f} Kelvin'
        return result
    
    @staticmethod
    def f_a_k(f,format=True):
        result = (f - 32)*5/9+273.15
        if format:
            return f'{f} Fahrenheit ={result:.2f} Kelvin'
        return result
    
    