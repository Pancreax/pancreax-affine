################################################################################################
#### O script mais pancreático para demonstração de python, openCV e Affine Transformation  ####
####                                                                                        ####
####                                   Cyber Pancreax                                       ####
####                                                                                        ####
################################################################################################

## Dependencias

import cv2              ## OpenCV: Biblioteca multiplataforma para visão computacional https://opencv.org/
from mss import mss     ## Multiple Screen Shots: módulo "ultra cross platform" para screen shots https://github.com/BoboTiG/python-mss
import numpy as np      ## NumPy: "O pacote fundamental para computação científica com python" https://numpy.org/


## Definindo o tamanho da tela
leftscreen = {'width':1366, 'height':768}

## Definindo a área que o mss vai capturar
boundindBox = {'top':0,
               'left':0,
               **leftscreen}

## instancia o mss
with mss() as screenshooter:

    ## loop infinito
    while(True):

        ## Captura uma screenshot
        image = np.array(screenshooter.grab(boundindBox))

        ## Define a matriz da transformação afim. 
        matrix = np.float32([[ 1, -6,  0],
                             [ 0,  1,  0]])

        ## Aplica a transformação
        image2 = cv2.warpAffine(image,matrix,None,borderMode=cv2.BORDER_WRAP)

        ## Exibe a imagem por 10 milisegundos e verifica se alguma tecla foi pressionada
        keypressed = cv2.waitKey(10) & 0xFF
        cv2.imshow('imagem',image2)

        ## Sai do loop se a tecla 'q' foi pressionada
        if (keypressed == ord('q')):
            cv2.destroyAllWindows()
            break
