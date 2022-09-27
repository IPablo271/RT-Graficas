from Utilities import *

def writefile(filename,width,height,framebuffer):
    #Esta no necesita recibir ningún nombre de archivo.
        #Abrir en bw: binary write.
        f = open(filename, "bw")
        
        #Pixel header.
        f.write(chart('B'))
        f.write(chart('M'))
        #Tamaño del archivo en bytes. 
        # El 3 es para los 3 bytes que seguirán. El 14 es el tamaño del infoheader y el 40 es el tamaño del otro header.
        f.write(dword(14 + 40 + width * height * 3))
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(word(0)) #Algo que no se usará. Este es de 2 bytes, por eso se utiliza el word.
        f.write(dword(14 + 40)) #Offset a la información de la imagen. 14 bytes para el header, 40 para la información de la imagen. Aquí empieza la data.
        #Lo anterior suma 14 bytes.
        
        #Info header.
        f.write(dword(40)) #Este es el tamaño del header. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(width)) #Ancho de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(height)) #Alto de la imagen. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(word(1)) #Número de planos. Esto es de 2 bytes, por eso se utiliza el word.
        f.write(word(24)) #24 bits por pixel. Esto es porque usa el true color y el RGB.
        f.write(dword(0)) #Esto es la compresión. Esto es de 4 bytes, por eso se utiliza el dword.
        f.write(dword(width * height * 3)) #Tamaño de la imagen sin el header.
        #Pixels que no se usarán mucho.
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        #Lo anterior suma 40 bytes.

        
        
        for y in range(height):
            for x in range(width):
                f.write(framebuffer[y][x])
        f.close()
