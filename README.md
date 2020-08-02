# Pancreax affine

Script utilizado no [primeiro vídeo do canal Cyber Pancreax](https://youtu.be/DKa1_2w4fMM) para aplicar affine transformations em capturas de tela.

**Como executar:**

 - Clonar este repositório
```
git clone https://github.com/Pancreax/pancreax-affine
cd pancreax-affine
```

 - Instalar o [virtualenv](https://virtualenv.pypa.io/en/latest/), para evitar séculos de dor com infinitas combinações de versões de python e dependências:
```
sudo apt install python3-virtualenv
```

 - Criar um novo virtual enviroment com o nome que desejar. Pode ser, pancreas, jairo, joaozinho... Aqui eu chamarei de `env`.
```
virtualenv env 
```

 - Ativar o virtual enviroment que você acabou de criar.
```
source env/bin/activate
```

 - Instalar o `opencv` e o `mss`
```
pip install opencv-python
pip install mss
```

 - O código fonte está no arquivo `affine.py` na pasta `src`. O funcionamento específico dele vai depender da sua configuração de tela. Altere o tamanho da tela e da bounding box de acordo com a sua necessidade. Ao executar, o código, será aberta uma janela que exibirá a screenshot capturada sendo aplicada a transformação definida no código.
```
cd src
python affine.py
```

 - Quando terminar de brincar, você pode desativar o virtual enviroment com o seguinte comando, ou simplesmente fechar o terminal:
```
deactivate
```

 - Divirta-se! :)